from modeltranslation.translator import TranslationOptions, register

from app.models import Banner, Amenity, Views, Visitor, Around, Room, RoomCategory, Blog, Review, MenuCategory, Menu, \
    RestaurantResult, RestaurantGallery, GalleryCategory


@register(Banner)
class BannerTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


@register(Amenity)
class AmenityTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Views)
class ViewsTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Visitor)
class VisitorTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Around)
class AroundTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Room)
class RoomTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(RoomCategory)
class RoomCategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Blog)
class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'text')


@register(Review)
class ReviewTranslationOptions(TranslationOptions):
    fields = ('country', 'message')


@register(MenuCategory)
class MenuCategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Menu)
class MenuTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


@register(RestaurantResult)
class RestaurantResultTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(RestaurantGallery)
class RestaurantGalleryTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(GalleryCategory)
class GalleryCategoryTranslationOptions(TranslationOptions):
    fields = ('title',)
