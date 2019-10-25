from django.urls import path

from .views import (
    RestaurantView,
    post_or_get_shopping,
    shopping_by_pk,
    see_qrcode,
    post_or_get_item,
    item_by_pk,
    post_or_get_menu,
    menu_by_pk,
)

urlpatterns = [
    path('restaurant/', RestaurantView.handle_get_or_post, name="restaurant"),
    path('restaurant/<int:pk>/', RestaurantView.handle_get_by_pk, name="restaurant_by_pk"),
    path('shopping/<int:pk>', shopping_by_pk, name="shopping_by_pk"),
    path('shopping/', post_or_get_shopping, name="shopping"),
    path('qrcode/<int:pk>', see_qrcode, name="see_qrcode"),
    path('item/', post_or_get_item, name="item"),
    path('item/<int:pk>/', item_by_pk, name="item_by_pk"),
    path('menu/', post_or_get_menu, name="menu"),
    path('menu/<int:pk>/', menu_by_pk, name="menu_by_pk"),
]
