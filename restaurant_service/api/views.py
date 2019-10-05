from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import (
    Restaurant, Shopping,
)
from .serializers import(
    RestaurantSerializer, ShoppingSerializer,
)
import pyqrcode 
from pyqrcode import QRCode 


@api_view(['GET'])
def see_qrcode(request, pk):
    try:
        shopping = Shopping.objects.get(pk=pk)
    except Shopping.DoesNotExist:
        return HttpResponse(status=404)

    url = 'http://localhost:8001/'
    # String which represent the QR code
    s = "{url}shopping/" + str(pk)

    # Generate QR code
    url = pyqrcode.create(s)

    return JsonResponse(url.png_as_base64_str(scale = 10, background = '#efefef',module_color = '#ef596b'), safe=False)

@api_view(['POST', 'GET'])
def post_or_get_restaurant(request):
    """
    List all restaurant, or create a new restaurant.
    """

    if request.method == 'GET':
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RestaurantSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201, safe=False)
        return JsonResponse(serializer.errors, status=400, safe=False)



@api_view(['GET', 'PUT', 'DELETE'])
def restaurant_by_pk(request, pk):
    """
    Resquests by restaurant pk for consult detail, edit or delete.
    """

    try:
        restaurant = Restaurant.objects.get(pk=pk)
    except Restaurant.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = RestaurantSerializer(restaurant)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RestaurantSerializer(restaurant, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        restaurant.delete()
        return HttpResponse(status=204)

@api_view(['GET', 'POST'])
def post_or_get_shopping(request):
    """
    List all shoppings
    """

    if request.method == 'GET':
        shopping = Shopping.objects.all()
        serializer = ShoppingSerializer(shopping, many = True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ShoppingSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201, safe=False)
        return JsonResponse(serializer.errors, status=400, safe=False)

@api_view(['GET', 'PUT', 'DELETE'])
def shopping_by_pk(request, pk):
    """
    Resquests by restaurant pk for consult detail, edit or delete.
    """

    try:
        shopping = Shopping.objects.get(pk=pk)
    except Restaurant.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ShoppingSerializer(shopping)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ShoppingSerializer(shopping, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        shopping.delete()
        return HttpResponse(status=204)
