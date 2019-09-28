from rest_framework.serializers import ModelSerializer
import restaurant_service.api.models as model


class ShoppingSerializer(ModelSerializer):
  
  class Meta:
    model = model.Shopping
    fields = '__all__'


class OpeningHoursSerializer(ModelSerializer):
  
  class Meta:
    model = model.OpeningHours
    fields = '__all__'


class RestaurantCategorySerializer(ModelSerializer):
  
  class Meta:
    model = model.RestaurantCategory
    fields = '__all__'


class RestaurantSerializer(ModelSerializer):
  
  class Meta:
    model = model.Restaurant
    fields = '__all__'


class MenuSerializer(ModelSerializer):
  
  class Meta:
    model = model.Menu
    fields = '__all__'


class ItemMenuSerializer(ModelSerializer):
  
  class Meta:
    model = model.ItemMenu
    fields = '__all__'


class ItemCategorySerializer(ModelSerializer):
  
  class Meta:
    model = model.ItemCategory
    fields = '__all__'


class CategoryOptionSerializer(ModelSerializer):
  
  class Meta:
    model = model.CategoryOption
    fields = '__all__'
