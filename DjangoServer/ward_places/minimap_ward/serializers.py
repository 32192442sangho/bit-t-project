from rest_framework import serializers
from models import MinimapWard

class MinimapWardSerializer(serializers.ModelSerializer):
    class Meta:
        model = MinimapWard
        fields = '__all__'