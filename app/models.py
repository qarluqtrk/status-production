from django.db import models


# Create your models here.


class Room(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    price = models.PositiveIntegerField(default=1)
    person = models.PositiveIntegerField(default=1, null=True, blank=True)
    size = models.PositiveIntegerField(default=1, null=True, blank=True)

    def __str__(self):
        return self.title


class RoomImage(models.Model):
    image = models.ImageField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.room.title
