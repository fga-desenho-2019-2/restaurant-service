from django.db import models

# Create your models here.
class Shopping(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  cnpj = models.CharField(primary_key=True, max_length=16)
  name = models.CharField(max_length=100)
  latitude = models.FloatField()
  longitude = models.FloatField()
  city = models.CharField(max_length=100)
  state = models.CharField(max_length=30)
  country = models.CharField(max_length=50)
  neighborhood = models.CharField(max_length=50)
  street = models.CharField(max_length=50)
  number = models.IntegerField()
  phone = models.CharField(max_length=11)
  
  class Meta:
    ordering = ['created']
    verbose_name = u'Shopping'
    verbose_name_plural = u'Shoppings'

  def __str__(self):
    return self.name


class OpeningHours(models.Model):
  day = models.CharField(max_length=50)
  start_time = models.TimeField()
  end_time = models.TimeField()

  class Meta:
    verbose_name = u'OpeningHours'
    verbose_name_plural = u'OpeningHours'
    

class RestaurantCategory(models.Model):
  name = models.CharField(max_length=60)

  class Meta:
    verbose_name = u'RestaurantCategory'
    verbose_name_plural = u'RestaurantCategories'

  def __str__(self):
    return self.name


class Restaurant(models.Model):
  cnpj = models.CharField(primary_key=True, max_length=16)
  name = models.CharField(max_length=100)
  number = models.IntegerField()
  description = models.CharField(max_length=200)
  phone = models.CharField(max_length=11)
  shopping = models.ForeignKey(
    Shopping, 
    on_delete=models.CASCADE,
    related_name="restaurants"
  )
  category = models.ForeignKey(
    RestaurantCategory, 
    on_delete=models.CASCADE,
    related_name="restaurants"
  )
  opening_hours = models.ManyToManyField(OpeningHours)

  class Meta:
    verbose_name = u'Restaurant'
    verbose_name_plural = u'Restaurants'

  def __str__(self):
    return self.name

  
class Menu(models.Model):
  description = models.CharField(max_length=200)
  restaurant = models.ForeignKey(
    Restaurant, 
    on_delete=models.CASCADE,
    related_name="menus"
  )

  class Meta:
    verbose_name = u'Menu'
    verbose_name_plural = u'Menus'

  def __str__(self):
    return self.description


class ItemMenu(models.Model):
  name = models.CharField(max_length=50)
  value = models.FloatField()
  description = models.CharField(max_length=200)
  preparation_time = models.DurationField()
  menu = models.ForeignKey(
    Menu, 
    on_delete=models.CASCADE,
    related_name="item_menu"
  )

  class Meta:
    verbose_name = u'Item menu'
    verbose_name_plural = u'Items menu'

  def __str__(self):
    return self.name


class ItemCategory(models.Model):
  title = models.CharField(max_length=50)
  description = models.CharField(max_length=200)
  required = models.BooleanField()
  number_of_items = models.IntegerField()
  item_menu = models.ForeignKey(
    ItemMenu, 
    on_delete=models.CASCADE,
    related_name="item_category"
  )

  class Meta:
    verbose_name = u'Item category'
    verbose_name_plural = u'Items category'

  def __str__(self):
    return self.title


class CategoryOption(models.Model):
  title = models.CharField(max_length=50)
  description = models.CharField(max_length=200)
  value = models.FloatField(blank=True)
  item_category = models.ForeignKey(
    ItemCategory, 
    on_delete=models.CASCADE,
    related_name="category_option"
  )

  class Meta:
    verbose_name = u'Category option'
    verbose_name_plural = u'Category options'

  def __str__(self):
    return self.title