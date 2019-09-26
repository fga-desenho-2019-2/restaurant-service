from rest_framework import serializers
import restaurant_service.models as model

class ShoppingSerializer(serializers.Serializer):
  cnpj = serializers.CharField()
  name = serializers.CharField()
  latitude = serializers.FloatField()
  longitude = serializers.FloatField()
  city = serializers.CharField()
  state = serializers.CharField()
  country = serializers.CharField()
  neighborhood = serializers.CharField()
  street = serializers.CharField()
  number = serializers.IntegerField()
  phone = serializers.CharField()


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
