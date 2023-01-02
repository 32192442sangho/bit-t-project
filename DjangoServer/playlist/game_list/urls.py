from django.urls import re_path as url
from playlist.game_list import views

urlpatterns = [
    url(r'playlist', views.game_list)
]