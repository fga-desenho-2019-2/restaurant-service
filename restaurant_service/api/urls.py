from django.urls import path
from django.conf.urls import url

from .views import (
    RestaurantView, ShoppingView, ItemView,
    MenuView, ItemCategoryView, RestaurantView,
    ComplementView, RestaurantCategoryView, see_qrcode
)
from .views_images import ImageRestaurantView, ImageRestaurantDetail

urlpatterns = [
    path('restaurant/', RestaurantView.handle_get_or_post, name="restaurant"),
    path('restaurant/<int:pk>', RestaurantView.handle_get_by_pk, name="restaurant_by_pk"),
    path('shopping/', ShoppingView.handle_get_or_post, name="shopping"),
    path('shopping/<int:pk>', ShoppingView.handle_get_by_pk, name="shopping_by_pk"),
    path('item/', ItemView.handle_get_or_post, name="item"),
    path('item/<int:pk>', ItemView.handle_get_by_pk, name="item_by_pk"),
    path('menu/', MenuView.handle_get_or_post, name="menu"),
    path('menu/<int:pk>', MenuView.handle_get_by_pk, name="menu_by_pk"),
    path('item_category/', ItemCategoryView.handle_get_or_post, name="item_category"),
    path('item_category/<int:pk>', ItemCategoryView.handle_get_by_pk, name="item_category_by_pk"),
    path('restaurant_category/', RestaurantCategoryView.handle_get_or_post, name="restaurant_category"),
    path('restaurant_category/<int:pk>', RestaurantCategoryView.handle_get_by_pk, name="restaurant_category_by_pk"),
    path('complement/', ComplementView.handle_get_or_post, name="complement"),
    path('complement/<int:pk>', ComplementView.handle_get_by_pk, name="complement_by_pk"),
    path('qrcode/<int:pk>', see_qrcode, name="see_qrcode"),
    url(r'^image_restaurant/$', ImageRestaurantView.as_view(), name='image-restaurant'),
    path('image_restaurant_detail/<int:pk>', ImageRestaurantDetail.as_view(), name='image-restaurant-detail')
]
