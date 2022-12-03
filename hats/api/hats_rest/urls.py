from django.urls import path
from .views import api_list_hats, api_show_hats

urlpatterns = [
    path("hats/", api_list_hats, name="api_list_hats"),
    path(
        "locations/<int:location_vo_id>/hats/",
        api_list_hats,
        name="api_list_hats",
    ),
    path("hats/<int:pk>/", api_show_hats, name="api_show_hats"),
]
