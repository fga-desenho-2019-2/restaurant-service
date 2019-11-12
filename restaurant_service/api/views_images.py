from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from .models import ImageRestaurant, ImageItem
from .serializers import ImageRestaurantSerializer, ImageItemSerializer

class ImageRestaurantView(APIView):
    def get(self, request, format=None):
        image = ImageRestaurant.objects.all()
        serializer = ImageRestaurantSerializer(image, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = ImageRestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def pre_save(self, obj):
        obj.owner = self.request.user


class ImageRestaurantDetail(APIView):
    def get_object(self, pk):
        try:
            return ImageRestaurant.objects.get(pk=pk)
        except ImageRestaurant.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        image = self.get_object(pk)
        serializer = ImageRestaurantSerializer(image)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        image = self.get_object(pk)
        serializer = ImageRestaurantSerializer(data=request.POST, files=request.FILES)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        image = self.get_object(pk)
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def pre_save(self, obj):
        obj.owner = self.request.user
