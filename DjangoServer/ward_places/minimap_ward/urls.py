from django.urls import re_path as url
from ward_places.minimap_ward import views

urlpatterns = [
    url(r'minimapward', views.minimap_ward)
]