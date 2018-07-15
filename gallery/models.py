from django.db import models
import datetime as dt
# Create your models here.

class Category(models.Model):
    CATEGORIES =(("SpaceX","SpaceX"),("Blue Origin","Blue Origin"),("Virgin Atlantic","Virgin Atlantic"))

    image_category = models.CharField(max_length=40,choices=CATEGORIES,)

class Location(models.Model):
    LOCATIONS=(("USA","USA"),("Canada","Canada"),("Britain","Britain"))

    image_location = models.CharField(max_length=40,choices=LOCATIONS,)

class Image(models.Model):
    image_name = models.CharField(max_length=30)
    image_description = models.TextField()
    image_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category)
    location = models.ForeignKey(Location)


    @classmethod
    def get_image(cls):
        image = cls.objects.get('image_name')
        return image
