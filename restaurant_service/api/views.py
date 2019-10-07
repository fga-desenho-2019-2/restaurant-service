from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
import pyqrcode 

from .models import (
    Restaurant, Shopping, Item
)
from .serializers import(
    RestaurantSerializer, ShoppingSerializer,
    ItemSerializer, MenuSerializer
)

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

@api_view(['POST', 'GET'])
def post_or_get_item(request):
    """
    List all item, or create a new item.
    """

    if request.method == 'GET':
        itens = Item.objects.all()
        serializer = ItemSerializer(itens, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201, safe=False)
        return JsonResponse(serializer.errors, status=400, safe=False)

@api_view(['GET', 'PUT', 'DELETE'])
def item_by_pk(request, pk):
    """
    Resquests by item pk for consult detail, edit or delete.
    """

    try:
        item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ItemSerializer(item)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ItemSerializer(item, data=data)
        if serializer.is_valid():
            serializer.save()

    elif request.method == 'DELETE':
        item.delete()
        return HttpResponse(status=204)

@api_view(['POST', 'GET'])
def post_or_get_menu(request):
    """
    List all menu, or create a new menu.
    """

    if request.method == 'GET':
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MenuSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201, safe=False)
        return JsonResponse(serializer.errors, status=400, safe=False)

@api_view(['GET', 'PUT', 'DELETE'])
def menu_by_pk(request, pk):
    """
    Resquests by menu pk for consult detail, edit or delete.
    """

    try:
        menu = Menu.objects.get(pk=pk)
    except Menu.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MenuSerializer(menu)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MenuSerializer(menu, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        menu.delete()
        return HttpResponse(status=204)

