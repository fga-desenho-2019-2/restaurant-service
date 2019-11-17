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


class ImageRestaurantSerializer(ModelSerializer):
    image = Base64ImageField()

    class Meta:
        model = model.ImageRestaurant
        fields= ['image']

        def create(self, validated_data):
            image=validated_data.pop('image')
            return model.objects.create(image=image)


class RestaurantSerializer(ModelSerializer):
    image = ImageRestaurantSerializer(many=True)

    class Meta:
        model = model.Restaurant
        fields = '__all__'
    
    def create(self, validated_data): 
        imgs_data = validated_data.pop('image')
        restaurant = model.Restaurant.objects.create(**validated_data)
        for img in imgs_data:
            model.ImageRestaurant.objects.create(restaurant=restaurant, **img)
        return restaurant


class MenuSerializer(ModelSerializer):

    class Meta:
        model = model.Menu
        fields = '__all__'


class ComplementSerializer(ModelSerializer):

    class Meta:
        model = model.Complement
        fields = ['name', 'description', 'selected', 'value', 'qtd']


class ImageItemSerializer(ModelSerializer):
    image = Base64ImageField()

    class Meta:
        model = model.ImageItem
        fields= ['image']

        def create(self, validated_data):
            image=validated_data.pop('image')
            return model.objects.create(image=image)


class ItemSerializer(ModelSerializer):
    sidedish = ComplementSerializer(many=True)
    image = ImageItemSerializer(many=True)

    class Meta:
        model = model.Item
        fields = '__all__'
    
    def create(self, validated_data): 
        complements_data = validated_data.pop('sidedish')
        imgs_data = validated_data.pop('image')
        item = model.Item.objects.create(**validated_data)
        for complement in complements_data:
            model.Complement.objects.create(item=item, **complement)
        for img in imgs_data:
            model.ImageItem.objects.create(item=item, **img)
        return item


class ItemCategorySerializer(ModelSerializer):

    class Meta:
        model = model.ItemCategory
        fields = '__all__'


