from django.urls import path

from .views import post_or_get

urlpatterns = [
    path('restaurant/', post_or_get, name="restaurant"),
]
