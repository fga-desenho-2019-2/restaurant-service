from django.urls import path

from .views import (
    post_or_get_restaurant,
    restaurant_by_pk,
)

urlpatterns = [
    path('restaurant/', post_or_get_restaurant, name="restaurant"),
    path('restaurant/<int:pk>/', restaurant_by_pk, name="restaurant_by_pk"),
]
