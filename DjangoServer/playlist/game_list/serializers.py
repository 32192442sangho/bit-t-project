from rest_framework import serializers
from models import GameList

class GameListSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameList
        fields = '__all__'