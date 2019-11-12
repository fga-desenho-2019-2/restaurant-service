from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from abc import ABC, abstractmethod

from .models import ImageRestaurant, ImageItem
from .serializers import ImageRestaurantSerializer, ImageItemSerializer

class TemplateClass(ABC):
    @abstractmethod
    def handle_get_or_post(request):
        pass
    
    @abstractmethod
    def handle_get_by_pk(request, pk):
        pass

    @abstractmethod
    def get_by_fk(request, fk):
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

class ImageRestaurantView(TemplateClass):
    @api_view(['GET', 'POST'])
    def handle_get_or_post(request):
        if request.method == 'GET':
            return TemplateClass.get_all(ImageRestaurant, ImageRestaurantSerializer)
        if request.method == 'POST':
            return TemplateClass.post(request, ImageRestaurantSerializer)

    @api_view(['GET', 'PUT', 'DELETE'])
    def handle_get_by_pk(request, pk):
        if request.method == 'GET':
            return TemplateClass.get_by_pk(ImageRestaurant, ImageRestaurantSerializer, pk)

        elif request.method == 'PUT':
            return TemplateClass.put(request, ImageRestaurant, ImageRestaurantSerializer, pk)
        
        elif request.method == 'DELETE':
            return TemplateClass.delete(ImageRestaurant, ImageRestaurantSerializer, pk)
    
    @api_view(['GET'])
    def get_by_fk(request, pk_restaurant):
        """
        Get one image by restaurant.
        """
        try:
            obj = ImageRestaurant.objects.get(restaurant=pk_restaurant)
        except ImageRestaurant.DoesNotExist:
            return HttpResponse(status=404)

        return HttpResponse(obj.image, content_type="image/png")

class ImageItemView(TemplateClass):
    @api_view(['GET', 'POST'])
    def handle_get_or_post(request):
        if request.method == 'GET':
            return TemplateClass.get_all(ImageItem, ImageItemSerializer)
        if request.method == 'POST':
            return TemplateClass.post(request, ImageItemSerializer)

    @api_view(['GET', 'PUT', 'DELETE'])
    def handle_get_by_pk(request, pk):
        if request.method == 'GET':
            return TemplateClass.get_by_pk(ImageItem, ImageItemSerializer, pk)

        elif request.method == 'PUT':
            return TemplateClass.put(request, ImageItem, ImageItemSerializer, pk)
        
        elif request.method == 'DELETE':
            return TemplateClass.delete(ImageItem, ImageItemSerializer, pk)

    @api_view(['GET'])
    def get_by_fk(request, pk_item):
        """
        Get one image by item.
        """
        try:
            obj = ImageItem.objects.get(item=pk_item)
        except ImageItem.DoesNotExist:
            return HttpResponse(status=404)

        return HttpResponse(obj.image, content_type="image/png")
