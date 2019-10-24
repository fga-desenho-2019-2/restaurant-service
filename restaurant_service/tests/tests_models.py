from django.test import TestCase
from model_mommy import mommy
from restaurant_service.api.models import (
    Shopping, 
    OpeningHours, 
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


class TestOpeningHours(TestCase):
  def setUp(self):
    self.opening_hours = mommy.make(OpeningHours, 
      day = 'Segunda-feira',
      start_time = '10:00:00',
      end_time = '22:00:00',
    )
      
  def test_shopping_creation(self):
    self.assertTrue(isinstance(self.opening_hours, OpeningHours))


class TestRestaurantCategory(TestCase):
  def setUp(self):
    self.restaurant_category = mommy.make(RestaurantCategory, name = 'Fast Food' )
      
  def test_shopping_creation(self):
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
    self.opening_hours_monday = mommy.make(OpeningHours, 
      day = 'Segunda-feira',
      start_time = '10:00:00',
      end_time = '22:00:00',
    )
    self.opening_hours_thuesday = mommy.make(OpeningHours, 
      day = 'Terça-feira',
      start_time = '10:00:00',
      end_time = '22:00:00',
    )
    self.category = mommy.make(RestaurantCategory, name = 'Fast-food' )
    self.restaurant = mommy.make(Restaurant, 
      cnpj = '13339532',
      name = 'Burger King',
      store_number = 112,
      description = 'O melhor FastFood',
      phone = '99999999999',
      shopping = self.shopping,
      category = self.category,
      opening_hours = [self.opening_hours_monday, self.opening_hours_thuesday],
    )
      
  def test_shopping_creation(self):
    self.assertTrue(isinstance(self.restaurant, Restaurant))
    self.assertEquals(self.restaurant.__str__(), self.restaurant.name)


class TestMenu(TestCase):
  def setUp(self):
    self.restaurant = mommy.make(Restaurant, 
      cnpj = '13339532',
      name = 'Burger King',
      store_number = 112,
      description = 'O melhor FastFood',
      phone = '99999999999',
    )
    self.menu = mommy.make(Menu, description = 'Combos', restaurant = self.restaurant)
      
  def test_shopping_creation(self):
    self.assertTrue(isinstance(self.menu, Menu))
    self.assertEquals(self.menu.__str__(), self.menu.description)


class TestItem(TestCase):
  def setUp(self):
    self.menu = mommy.make(Menu, description = 'Combos')
    self.category = mommy.make(ItemCategory, 
      title = 'Escolha um molho',
      description = 'Escolha apenas 1 molho',
      required = True, 
      number_of_items = 1
    )
    self.item = mommy.make(Item, 
      name = 'X-Salada',
      value = 20.50,
      description = 'Sanduiche muito gostoso', 
      preparation_time = '00:15:00',
      menu = self.menu,
      category = self.category
    )
      
  def test_shopping_creation(self):
    self.assertTrue(isinstance(self.item, Item))
    self.assertEquals(self.item.__str__(), self.item.name)


class TestItemCategory(TestCase):
  def setUp(self):
    self.item_category = mommy.make(ItemCategory, 
      title = 'Escolha um molho',
      description = 'Escolha apenas 1 molho',
      required = True, 
      number_of_items = 1
    )
      
  def test_shopping_creation(self):
    self.assertTrue(isinstance(self.item_category, ItemCategory))
    self.assertEquals(self.item_category.__str__(), self.item_category.title)


class TestComplement(TestCase):
  def setUp(self):
    self.item_category = mommy.make(ItemCategory, 
      title = 'Escolha um molho',
      description = 'Escolha apenas 1 molho',
      required = True, 
      number_of_items = 1,
    )
    self.complement = mommy.make(Complement, 
      title = 'Maionese',
      description = 'Maionese especial do BK',
      value = 1.00, 
      item_category = self.item_category,
    )
      
  def test_shopping_creation(self):
    self.assertTrue(isinstance(self.complement, Complement))
    self.assertEquals(self.complement.__str__(), self.complement.title)
