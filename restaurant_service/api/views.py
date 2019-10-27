from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from abc import ABC, abstractmethod
import pyqrcode 

from .models import (
    Restaurant, Shopping, Item, Menu,
    RestaurantCategory, ItemCategory, Complement
)
from .serializers import(
    RestaurantSerializer, ShoppingSerializer, 
    ComplementSerializer, ItemSerializer, MenuSerializer, 
    RestaurantCategorySerializer, ItemCategorySerializer
)

class TemplateClass(ABC):
    @abstractmethod
    def handle_get_or_post(request):
        pass
    
    @abstractmethod
    def handle_get_by_pk(request, pk):
        pass

    def get_all(model, serializer):
        """
        List all objects.
        """
        objects = model.objects.all()
        serializer = serializer(objects, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(request, serializer):
        """
        Create a new object.
        """
        data = JSONParser().parse(request)
        serializer = serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201, safe=False)
        return JsonResponse(serializer.errors, status=400, safe=False)

    def get_by_pk(model, serializer, pk):
        """
        Get one object.
        """
        try:
            obj = model.objects.get(pk=pk)
        except model.DoesNotExist:
            return HttpResponse(status=404)

        serializer = serializer(obj)
        return JsonResponse(serializer.data)
    
    def put(request, model, serializer, pk):
        """
        Edit one object.
        """
        try:
            obj = model.objects.get(pk=pk)
        except model.DoesNotExist:
            return HttpResponse(status=404)
        
        data = JSONParser().parse(request)
        serializer = serializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    def delete(model, serializer, pk):
        """
        Delete one object.
        """
        try:
            obj = model.objects.get(pk=pk)
        except model.DoesNotExist:
            return HttpResponse(status=404)

        obj.delete()
        return HttpResponse(status=204)

class RestaurantView(TemplateClass):
    @api_view(['GET', 'POST'])
    def handle_get_or_post(request):
        if request.method == 'GET':
            return TemplateClass.get_all(Restaurant, RestaurantSerializer)
        if request.method == 'POST':
            return TemplateClass.post(request, RestaurantSerializer)

    @api_view(['GET', 'PUT', 'DELETE'])
    def handle_get_by_pk(request, pk):
        if request.method == 'GET':
            return TemplateClass.get_by_pk(Restaurant, RestaurantSerializer, pk)

        elif request.method == 'PUT':
            return TemplateClass.put(request, Restaurant, RestaurantSerializer, pk)
        
        elif request.method == 'DELETE':
            return TemplateClass.delete(Restaurant, RestaurantSerializer, pk)

class ShoppingView(TemplateClass):
    @api_view(['GET', 'POST'])
    def handle_get_or_post(request):
        if request.method == 'GET':
            return TemplateClass.get_all(Shopping, ShoppingSerializer)
        if request.method == 'POST':
            return TemplateClass.post(request, ShoppingSerializer)

    @api_view(['GET', 'PUT', 'DELETE'])
    def handle_get_by_pk(request, pk):
        if request.method == 'GET':
            return TemplateClass.get_by_pk(Shopping, ShoppingSerializer, pk)

        elif request.method == 'PUT':
            return TemplateClass.put(request, Shopping, ShoppingSerializer, pk)
        
        elif request.method == 'DELETE':
            return TemplateClass.delete(Shopping, ShoppingSerializer, pk)

class ItemView(TemplateClass):
    @api_view(['GET', 'POST'])
    def handle_get_or_post(request):
        if request.method == 'GET':
            return TemplateClass.get_all(Item, ItemSerializer)
        if request.method == 'POST':
            return TemplateClass.post(request, ItemSerializer)

    @api_view(['GET', 'PUT', 'DELETE'])
    def handle_get_by_pk(request, pk):
        if request.method == 'GET':
            return TemplateClass.get_by_pk(Item, ItemSerializer, pk)

        elif request.method == 'PUT':
            return TemplateClass.put(request, Item, ItemSerializer, pk)
        
        elif request.method == 'DELETE':
            return TemplateClass.delete(Item, ItemSerializer, pk)

