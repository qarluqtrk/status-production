from django.shortcuts import render


def index_view(request):
    return render(request=request, template_name='app/index.html')


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
