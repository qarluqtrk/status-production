from django.urls import path

from app.views.blog.blog_details import blog_details_view
from app.views.blog.blogs import blogs_view
from app.views.other.main import index_view, about_view, restaurant_view, menu_view, contact_view, gallery_view, \
    faq_view, bad_request_view
from app.views.room.room_details import room_details
from app.views.room.rooms import rooms_view

urlpatterns = [
    path('', index_view, name='index'),
    path('about/', about_view, name='about'),
    path('rooms/', rooms_view, name='rooms'),
    path('room_details/', room_details, name='room_details'),
    path('restaurant/', restaurant_view, name='restaurant'),
    path('menu/', menu_view, name='menu'),
    path('contact/', contact_view, name='contact'),
    path('blogs/', blogs_view, name='blogs'),
    path('blog_details/', blog_details_view, name='blog_details'),
    path('gallery/', gallery_view, name='gallery'),
    path('faq/', faq_view, name='faq'),
    path('404/', bad_request_view, name='404'),
]
