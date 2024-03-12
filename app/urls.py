from django.urls import path

from app.views.blog import blogs_view, blog_details_view
from app.views.main import index_view, about_view, contact_view, gallery_view
from app.views.qr_code import review
from app.views.restaurant import restaurant_view, menu_view
from app.views.room import rooms_view, room_details

urlpatterns = [
    path('', index_view, name='index'),
    path('about/', about_view, name='about'),
    path('rooms/', rooms_view, name='rooms'),
    path('room_details/<int:room_id>/', room_details, name='room_details'),
    path('restaurant/', restaurant_view, name='restaurant'),
    path('menu/', menu_view, name='menu'),
    path('contact/', contact_view, name='contact'),
    path('blogs/', blogs_view, name='blogs'),
    path('blog_details/<int:blog_id>/', blog_details_view, name='blog_details'),
    path('gallery/', gallery_view, name='gallery'),
    path('review/', review, name='review'),


]
