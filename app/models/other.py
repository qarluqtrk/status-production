from PIL import Image
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver

from app.models.room import Room


# Create your models here.

# Banner    ---------------------------------------------------------------------------

class Banner(models.Model):
    title = models.CharField(max_length=255)
    image = models.FileField(upload_to='banners/')
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


@receiver(post_delete, sender=Banner)
def delete_blog_image(sender, instance, **kwargs):
    # Delete the image file when the AboutBanner instance is deleted
    instance.image.delete(save=False)


@receiver(pre_save, sender=Banner)
def delete_blog_old_image(sender, instance, **kwargs):
    # Delete the old image file when the AboutBanner instance is updated with a new image
    if instance.pk:
        try:
            old_instance = sender.objects.get(pk=instance.pk)
            if old_instance.image != instance.image:
                old_instance.image.delete(save=False)

        except sender.DoesNotExist:
            pass


# Banner End ---------------------------------------------------------------------------


# Views      ---------------------------------------------------------------------------
class Views(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='views/')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Call the parent class's save() method
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        max_width = 1100
        max_height = 900

        if img.width > max_width or img.height > max_height:
            new_size = (max_width, max_height)
            img.thumbnail(new_size, Image.Resampling.LANCZOS)
            img.save(self.image.path)


@receiver(post_delete, sender=Views)
def delete_blog_image(sender, instance, **kwargs):
    # Delete the image file when the AboutBanner instance is deleted
    instance.image.delete(save=False)


@receiver(pre_save, sender=Views)
def delete_blog_old_image(sender, instance, **kwargs):
    # Delete the old image file when the AboutBanner instance is updated with a new image
    if instance.pk:
        try:
            old_instance = sender.objects.get(pk=instance.pk)
            if old_instance.image != instance.image:
                old_instance.image.delete(save=False)

        except sender.DoesNotExist:
            pass


# Views End ---------------------------------------------------------------------------
class Visitor(models.Model):
    title = models.CharField(max_length=255)
    count = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title


class Review(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=80)
    message = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    rank = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE,
                             related_name='reviews')
    main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    message = models.TextField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL,
                             related_name='reservations', null=True, blank=True)
    connected = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone_number_regex = RegexValidator(
        regex=r'^\+\d{1,4} \d{1,15}$|^(\+\d{1,4}\d{1,15})$'
    )

    phone_number = models.CharField(max_length=25, validators=[phone_number_regex])
    message = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class MainInfo(models.Model):
    title = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='main_info/', null=True, blank=True)

    def __str__(self):
        return self.title


class MainSocial(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    link = models.CharField(max_length=255)
    image = models.ImageField(upload_to='main_social/')

    def __str__(self):
        return self.title


# Around  ---------------------------------------------------------------------------
class Around(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='arounds/', null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Call the parent class's save() method
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        max_width = 1100
        max_height = 900

        if img.width > max_width or img.height > max_height:
            new_size = (max_width, max_height)
            img.thumbnail(new_size, Image.Resampling.LANCZOS)
            img.save(self.image.path)


@receiver(post_delete, sender=Around)
def delete_blog_image(sender, instance, **kwargs):
    # Delete the image file when the AboutBanner instance is deleted
    instance.image.delete(save=False)


@receiver(pre_save, sender=Around)
def delete_blog_old_image(sender, instance, **kwargs):
    # Delete the old image file when the AboutBanner instance is updated with a new image
    if instance.pk:
        try:
            old_instance = sender.objects.get(pk=instance.pk)
            if old_instance.image != instance.image:
                old_instance.image.delete(save=False)

        except sender.DoesNotExist:
            pass


# Around End ---------------------------------------------------------------------------

# Services   ---------------------------------------------------------------------------
class Service(models.Model):
    image = models.ImageField(upload_to='services/')
    title = models.CharField(max_length=255)
    description = models.TextField()

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


@receiver(post_delete, sender=Service)
def delete_blog_image(sender, instance, **kwargs):
    # Delete the image file when the AboutBanner instance is deleted
    instance.image.delete(save=False)


@receiver(pre_save, sender=Service)
def delete_blog_old_image(sender, instance, **kwargs):
    # Delete the old image file when the AboutBanner instance is updated with a new image
    if instance.pk:
        try:
            old_instance = sender.objects.get(pk=instance.pk)
            if old_instance.image != instance.image:
                old_instance.image.delete(save=False)

        except sender.DoesNotExist:
            pass


class Booking(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=80)
    phone_number_regex = RegexValidator(
        regex=r'^\+\d{1,4} \d{1,15}$|^(\+\d{1,4}\d{1,15})$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    phone_number = models.CharField(validators=[phone_number_regex], max_length=17)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


