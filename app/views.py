from django.shortcuts import render


def index_view(request):
    return render(request, 'app/index.html')


def about_view(request):
    return render(request, 'app/about.html')


def rooms_view(request):
    return render(request, 'app/rooms.html')


def room_details_view(request):
    return render(request, 'app/room-details.html')


def services_view(request):
    return render(request, 'app/services.html')


def restaurant_view(request):
    return render(request, 'app/restaurant.html')


def blog_view(request):
    return render(request, 'app/blog.html')


def post_view(request):
    return render(request, 'app/post.html')


def contact_view(request):
    return render(request, 'app/contact.html')


def bad_request_view(request):
    return render(request, 'app/404.html')
