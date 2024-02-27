from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from app.models.blog import Blog, Comment
from app.models.gallery import GalleryCategory, Gallery
from app.models.other import Banner, Views, Visitor, Around, Review, Service, MainSocial, Contact, Booking
from app.models.restaurant import MenuCategory, Menu, RestaurantResult, RestaurantGallery
from app.models.room import Amenity, Room, RoomCategory, RoomImages, RoomAmenity


class CustomTranslationAdmin(TranslationAdmin):
    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Banner)
class BannerAdmin(CustomTranslationAdmin):
    list_display = ('title', 'text')


@admin.register(Amenity)
class AmenityAdmin(CustomTranslationAdmin):
    list_display = ('title',)


@admin.register(Views)
class ViewsAdmin(CustomTranslationAdmin):
    list_display = ('title',)


@admin.register(Visitor)
class VisitorAdmin(CustomTranslationAdmin):
    list_display = ('title',)


@admin.register(Around)
class AroundAdmin(CustomTranslationAdmin):
    list_display = ('title', 'description')


@admin.register(Room)
class RoomAdmin(CustomTranslationAdmin):
    list_display = ('title', 'description')


@admin.register(RoomCategory)
class RoomCategoryAdmin(CustomTranslationAdmin):
    list_display = ('title',)


@admin.register(Blog)
class BlogAdmin(CustomTranslationAdmin):
    list_display = ('title', 'description', 'text')


@admin.register(Review)
class ReviewAdmin(CustomTranslationAdmin):
    list_display = ('country', 'message')


@admin.register(MenuCategory)
class MenuCategoryAdmin(CustomTranslationAdmin):
    list_display = ('title',)


@admin.register(Menu)
class MenuAdmin(CustomTranslationAdmin):
    list_display = ('title', 'text')


@admin.register(RestaurantResult)
class RestaurantResultAdmin(CustomTranslationAdmin):
    list_display = ('title',)


@admin.register(RestaurantGallery)
class RestaurantGalleryAdmin(CustomTranslationAdmin):
    list_display = ('title',)


@admin.register(GalleryCategory)
class GalleryCategoryAdmin(CustomTranslationAdmin):
    list_display = ('title',)


@admin.register(Service)
class ServiceAdmin(CustomTranslationAdmin):
    list_display = ('title', "description")


admin.site.register([
    RoomImages,
    RoomAmenity,
    Gallery,
    MainSocial,
    Contact,
    Comment,
    Booking
])
