from django.shortcuts import render, redirect

from app.forms import ContactModelForm
from app.models import Room, Around, Review, Blog, Banner, Amenity, Views, GalleryCategory, Menu, Gallery, Service


def index_view(request):
    rooms = Room.objects.all()
    arounds = Around.objects.all()[:3]
    reviews = Review.objects.filter(is_active=True, main=True).order_by('created_at').all()
    blogs = Blog.objects.all()
    banner = Banner.objects.first()
    amenities = Amenity.objects.filter(main=True).all()[:4]
    views = Views.objects.all()
    return render(request=request, template_name='app/index.html',
                  context={'rooms': rooms,
                           'arounds': arounds,
                           'reviews': reviews,
                           'blogs': blogs,
                           'banner': banner,
                           'amenities': amenities,
                           'views': views})


def about_view(request):
    reviews = Review.objects.filter(is_active=True, main=True).order_by('created_at').all()
    blogs = Blog.objects.all()[:3]
    amenities = Amenity.objects.filter(general=True).all()[:4]
    services = Service.objects.all()
    return render(request=request, template_name='app/about.html',
                  context={"blogs":blogs,
                           "reviews":reviews,
                           "amenities":amenities,
                           "services":services})


def contact_view(request):
    if request.method == "POST":
        form = ContactModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            message = "Ma'lumotlarni kiritishda xatolik bor!"
            # messages.add_message(request, message=message)
            return redirect('contact')
    return render(request=request, template_name='app/contact.html')


def gallery_view(request):
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
                           "reviews": reviews})


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
