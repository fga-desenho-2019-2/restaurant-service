from django.urls import path

from .views import (
    post_or_get_restaurant,
    restaurant_by_pk,
    post_or_get_shopping,
    shopping_by_pk,
    see_qrcode
)

urlpatterns = [
    path('restaurant/', post_or_get_restaurant, name="restaurant"),
    path('restaurant/<int:pk>/', restaurant_by_pk, name="restaurant_by_pk"),
    path('shopping/<int:pk>', shopping_by_pk, name="shopping_by_pk"),
    path('shopping/', post_or_get_shopping, name="shopping"),
    path('qrcode/<int:pk>', see_qrcode, name="see_qrcode"),
]
