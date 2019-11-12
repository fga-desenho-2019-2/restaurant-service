from django.urls import path
from django.conf.urls import url

from .views import (
    RestaurantView, ShoppingView, ItemView,
    MenuView, ItemCategoryView, RestaurantView,
    ComplementView, RestaurantCategoryView, see_qrcode
)
from .image_views import ImageRestaurantView, ImageItemView

urlpatterns = [
    path('restaurant', RestaurantView.handle_get_or_post, name="restaurant"),
    path('restaurant/<int:pk>', RestaurantView.handle_get_by_pk, name="restaurant_by_pk"),
    path('shopping', ShoppingView.handle_get_or_post, name="shopping"),
    path('shopping/<int:pk>', ShoppingView.handle_get_by_pk, name="shopping_by_pk"),
    path('item', ItemView.handle_get_or_post, name="item"),
    path('item/<int:pk>', ItemView.handle_get_by_pk, name="item_by_pk"),
    path('menu', MenuView.handle_get_or_post, name="menu"),
    path('menu/<int:pk>', MenuView.handle_get_by_pk, name="menu_by_pk"),
    path('item-category', ItemCategoryView.handle_get_or_post, name="item_category"),
    path('item-category/<int:pk>', ItemCategoryView.handle_get_by_pk, name="item_category_by_pk"),
    path('restaurant-category', RestaurantCategoryView.handle_get_or_post, name="restaurant_category"),
    path('restaurant-category/<int:pk>', RestaurantCategoryView.handle_get_by_pk, name="restaurant_category_by_pk"),
    path('complement', ComplementView.handle_get_or_post, name="complement"),
    path('complement/<int:pk>', ComplementView.handle_get_by_pk, name="complement_by_pk"),
    path('qrcode/<int:pk>', see_qrcode, name="see_qrcode"),
    path('restaurant-image', ImageRestaurantView.handle_get_or_post, name='restaurant_image'),
    path('restaurant-image-by-pk/<int:pk>', ImageRestaurantView.handle_get_by_pk, name='image_restaurant_by_pk'),
    path('restaurant-image/<int:pk_restaurant>', ImageRestaurantView.get_by_fk, name='image_by_restaurant'),
    path('item-image', ImageItemView.handle_get_or_post, name='item_image'),
    path('item-image-by-pk/<int:pk>', ImageItemView.handle_get_by_pk, name='image_item_by_pk'),
    path('item-image/<int:pk_item>', ImageItemView.get_by_fk, name='image_by_item')
]
