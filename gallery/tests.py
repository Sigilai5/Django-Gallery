from django.test import TestCase
from . models import Image,Location,Category

# Create your tests here.
class ImageTestClass(TestCase):

    def setUp(self):
        self.mario = Image(image_name='Mario',image_description='Love',image_date='2018-02-21',category='SpaceX',location='Canada')


    def test_instance(self):
        self.assertTrue(isinstance(self.mario,Image))

    def test_save_method(self):
        self.mario.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>1)

