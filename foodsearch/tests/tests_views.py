
from django.test import Client, TestCase
from django.test.utils import setup_test_environment



class FoodSearchTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_different_food_descriptions(self):
        """ 
        name different foods that we should be able to look up 
        """ 
        list_of_valid_food_choices = ['bread', 'BrEAD', 'cookies','']

