from django.db import models

class Shopping(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  cnpj = models.CharField(primary_key=True, max_length=16)
  name = models.CharField(max_length=100)
  city = models.CharField(max_length=100)
  state = models.CharField(max_length=30)
  country = models.CharField(max_length=50)
  neighborhood = models.CharField(max_length=50, blank=True)
  cep = models.CharField(max_length=8)
  number = models.IntegerField()
  phone = models.CharField(max_length=12)
#  identification = models.IntegerField(primary_key=True)
  
  class Meta:
    ordering = ['created']
    verbose_name = u'Shopping'
    verbose_name_plural = u'Shoppings'

  def __str__(self):
    return self.name

#class OpeningHours(models.Model):
#  day = models.CharField(max_length=50)
#  start_time = models.TimeField()
#  end_time = models.TimeField()
#
#  class Meta:
#    verbose_name = u'OpeningHours'
#    verbose_name_plural = u'OpeningHours'
#    

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
  corporate_name = models.CharField(max_length=100, default=name)
  store_number = models.IntegerField()
  description = models.CharField(max_length=200, blank=True)
  phone = models.CharField(max_length=12)
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
  #opening_hours = models.ManyToManyField(OpeningHours)

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


class ItemCategory(models.Model):
  title = models.CharField(max_length=50)
  description = models.CharField(max_length=200, blank=True)
  required = models.BooleanField()
  number_of_items = models.IntegerField()
  
  class Meta:
    verbose_name = u'Item category'
    verbose_name_plural = u'Items categorys'

  def __str__(self):
    return self.title


class Item(models.Model):
  name = models.CharField(max_length=50)
  value = models.FloatField()
  description = models.CharField(max_length=200, blank=True)
  preparation_time = models.DurationField(blank=True)
  menu = models.ForeignKey(
    Menu, 
    on_delete=models.CASCADE,
    related_name="items"
  )
  category = models.ForeignKey(
    ItemCategory, 
    on_delete=models.CASCADE,
    related_name="items"
  )

  class Meta:
    verbose_name = u'Item'
    verbose_name_plural = u'Items'

  def __str__(self):
    return self.name


class Complement(models.Model):
  title = models.CharField(max_length=50)
  description = models.CharField(max_length=200)
  value = models.FloatField(blank=True)
  item_category = models.ForeignKey(
    ItemCategory,
    on_delete=models.CASCADE,
    related_name="complement_category"
  )

  class Meta:
    verbose_name = u'Complement category'
    verbose_name_plural = u'Complements categorys'

  def __str__(self):
    return self.title

class ImageRestaurant(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(upload_to='restaurant_images', max_length=255)

class ImageItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(upload_to='item_images', max_length=255)

