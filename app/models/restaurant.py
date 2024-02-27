from PIL import Image
from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver


class RestaurantResult(models.Model):
    title = models.CharField(max_length=255)
    rank = models.PositiveIntegerField(default=1, null=True, blank=True)
    plus = models.BooleanField(default=False)

    def __str__(self):
        return self.title


# RestaurantGallery --------------------------------------------------------------------
class RestaurantGallery(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='restaurant_gallery/')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Call the parent class's save() method
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        max_width = 1000
        max_height = 800

        if img.width > max_width or img.height > max_height:
            new_size = (max_width, max_height)
            img.thumbnail(new_size, Image.Resampling.LANCZOS)
            img.save(self.image.path)

@receiver(post_delete, sender=RestaurantGallery)
def delete_blog_image(sender, instance, **kwargs):
    # Delete the image file when the AboutBanner instance is deleted
    instance.image.delete(save=False)


@receiver(pre_save, sender=RestaurantGallery)
def delete_blog_old_image(sender, instance, **kwargs):
    # Delete the old image file when the AboutBanner instance is updated with a new image
    if instance.pk:
        try:
            old_instance = sender.objects.get(pk=instance.pk)
            if old_instance.image != instance.image:
                old_instance.image.delete(save=False)

        except sender.DoesNotExist:
            pass


# RestaurantGallery  End --------------------------------------------------------------------

class MenuCategory(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


# Menu ----------------------------------------------------------------------------
class Menu(models.Model):
    image = models.ImageField(upload_to='menus/')
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=40, null=True, blank=True)
    price = models.PositiveIntegerField(default=1)
    popular = models.BooleanField(default=False)
    category = models.ForeignKey(MenuCategory, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Call the parent class's save() method
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        max_width = 1000
        max_height = 800

        if img.width > max_width or img.height > max_height:
            new_size = (max_width, max_height)
            img.thumbnail(new_size, Image.Resampling.LANCZOS)
            img.save(self.image.path)


@receiver(post_delete, sender=Menu)
def delete_blog_image(sender, instance, **kwargs):
    # Delete the image file when the AboutBanner instance is deleted
    instance.image.delete(save=False)


@receiver(pre_save, sender=Menu)
def delete_blog_old_image(sender, instance, **kwargs):
    # Delete the old image file when the AboutBanner instance is updated with a new image
    if instance.pk:
        try:
            old_instance = sender.objects.get(pk=instance.pk)
            if old_instance.image != instance.image:
                old_instance.image.delete(save=False)

        except sender.DoesNotExist:
            pass
