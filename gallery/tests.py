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

    def test_delete_method(self):
        self.test_location = Location(image_location='Canada')
        self.test_location.save_location()
        self.test_location.delete_location()
        loc = Location.objects.all()
        self.assertTrue(len(loc)<1)

    def test_update_method(self):
        self.test_location = Location(image_location='Canada')
        self.test_location.save_location()
        update = Location.update_location('Canada','USA')
        self.assertTrue(update,'USA')


class CategoryTestClass(TestCase):

    def setUp(self):
        self.space = Category(image_category='SpaceX')


    def test_instance(self):
        self.assertTrue(isinstance(self.space,Category))

    def test_save_method(self):
        self.space.save_category()
        space = Category.objects.all()
        self.assertTrue(len(space)>0)

    def test_delete_method(self):
        self.test_category = Category(image_category='SpaceX')
        self.test_category.save_category()
        self.test_category.delete_category()
        cat = Category.objects.all()
        self.assertTrue(len(cat)<1)

    def test_update_method(self):
        self.test_category = Category(image_category='SpaceX')
        self.test_category.save_category()
        update = Category.update_category('SpaceX','Blue Origin')
        self.assertTrue(update,'Blue Origin')


# class ImageTestClass(TestCase):
#
#     def setUp(self):
#         self.image = Image(image_name='Elon',image_description='Love',image_date='2018-07-04',image='love.jpg',category='SpaceX',location='Canada')
#
#     def test_instance(self):
#         self.assertTrue(isinstance(self.image,Image))
#
#     def test_save_method(self):
#         self.image.save_image()
#         image = Image.objects.all()
#         self.assertTrue(len(image)>0)





