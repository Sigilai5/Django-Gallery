from django.test import TestCase
from . models import Image,Location,Category

# Create your tests here.
class LocationTestClass(TestCase):

    def setUp(self):
        self.can = Location(image_location='Canada')


    def test_instance(self):
        self.assertTrue(isinstance(self.can,Location))

    def test_save_method(self):
        self.can.save_location()
        loc = Location.objects.all()
        self.assertTrue(len(loc)>0)







