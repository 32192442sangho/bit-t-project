from django.urls import re_path as url
from ward_places.min_output import views

urlpatterns = [
    url(r'minoutput', views.min_output)
]