from PIL import Image
from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver


class GalleryCategory(models.Model):
    title = models.CharField(max_length=155)

    def __str__(self):
        return self.title


# Gallery    --------------------------------------------------------------------------------------
class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/')
    category = models.ForeignKey(GalleryCategory, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.category.title + ' - ' + self.image.url

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


@receiver(post_delete, sender=Gallery)
def delete_blog_image(sender, instance, **kwargs):
    # Delete the image file when the AboutBanner instance is deleted
    instance.image.delete(save=False)


@receiver(pre_save, sender=Gallery)
def delete_blog_old_image(sender, instance, **kwargs):
    # Delete the old image file when the AboutBanner instance is updated with a new image
    if instance.pk:
        try:
            old_instance = sender.objects.get(pk=instance.pk)
            if old_instance.image != instance.image:
                old_instance.image.delete(save=False)

        except sender.DoesNotExist:
            pass

# Gallery End   --------------------------------------------------------------------------------------
