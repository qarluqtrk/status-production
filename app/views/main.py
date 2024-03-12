from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _

from app.forms import ContactModelForm, BookingModelForm
from app.models.blog import Blog
from app.models.gallery import GalleryCategory, Gallery
from app.models.other import Around, Review, Banner, Views, Service, Visitor
from app.models.restaurant import Menu
from app.models.room import Room, Amenity


def index_view(request):
    if request.method == "POST":
        form = BookingModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = BookingModelForm()
    rooms = Room.objects.all()
    arounds = Around.objects.all()[:3]
    reviews = Review.objects.filter(is_active=True, main=True).order_by('created_at').all()
    blogs = Blog.objects.all()
    banner = Banner.objects.first()
    amenities = Amenity.objects.filter(main=True).all()[:4]
    views = Views.objects.all()
    visitors = Visitor.objects.all()

    return render(request=request, template_name='app/index.html',
                  context={'rooms': rooms,
                           'arounds': arounds,
                           'reviews': reviews,
                           'blogs': blogs,
                           'banner': banner,
                           'amenities': amenities,
                           'views': views,
                           'form': form,
                           'visitors': visitors})


def about_view(request):
    if request.method == "POST":
        form = BookingModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = BookingModelForm()
    reviews = Review.objects.filter(is_active=True, main=True).order_by('created_at').all()
    blogs = Blog.objects.all()[:3]
    amenities = Amenity.objects.filter(general=True).all()
    services = Service.objects.all()
    return render(request=request, template_name='app/about.html',
                  context={"blogs": blogs,
                           "reviews": reviews,
                           "amenities": amenities,
                           "services": services,
                           "form": form})


def contact_view(request):
    if request.method == "POST":
        form_type = request.POST.get('form_type')
        if form_type == 'form1':
            form = ContactModelForm(data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')
            else:
                message = _("Telefon raqamingizni kiritishda xatolik bor! Iltimos, to'g'ri raqam kiriting.")
                messages.add_message(request, messages.ERROR, message)
                return redirect('contact')
        elif form_type == 'form2':
            form = BookingModelForm(data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')
    form = ContactModelForm()

    return render(request=request, template_name='app/contact.html',
                  context={'form': form})


def gallery_view(request):
    if request.method == "POST":
        form = BookingModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = BookingModelForm()
    categories = GalleryCategory.objects.all()
    products = Menu.objects.all()
    images = Gallery.objects.all()
    rooms = Room.objects.all()
    reviews = Review.objects.filter(is_active=True, main=True).order_by('created_at').all()
    return render(request=request, template_name='app/gallery.html',
                  context={'categories': categories,
                           'products': products,
                           'images': images,
                           "rooms": rooms,
                           "reviews": reviews,
                           "form": form})


def bad_request_view(request, exception):
    return render(request=request, template_name='app/404.html')


from urllib.parse import urlparse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation


# This code sets the language
def set_language(request, language):
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None
        if view:
            break
    if view:
        translation.activate(language)
        next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        response = HttpResponseRedirect(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    else:
        response = HttpResponseRedirect("/")
    return response
