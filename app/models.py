from django.db import models


# Create your models here.


class Banner(models.Model):
    title = models.CharField(max_length=255)
    image = models.FileField(upload_to='banners/')
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class Views(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField()

    def __str__(self):
        return self.title


class Visitor(models.Model):
    title = models.CharField(max_length=255)
    count = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title


class MenuCategory(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Menu(models.Model):
    image = models.ImageField(upload_to='menus/')
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=40, null=True, blank=True)
    price = models.PositiveIntegerField(default=1)
    popular = models.BooleanField(default=False)
    category = models.ForeignKey(MenuCategory, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title


class GalleryCategory(models.Model):
    title = models.CharField(max_length=155)

    def __str__(self):
        return self.title


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/')
    category = models.ForeignKey(GalleryCategory, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.category.title + ' - ' + self.image.url


class RestaurantResult(models.Model):
    title = models.CharField(max_length=255)
    rank = models.PositiveIntegerField(default=1, null=True, blank=True)
    plus = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class RestaurantGallery(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='restaurant_gallery/')

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


class RoomImages(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE,
                             related_name='room_images')
    image = models.ImageField(upload_to='room_images/', null=True, blank=True)

    def __str__(self):
        return self.room.title + ' - ' + self.image.url


class Amenity(models.Model):
    title = models.CharField(max_length=255)
    main = models.BooleanField(default=False)
    general = models.BooleanField(default=False)
    image = models.ImageField(upload_to='amenities/', null=True, blank=True)

    def __str__(self):
        return self.title


class RoomAmenity(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE,
                             related_name='room_amenities')
    amenity = models.ForeignKey(Amenity, on_delete=models.CASCADE,
                                related_name='room_amenities')

    def __str__(self):
        return self.room.title + ' - ' + self.amenity.title


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
    phone_number = models.CharField(max_length=25)
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


class Around(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='arounds/', null=True, blank=True)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    text = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='blogs/')
    mini_image = models.ImageField(upload_to='blogs/')
    mini_image2 = models.ImageField(upload_to='blogs/')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE,
                             related_name='comments')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    image = models.ImageField(upload_to='services/')
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
