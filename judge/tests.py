from django.test import TestCase
from .models import Food

class FoodModelTest(TestCase):

    def setUp(self):
        Food.objects.create(name="Chicken", is_meat=True)
        Food.objects.create(name="Carrot", is_meat=False)

    def test_food_is_meat(self):
        chicken = Food.objects.get(name="Chicken")
        carrot = Food.objects.get(name="Carrot")
        self.assertTrue(chicken.is_meat)
        self.assertFalse(carrot.is_meat)

    def test_food_name(self):
        chicken = Food.objects.get(name="Chicken")
        self.assertEqual(chicken.name, "Chicken")