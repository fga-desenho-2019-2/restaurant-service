import json
from model_mommy import mommy
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from json import loads
from restaurant_service.api.models import RestaurantCategory


class RestaurantCategoryTests(APITestCase):
    def setUp(self):
        self.category = {'name' : 'Fast-food'}
        self.url_post = reverse('restaurant_category') # url "api/restaurant_category"


    def test_post_category(self):
        """
        Ensure we can create a new category object.
        """

        # test post with success
        response = self.client.post(self.url_post, self.category, format='json') 
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(RestaurantCategory.objects.count(), 1)
        self.assertEqual(RestaurantCategory.objects.get().name, 'Fast-food')
        

    def test_put_category(self):
        """
        Ensure we can put a category
        """
        
        response = self.client.post(self.url_post, self.category, format='json') 
        
        category = RestaurantCategory.objects.get(name="Fast-food") 
        pk = category.pk
        url_by_pk = reverse('restaurant_category_by_pk', args=[pk]) # url "api/restaurant_category/<int:pk>"

        # test put with success
        self.category['name'] = 'Massas'
        response = self.client.put(url_by_pk,  self.category, format='json') 
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(RestaurantCategory.objects.get(pk=pk).name, 'Massas')
    
    def test_delete_category(self):
        """
        Ensure we can delete a category
        """
        
        response = self.client.post(self.url_post, self.category, format='json') 

        category = RestaurantCategory.objects.get(name="Fast-food") 
        pk = category.pk
        url_by_pk = reverse('restaurant_category_by_pk', args=[pk]) # url "api/restaurant_category/<int:pk>"

        # test delete with success
        response = self.client.delete(url_by_pk,  self.category, format='json') 
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(RestaurantCategory.objects.count(), 0)

