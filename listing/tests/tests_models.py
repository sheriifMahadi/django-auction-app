from django.test import TestCase
from django.contrib.auth.models import User


from listing.models import Category, Listing

class TestCategoriesModel(TestCase):
    
    def setUp(self):
        self.data1 = Category.objects.create(name='Tech', slug='tech')

    def test_category_name(self):
        """Test string returned as name"""

        data = self.data1
        self.assertEqual(str(data), 'Tech')
    

class TestListingModel(TestCase):

    def setUp(self):
        Category.objects.create(name='Tech', slug='tech')
        User.objects.create(username='xxxx')
        self.data1 = Listing.objects.create(category_id=1, item='IBM PC', 
                                            created_by_id=1, slug='ibm pc',
                                            price='20.00', image='img1_DCytNvp.png', is_active=True)

    def test_listing_name(self):
            """Test string returned as name"""

            data = self.data1
            self.assertEqual(str(data), 'IBM PC')
        