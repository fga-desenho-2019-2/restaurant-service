from django.test import TestCase
from model_mommy import mommy
from django.utils.timezone import datetime
from restaurant_service.models import Shopping, OpeningHours, RestaurantCategory, Restaurant, Menu, ItemMenu, ItemCategory, CategoryOption

class TestShopping(TestCase):
  def setUp(self):
      self.shopping = mommy.make(Shopping, 
        cnpj = '13.339.532/0001-09',
        name = 'Shopping Mauá',
        latitude = -15.837045,
        longitude = -48.033509,
        city = 'Mauá City',
        state = 'Tocantis',
        country = 'Brasil',
        neighborhood = 'Bairro das Castanheiras',
        street = 'Rua 198',
        number = 10,
        phone = '99999999999'
      )
      
  def test_shopping_creation(self):
      self.assertTrue(isinstance(self.shopping, Shopping))
      self.assertEquals(self.shopping.__str__(), self.shopping.name)

