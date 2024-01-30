from modeltranslation.translator import TranslationOptions, register

from .models import Room


@register(Room)
class RoomTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
