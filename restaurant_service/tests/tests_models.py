from django.test import TestCase
from model_mommy import mommy
# from django.utils.timezone import datetime
from restaurant_service.models import Shopping, OpeningHours, RestaurantCategory, Restaurant, Menu, ItemMenu, ItemCategory, CategoryOption


class TestShopping(TestCase):
  def setUp(self):
    self.shopping = mommy.make(Shopping, 
      cnpj = '13339532000109',
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
      cnpj = '13339532000109',
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
      cnpj = '13339532000109',
      name = 'Burger King',
      number = 112,
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
      cnpj = '13339532000109',
      name = 'Burger King',
      number = 112,
      description = 'O melhor FastFood',
      phone = '99999999999',
    )
    self.menu = mommy.make(Menu, description = 'Combos', restaurant = self.restaurant)
      
  def test_shopping_creation(self):
    self.assertTrue(isinstance(self.menu, Menu))
    self.assertEquals(self.menu.__str__(), self.menu.description)


class TestItemMenu(TestCase):
  def setUp(self):
    self.menu = mommy.make(Menu, description = 'Combos')
    self.item_menu = mommy.make(ItemMenu, 
      name = 'X-Salada',
      value = 20.50,
      description = 'Sanduiche muito gostoso', 
      preparation_time = '00:15:00',
      menu = self.menu
    )
      
  def test_shopping_creation(self):
    self.assertTrue(isinstance(self.item_menu, ItemMenu))
    self.assertEquals(self.item_menu.__str__(), self.item_menu.name)


class TestItemCategory(TestCase):
  def setUp(self):
    self.item_menu = mommy.make(ItemMenu, 
      name = 'X-Salada',
      value = 20.50,
      description = 'Sanduiche muito gostoso', 
      preparation_time = '00:15:00',
    )
    self.item_category = mommy.make(ItemCategory, 
      title = 'Escolha um molho',
      description = 'Escolha apenas 1 molho',
      required = True, 
      number_of_items = 1,
      item_menu = self.item_menu
    )
      
  def test_shopping_creation(self):
    self.assertTrue(isinstance(self.item_category, ItemCategory))
    self.assertEquals(self.item_category.__str__(), self.item_category.title)


class TestCategoryOption(TestCase):
  def setUp(self):
    self.item_category = mommy.make(ItemCategory, 
      title = 'Escolha um molho',
      description = 'Escolha apenas 1 molho',
      required = True, 
      number_of_items = 1,
    )
    self.category_option = mommy.make(CategoryOption, 
      title = 'Maionese',
      description = 'Maionese especial do BK',
      value = 1.00, 
      item_category = self.item_category,
    )
      
  def test_shopping_creation(self):
    self.assertTrue(isinstance(self.category_option, CategoryOption))
    self.assertEquals(self.category_option.__str__(), self.category_option.title)


