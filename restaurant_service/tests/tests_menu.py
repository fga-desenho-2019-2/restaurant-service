import json
from model_mommy import mommy
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from json import loads
from restaurant_service.api.models import (
    Restaurant,
    Menu,
)


class MenuTests(APITestCase):
    def setUp(self):
        self.restaurant = mommy.make(Restaurant,
               cnpj = '13339532',
               name = 'Burger King',
               description = 'O melhor FastFood',
               note = 4.8,
               wait_time = '00:12:00'
        )

        self.menu = {
                'description' : 'Massas',
                'restaurant' : self.restaurant.pk
        }

        self.url_post = reverse('menu') # url "api/menu"

    def test_post_menu(self):
        """
        Ensure we can create a new menu object.
        """

        # test post with success
        response = self.client.post(self.url_post, self.menu, format='json') 
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Menu.objects.count(), 1)
        self.assertEqual(Menu.objects.get().description, 'Massas')
        

    def test_put_menu(self):
        """
        Ensure we can put a menu
        """
        
        response = self.client.post(self.url_post, self.menu, format='json') 

        menu = Menu.objects.get(description="Massas")
        pk = menu.pk
        url_by_pk = reverse('menu_by_pk', args=[pk]) # url "api/menu/<int:pk>"

        # test put with success
        self.menu['description'] = 'Sanduiches'
        response = self.client.put(url_by_pk,  self.menu, format='json') 
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Menu.objects.get(pk=pk).description, 'Sanduiches')
    
    def test_delete_menu(self):
        """
        Ensure we can delete a menu
        """
        
        response = self.client.post(self.url_post, self.menu, format='json') 

        menu = Menu.objects.get(description="Massas")
        pk = menu.pk
        url_by_pk = reverse('menu_by_pk', args=[pk]) # url "api/menu/<int:pk>"

        # test delete with success
        response = self.client.delete(url_by_pk,  self.menu, format='json') 
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Menu.objects.count(), 0)
