from django.urls import path
from .api_views import api_list_hats


urlPatterns = [
    path("hats/", api_list_hats, name="api_list_hats"),
]