class MenuView(TemplateClass):
    @api_view(['GET', 'POST'])
    def handle_get_or_post(request):
        if request.method == 'GET':
            return TemplateClass.get_all(Menu, MenuSerializer)
        if request.method == 'POST':
            return TemplateClass.post(request, MenuSerializer)

    @api_view(['GET', 'PUT', 'DELETE'])
    def handle_get_by_pk(request, pk):
        if request.method == 'GET':
            return TemplateClass.get_by_pk(Menu, MenuSerializer, pk)

        elif request.method == 'PUT':
            return TemplateClass.put(request, Menu, MenuSerializer, pk)
        
        elif request.method == 'DELETE':
            return TemplateClass.delete(Menu, MenuSerializer, pk)

class ItemCategoryView(TemplateClass):
    @api_view(['GET', 'POST'])
    def handle_get_or_post(request):
        if request.method == 'GET':
            return TemplateClass.get_all(ItemCategory, ItemCategorySerializer)
        if request.method == 'POST':
            return TemplateClass.post(request, ItemCategorySerializer)

    @api_view(['GET', 'PUT', 'DELETE'])
    def handle_get_by_pk(request, pk):
        if request.method == 'GET':
            return TemplateClass.get_by_pk(ItemCategory, ItemCategorySerializer, pk)

        elif request.method == 'PUT':
            return TemplateClass.put(request, ItemCategory, ItemCategorySerializer, pk)
        
        elif request.method == 'DELETE':
            return TemplateClass.delete(ItemCategory, ItemCategorySerializer, pk)

class RestaurantCategoryView(TemplateClass):
    @api_view(['GET', 'POST'])
    def handle_get_or_post(request):
        if request.method == 'GET':
            return TemplateClass.get_all(RestaurantCategory, RestaurantCategorySerializer)
        if request.method == 'POST':
            return TemplateClass.post(request, RestaurantCategorySerializer)

    @api_view(['GET', 'PUT', 'DELETE'])
    def handle_get_by_pk(request, pk):
        if request.method == 'GET':
            return TemplateClass.get_by_pk(RestaurantCategory, RestaurantCategorySerializer, pk)

        elif request.method == 'PUT':
            return TemplateClass.put(request, RestaurantCategory, RestaurantCategorySerializer, pk)
        
        elif request.method == 'DELETE':
            return TemplateClass.delete(RestaurantCategory, RestaurantCategorySerializer, pk)

class ItemCategoryView(TemplateClass):
    @api_view(['GET', 'POST'])
    def handle_get_or_post(request):
        if request.method == 'GET':
            return TemplateClass.get_all(ItemCategory, ItemCategorySerializer)
        if request.method == 'POST':
            return TemplateClass.post(request, ItemCategorySerializer)

    @api_view(['GET', 'PUT', 'DELETE'])
    def handle_get_by_pk(request, pk):
        if request.method == 'GET':
            return TemplateClass.get_by_pk(ItemCategory, ItemCategorySerializer, pk)

        elif request.method == 'PUT':
            return TemplateClass.put(request, ItemCategory, ItemCategorySerializer, pk)
        
        elif request.method == 'DELETE':
            return TemplateClass.delete(ItemCategory, ItemCategorySerializer, pk)

class ComplementView(TemplateClass):
    @api_view(['GET', 'POST'])
    def handle_get_or_post(request):
        if request.method == 'GET':
            return TemplateClass.get_all(Complement, ComplementSerializer)
        if request.method == 'POST':
            return TemplateClass.post(request, ComplementSerializer)

    @api_view(['GET', 'PUT', 'DELETE'])
    def handle_get_by_pk(request, pk):
        if request.method == 'GET':
            return TemplateClass.get_by_pk(Complement, ComplementSerializer, pk)

        elif request.method == 'PUT':
            return TemplateClass.put(request, Complement, ComplementSerializer, pk)
        
        elif request.method == 'DELETE':
            return TemplateClass.delete(Complement, ComplementSerializer, pk)

@api_view(['GET'])
def see_qrcode(request, pk):
    try:
        Shopping.objects.get(pk=pk)
    except Shopping.DoesNotExist:
        return HttpResponse(status=404)

    url = 'http://localhost:8001/'
    # String which represent the QR code
    s = "{url}shopping/" + str(pk)

    # Generate QR code
    url = pyqrcode.create(s)

    qrString = {
        'qrcode': url.png_as_base64_str(scale = 10, background = '#efefef',module_color = '#ef596b')
    }

    return JsonResponse(qrString , safe=False)
