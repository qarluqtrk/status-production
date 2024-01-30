from django.db import models


# Create your models here.

class RoomImage(models.Model):
    image = models.ImageField()


class Room(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(default=1)
    image = models.ForeignKey(RoomImage, on_delete=models.CASCADE, related_name="room")
    person = models.IntegerField(default=1, null=True, blank=True)
    size = models.IntegerField(default=1, null=True, blank=True)

    def __str__(self):
        return self.title
