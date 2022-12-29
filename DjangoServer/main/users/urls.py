from django.urls import re_path as url
from main.users import views

urlpatterns = [
    url(r'users', views.users)
]