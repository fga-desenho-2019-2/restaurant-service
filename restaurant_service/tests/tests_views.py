import json
from model_mommy import mommy
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from json import loads
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


class QRCodeTest(APITestCase):
    def setUp(self):
        self.shopping = {
            'cnpj' : 12345678,
            'name' : 'Shopping Mauá',
            'city' : 'Mauá City',
            'state' : 'Tocantis',
            'country' : 'Brasil',
            'neighborhood' : 'Bairro das Castanheiras',
            'cep' : '7222323',
            'number' : 10,
            'phone' : '99999999999'
        }

        self.pk = 12345678
        self.url_post = reverse('shopping') # url "api/shopping"
        self.url_qrcode = reverse('see_qrcode', args = [self.pk])

    def test_get_qrcode(self):

        base64Code = "iVBORw0KGgoAAAANSUhEUgAAAXIAAAFyAQMAAADS6sNKAAAABlBMVEXvWWvv7+/QvEp3AAAAAnRSTlP//8i138cAAAGtSURBVHic7dlBjoMwDAVQSxyAI+XqHKkHQMoE299JUUeakbr56GdBS3jpBscY1/q/xmHy8vLy8vLyX/KWYxsz+zht/YxTay9ca/K83k/6a8N9H2qsHIsa5uSp/XXb/Zorj4xruc9lZMg/wo8vY+aMeIhF8o/xnsrlH+f9w3O3p/IKisrx8sw+BxL4esA1eV4/h1+KeDhql88hT+qvXd4jqdc3T+rvi+Q5/fWWnIfa+bb7D316XsuzeW+FGJ7Nk7ZZmcnz+jjZz0jl96Jbntyj7WHV4DrR7+rzN+SJ/TUV+TwTeJ/vU8c9n8uT+QyFOvgctn/+pDyvj1bmkrtPQ5Xtc/Lcvv6AWIru9IiMLk/rZyh4UkeV3bFcntvnfjeMJalf+dwXyfP6udXR78KrchVl7/0QeS4f704VFPVSdQsPeVJfw+rJvWz6VuWZPKVHHs9tjX5mRgZ2vjyt95vda5e3hdZVeWIPgAYIntJm60p5dh+5e/YzlxpN/hG+7v0sun/pb8vzeICe/xxjtJ712C0e5Kl8Di+1DbV1bPXtc/9Tnsj/ecjLy8vLy8t/wf8A/ZmjxS8QvUYAAAAASUVORK5CYII="
        response = self.client.post(self.url_post, self.shopping, format='json')
        response = self.client.get(self.url_qrcode)

        data = json.loads(response.content)

        self.assertEqual(data['qrcode'], base64Code)
        self.assertEqual(response.status_code, 200)

class RestaurantTests(APITestCase):
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
        self.restaurant = {
               'cnpj' : '13339532',
               'name' : 'Burger King',
               'store_number': 112,
               'description'  : 'O melhor FastFood',
               'phone' : '99999999999',
               'shopping' : self.shopping.pk,
               'category' : self.category.pk,
               'opening_hours' : [self.opening_hours_monday.pk, self.opening_hours_thuesday.pk]
        }

        self.pk = 13339532
        self.url_post = reverse('restaurant') # url "api/restaurant"
        self.url_by_pk = reverse('restaurant_by_pk', args=[self.pk]) # url "api/restaurant/<int:pk>"


    def test_post_restaurant(self):
        """
        Ensure we can create a new restaurant object.
        """

        # test post with success
        response = self.client.post(self.url_post, self.restaurant, format='json') 
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Restaurant.objects.count(), 1)
        self.assertEqual(Restaurant.objects.get().name, 'Burger King')
        

    def test_put_restaurant(self):
        """
        Ensure we can put a restaurant
        """
        
        response = self.client.post(self.url_post, self.restaurant, format='json') 

        # test put with success
        self.restaurant['name'] = 'Mack Donalds'
        response = self.client.put(self.url_by_pk,  self.restaurant, format='json') 
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Restaurant.objects.get(pk=self.pk).name, 'Mack Donalds')
    
    def test_delete_shopping(self):
        """
        Ensure we can delete a restaurant
        """
        
        response = self.client.post(self.url_post, self.restaurant, format='json') 

        # test delete with success
        response = self.client.delete(self.url_by_pk,  self.restaurant, format='json') 
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Restaurant.objects.count(), 0)

class ShopppingTests(APITestCase):
    def setUp(self):
        self.shopping = {
            'cnpj' : 13339532,
            'name' : 'Shopping Mauá',
            'city' : 'Mauá City',
            'state' : 'Tocantis',
            'country' : 'Brasil',
            'neighborhood' : 'Bairro das Castanheiras',
            'cep' : '7222323',
            'number' : 10,
            'phone' : '99999999999'
        }

        self.pk = 13339532
        self.url_post = reverse('shopping') # url "api/shopping"
        self.url_by_pk = reverse('shopping_by_pk', args=[self.pk]) # url "api/shopping/<int:pk>"


    def test_post_shopping(self):
        """
        Ensure we can create a new shopping object.
        """

        # test post with success
        response = self.client.post(self.url_post, self.shopping, format='json') 
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Shopping.objects.count(), 1)
        self.assertEqual(Shopping.objects.get().name, 'Shopping Mauá')
        

    def test_put_shopping(self):
        """
        Ensure we can put a shopping
        """
        
        response = self.client.post(self.url_post, self.shopping, format='json') 

        # test put with success
        self.shopping['name'] = 'Park Shopping'
        response = self.client.put(self.url_by_pk,  self.shopping, format='json') 
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Shopping.objects.get(pk=self.pk).name, 'Park Shopping')
    
    def test_delete_shopping(self):
        """
        Ensure we can delete a shopping
        """
        
        response = self.client.post(self.url_post, self.shopping, format='json') 

        # test delete with success
        response = self.client.delete(self.url_by_pk,  self.shopping, format='json') 
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Shopping.objects.count(), 0)


