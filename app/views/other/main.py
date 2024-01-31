from django.shortcuts import render

from app.models import Room


def index_view(request):
    rooms = Room.objects.all()
    return render(request=request, template_name='app/index.html',
                  context={'rooms': rooms})


def about_view(request):
    return render(request=request, template_name='app/about.html')


def restaurant_view(request):
    return render(request=request, template_name='app/restaurant.html')


def menu_view(request):
    return render(request=request, template_name='app/menu.html')


def contact_view(request):
    return render(request=request, template_name='app/contact.html')


def gallery_view(request):
    return render(request=request, template_name='app/gallery.html')


def faq_view(request):
    return render(request=request, template_name='app/faq.html')


def bad_request_view(request):
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
