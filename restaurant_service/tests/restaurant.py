import json
from model_mommy import mommy
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from json import loads
from restaurant_service.api.models import (
    Shopping,
    RestaurantCategory,
    Restaurant,
)

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
        )
        self.category = mommy.make(RestaurantCategory, name = 'Fast-food' )
        self.restaurant = {
               'cnpj' : '13339532',
               'name' : 'Burger King',
               'description'  : 'O melhor FastFood',
               'shopping' : self.shopping.pk,
               'category' : self.category.pk,
               'note': 4.8,
               'wait_time': '00:12:00'
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
    
    def test_delete_restaurant(self):
        """
        Ensure we can delete a restaurant
        """
        
        response = self.client.post(self.url_post, self.restaurant, format='json') 

        # test delete with success
        response = self.client.delete(self.url_by_pk,  self.restaurant, format='json') 
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Restaurant.objects.count(), 0)

