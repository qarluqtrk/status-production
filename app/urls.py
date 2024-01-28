from django.urls import path

from app.views import index_view, about_view, rooms_view, room_details_view, services_view, restaurant_view, blog_view, \
    post_view, contact_view, bad_request_view

urlpatterns = [
    path('', index_view, name='index'),
    path('about/', about_view, name='about'),
    path('rooms/', rooms_view, name='rooms'),
    path('room_details/', room_details_view, name='room-details'),
    path('services/', services_view, name='services'),
    path('restaurant/', restaurant_view, name='restaurant'),
    path('blog/', blog_view, name='blog'),
    path('post/', post_view, name='post'),
    path('contact/', contact_view, name='contact'),
    path('404/', bad_request_view, name='404'),
]