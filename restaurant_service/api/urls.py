from django.urls import path

from .views import (
    RestaurantView,
    ShoppingView,
    ItemView,
    MenuView,
    see_qrcode,
)

urlpatterns = [
    path('restaurant/', RestaurantView.handle_get_or_post, name="restaurant"),
    path('restaurant/<int:pk>', RestaurantView.handle_get_by_pk, name="restaurant_by_pk"),
    path('shopping/', ShoppingView.handle_get_or_post, name="shopping"),
    path('shopping/<int:pk>', ShoppingView.handle_get_by_pk, name="shopping_by_pk"),
    path('item/', ItemView.handle_get_or_post, name="item"),
    path('item/<int:pk>', ItemView.handle_get_by_pk, name="item_by_pk"),
    path('menu/', MenuView.handle_get_or_post, name="menu"),
    path('menu/<int:pk>', MenuView.handle_get_by_pk, name="menu_by_pk"),
    path('qrcode/<int:pk>', see_qrcode, name="see_qrcode"),
]
