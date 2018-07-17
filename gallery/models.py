from django.db import models
import datetime as dt
# Create your models here.

class Category(models.Model):
    CATEGORIES =(("SpaceX","SpaceX"),("Blue Origin","Blue Origin"),("Virgin Atlantic","Virgin Atlantic"))

    image_category = models.CharField(max_length=40,choices=CATEGORIES,)

    def save_category(self):
        self.save()
    def __str__(self):
        return self.image_category

class Location(models.Model):
    LOCATIONS=(("USA","USA"),("Canada","Canada"),("Britain","Britain"))

    image_location = models.CharField(max_length=40,choices=LOCATIONS,)

    def save_location(self):
        self.save()
    def __str__(self):
        return self.image_location

class Image(models.Model):
    image_name = models.CharField(max_length=30)
    image_description = models.TextField()
    image_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/',default='nothing')
    category = models.ForeignKey(Category)
    location = models.ForeignKey(Location)

    def __str__(self):
        return self.image_name
    def __unicode__(self):
        return self.category


    class Meta:
        ordering = ['image_name']

    def save_image(self):
        self.save()

    @classmethod
    def search_by_title(cls,search_term):
        image = cls.objects.filter(image_name__icontains=search_term)
        return image

    @classmethod
    def filter_location(cls,location):
        # location = Location.objects.(image_location=location)
        images = cls.objects.filter(location__image_location__istartswith=location)
        return images

    # @classmethod
    # def get_image(cls):
    #     image = cls.objects.filter(category__image_category__contains='SpaceX')
    #
    #     return image




