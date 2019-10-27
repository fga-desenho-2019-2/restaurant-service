import json
from model_mommy import mommy
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from json import loads
from restaurant_service.api.models import (
    Menu,
    Item,
    ItemCategory,
)


class ItemTests(APITestCase):
    def setUp(self):
        self.category = mommy.make(ItemCategory,
            title = "Bebidas",
            description = 'Acompanhamentos líquidos',
            required = True,
            number_of_items = 11
        )
        self.menu = mommy.make(Menu,
            description = "Massas"
        )
        self.item = {
               'name' : 'Macarrão',
               'value' : 12.00,
               'description'  : 'Espaguete',
               'category' : self.category.pk,
               'preparation_time' : '00:45:00',
               'menu': self.menu.pk
        }

        self.url_post = reverse('item') # url "api/item"

    def test_post_item(self):
        """
        Ensure we can create a new item object.
        """

        # test post with success
        response = self.client.post(self.url_post, self.item, format='json') 
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Item.objects.count(), 1)
        self.assertEqual(Item.objects.get().name, 'Macarrão')
        

    def test_put_item(self):
        """
        Ensure we can put a item
        """
        
        response = self.client.post(self.url_post, self.item, format='json') 

        item = Item.objects.get(name="Macarrão")
        pk = item.pk
        url_by_pk = reverse('item_by_pk', args=[pk]) # url "api/item/<int:pk>"

        # test put with success
        self.item['name'] = 'Pizza'
        response = self.client.put(url_by_pk,  self.item, format='json') 
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Item.objects.get(pk=pk).name, 'Pizza')
    
    def test_delete_item(self):
        """
        Ensure we can delete a item
        """
        
        response = self.client.post(self.url_post, self.item, format='json') 
        
        item = Item.objects.get(name="Macarrão")
        pk = item.pk
        url_by_pk = reverse('item_by_pk', args=[pk]) # url "api/item/<int:pk>"

        # test delete with success
        response = self.client.delete(url_by_pk,  self.item, format='json') 
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Item.objects.count(), 0)

