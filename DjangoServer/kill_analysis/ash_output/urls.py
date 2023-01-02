from django.urls import re_path as url
from kill_analysis.ash_output import views

urlpatterns = [
    url(r'ashoutput', views.ash_output)
]