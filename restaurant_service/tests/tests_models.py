from django.test import TestCase
from model_mommy import mommy
from restaurant_service.api.models import (
    Shopping, 
    RestaurantCategory, 
    Restaurant, 
    Menu, 
    Item, 
    ItemCategory, 
    Complement
)


class TestShopping(TestCase):
  def setUp(self):
    self.shopping = mommy.make(Shopping, 
      cnpj = 13339532,
      name = 'Shopping Mauá',
      city = 'Mauá City',
      state = 'Tocantis',
      country = 'Brasil',
      neighborhood = 'Bairro das Castanheiras',
      cep = '7222323',
      number = 10,
      phone = '99999999999',
    )
      
  def test_shopping_creation(self):
    self.assertTrue(isinstance(self.shopping, Shopping))
    self.assertEquals(self.shopping.__str__(), self.shopping.name)


#class TestOpeningHours(TestCase):
#  def setUp(self):
#    self.opening_hours = mommy.make(OpeningHours, 
#      day = 'Segunda-feira',
#      start_time = '10:00:00',
#      end_time = '22:00:00',
#    )
#      
#  def test_shopping_creation(self):
#    self.assertTrue(isinstance(self.opening_hours, OpeningHours))
#

class TestRestaurantCategory(TestCase):
  def setUp(self):
    self.restaurant_category = mommy.make(RestaurantCategory, name = 'Fast Food' )
      
  def test_restaurant_category_creation(self):
    self.assertTrue(isinstance(self.restaurant_category, RestaurantCategory))
    self.assertEquals(self.restaurant_category.__str__(), self.restaurant_category.name)


class TestRestaurant(TestCase):
  def setUp(self):
    self.shopping = mommy.make(Shopping, 
      cnpj = 13339532,
      name = 'Shopping Mauá',
      city = 'Mauá City',
      state = 'Tocantis',
      country = 'Brasil',
      neighborhood = 'Bairro das Castanheiras',
      cep = '7222323',
      number = 10,
      phone = '9999999999',
    )
    self.category = mommy.make(RestaurantCategory, name = 'Fast-food' )
    self.restaurant = mommy.make(Restaurant, 
      cnpj = '13339532',
      name = 'Burger King',
      description = 'O melhor FastFood',
      shopping = self.shopping,
      category = self.category,
      note = 4.8,
      wait_time = "00:12:00"
      #opening_hours = [self.opening_hours_monday, self.opening_hours_thuesday],
    )
      
  def test_restaurant_creation(self):
    self.assertTrue(isinstance(self.restaurant, Restaurant))
    self.assertEquals(self.restaurant.__str__(), self.restaurant.name)


class TestMenu(TestCase):
  def setUp(self):
    self.restaurant = mommy.make(Restaurant, 
      cnpj = '13339532',
      name = 'Burger King',
      note = 4.8,
      wait_time = "00:12:00"
    )
    self.menu = mommy.make(Menu, description = 'Combos', restaurant = self.restaurant)
      
  def test_menu_creation(self):
    self.assertTrue(isinstance(self.menu, Menu))
    self.assertEquals(self.menu.__str__(), self.menu.description)


class TestItem(TestCase):
  def setUp(self):
    self.item = mommy.make(Item, 
      name = 'X-Salada',
      value = 20.50,
      details = 'Sanduiche muito gostoso', 
      category = "1",
      restaurant_cnpj = "12345",
    )
      
  def test_item_creation(self):
    self.assertTrue(isinstance(self.item, Item))
    self.assertEquals(self.item.__str__(), self.item.name)


class TestItemCategory(TestCase):
  def setUp(self):
    self.item_category = mommy.make(ItemCategory, 
      name = 'Escolha um molho',
    )
      
  def test_category_creation(self):
    self.assertTrue(isinstance(self.item_category, ItemCategory))
    self.assertEquals(self.item_category.__str__(), self.item_category.name)


class TestComplement(TestCase):
  def setUp(self):
    self.item = mommy.make(Item, 
      name = 'X-Salada',
      value = 20.50,
      details = 'Sanduiche muito gostoso', 
      category = "1",
      restaurant_cnpj = "12345"
    )
    self.complement = mommy.make(Complement, 
      name = 'Maionese',
      description = 'Maionese especial do BK',
      value = 1.00, 
      selected = False,
      qnt = 1,
      item = self.item
    )
  
    def test_complement_creation(self):
        self.assertTrue(isinstance(self.complement, Complement))
        self.assertEquals(self.complement.__str__(), self.complement.name)
      
