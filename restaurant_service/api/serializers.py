from rest_framework.serializers import ModelSerializer
from rest_framework.fields import ImageField
from drf_extra_fields.fields import Base64ImageField

import restaurant_service.api.models as model

class ShoppingSerializer(ModelSerializer):

    class Meta:
        model = model.Shopping
        fields = '__all__'


#class OpeningHoursSerializer(ModelSerializer):
#  
#  class Meta:
#    model = model.OpeningHours
#    fields = '__all__'


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


class ItemSerializer(ModelSerializer):

    class Meta:
        model = model.Item
        fields = '__all__'


class ItemCategorySerializer(ModelSerializer):

    class Meta:
        model = model.ItemCategory
        fields = '__all__'


class ComplementSerializer(ModelSerializer):

    class Meta:
        model = model.Complement
        fields = '__all__'

class ImageRestaurantSerializer(ModelSerializer):
    image = Base64ImageField()

    class Meta:
        model = model.ImageRestaurant
        fields= ('restaurant', 'image')

        def create(self, validated_data):
            image=validated_data.pop('image')
            restaurant=validated_data.pop('restaurant')
            return model.objects.create(restaurant=restaurant,image=image)


class ImageItemSerializer(ModelSerializer):
    image = Base64ImageField()

    class Meta:
        model = model.ImageItem
        fields= ('item', 'image')

        def create(self, validated_data):
            image=validated_data.pop('image')
            item=validated_data.pop('item')
            return model.objects.create(item=item,image=image)
