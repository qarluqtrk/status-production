from PIL import Image
from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver


# Blog    --------------------------------------------------------------------------------------
class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    text = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='blogs/')
    mini_image = models.ImageField(upload_to='blogs/')
    mini_image2 = models.ImageField(upload_to='blogs/')
    created_at = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Call the parent class's save() method
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        img2 = Image.open(self.mini_image.path)
        img3 = Image.open(self.mini_image2.path)

        max_width = 1100
        max_height = 900

        if img.width > max_width or img.height > max_height:
            new_size = (max_width, max_height)
            img.thumbnail(new_size, Image.Resampling.LANCZOS)
            img.save(self.image.path)

        if img2.width > max_width or img2.height > max_height:
            new_size = (max_width, max_height)
            img2.thumbnail(new_size, Image.Resampling.LANCZOS)
            img2.save(self.mini_image.path)

        if img3.width > max_width or img3.height > max_height:
            new_size = (max_width, max_height)
            img3.thumbnail(new_size, Image.Resampling.LANCZOS)
            img3.save(self.mini_image2.path)

    def __str__(self):
        return self.title


@receiver(post_delete, sender=Blog)
def delete_blog_image(sender, instance, **kwargs):
    # Delete the image file when the AboutBanner instance is deleted
    instance.image.delete(save=False)
    instance.mini_image.delete(save=False)
    instance.mini_image2.delete(save=False)


@receiver(pre_save, sender=Blog)
def delete_blog_old_image(sender, instance, **kwargs):
    # Delete the old image file when the AboutBanner instance is updated with a new image
    if instance.pk:
        try:
            old_instance = sender.objects.get(pk=instance.pk)
            if old_instance.image != instance.image:
                old_instance.image.delete(save=False)

            if old_instance.mini_image != instance.mini_image:
                old_instance.mini_image.delete(save=False)

            if old_instance.mini_image2 != instance.mini_image2:
                old_instance.mini_image2.delete(save=False)

        except sender.DoesNotExist:
            pass


# Blog End   --------------------------------------------------------------------------------------

class Comment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE,
                             related_name='comments')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
