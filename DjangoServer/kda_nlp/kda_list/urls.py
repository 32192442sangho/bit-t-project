from django.urls import re_path as url
from kda_nlp.kda_list import views

urlpatterns = [
    url(r'kdaList', views.kda_list)
]