from PIL import Image
from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver


class Amenity(models.Model):
    title = models.CharField(max_length=255)
    main = models.BooleanField(default=False)
    general = models.BooleanField(default=False)
    image = models.ImageField(upload_to='amenities/', null=True, blank=True)

    def __str__(self):
        return self.title


class RoomCategory(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='room_categories/', null=True, blank=True)

    def __str__(self):
        return self.title


class Room(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.PositiveIntegerField(default=1)
    size = models.PositiveIntegerField(null=True, blank=True)
    person = models.PositiveIntegerField(null=True, blank=True)
    category = models.ForeignKey(RoomCategory, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title


# Room Images       ---------------------------------------------------------------------
class RoomImages(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE,
                             related_name='room_images')
    image = models.ImageField(upload_to='room_images/', null=True, blank=True)

    def __str__(self):
        return self.room.title + ' - ' + self.image.url

    def save(self, *args, **kwargs):
        # Call the parent class's save() method
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        max_width = 1300
        max_height = 1100

        if img.width > max_width or img.height > max_height:
            new_size = (max_width, max_height)
            img.thumbnail(new_size, Image.Resampling.LANCZOS)
            img.save(self.image.path)


@receiver(post_delete, sender=RoomImages)
def delete_blog_image(sender, instance, **kwargs):
    # Delete the image file when the AboutBanner instance is deleted
    instance.image.delete(save=False)


@receiver(pre_save, sender=RoomImages)
def delete_blog_old_image(sender, instance, **kwargs):
    # Delete the old image file when the AboutBanner instance is updated with a new image
    if instance.pk:
        try:
            old_instance = sender.objects.get(pk=instance.pk)
            if old_instance.image != instance.image:
                old_instance.image.delete(save=False)

        except sender.DoesNotExist:
            pass


# Room Images   End    ---------------------------------------------------------------------

class RoomAmenity(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE,
                             related_name='room_amenities')
    amenity = models.ForeignKey(Amenity, on_delete=models.CASCADE,
                                related_name='room_amenities')

    def __str__(self):
        return self.room.title + ' - ' + self.amenity.title
