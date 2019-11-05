import json
from model_mommy import mommy
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from json import loads
from restaurant_service.api.models import Complement, ItemCategory


class ComplementTests(APITestCase):
    def setUp(self):
        self.item_category = mommy.make(ItemCategory,
              title = "Bebidas",
              description = 'Acompanhamentos líquidos',
              required = True,
              number_of_items = 11
        )
        self.complement = {
                'title' : 'Bebida',
                'description': 'Escolha uma bebida',
                'value' : 2.00,
                'number_of_items' : 3,
                'item_category': self.item_category.pk
        }
        self.url_post = reverse('complement') # url "api/complement"


    def test_post_complement(self):
        """
        Ensure we can create a new complement object.
        """

        # test post with success
        response = self.client.post(self.url_post, self.complement, format='json') 
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Complement.objects.count(), 1)
        self.assertEqual(Complement.objects.get().title, 'Bebida')
        

    def test_put_complement(self):
        """
        Ensure we can put a complement
        """
        
        response = self.client.post(self.url_post, self.complement, format='json') 
        
        complement = Complement.objects.get(title="Bebida") 
        pk = complement.pk
        url_by_pk = reverse('complement_by_pk', args=[pk]) # url "api/complement/<int:pk>"

        # test put with success
        self.complement['title'] = 'Molho'
        response = self.client.put(url_by_pk,  self.complement, format='json') 
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Complement.objects.get(pk=pk).title, 'Molho')
    
    def test_delete_complement(self):
        """
        Ensure we can delete a complement
        """
        
        response = self.client.post(self.url_post, self.complement, format='json') 

        complement = Complement.objects.get(title="Bebida") 
        pk = complement.pk
        url_by_pk = reverse('complement_by_pk', args=[pk]) # url "api/complement/<int:pk>"

        # test delete with success
        response = self.client.delete(url_by_pk,  self.complement, format='json') 
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Complement.objects.count(), 0)

