from rest_framework import serializers
from models import KdaList

class KdaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = KdaList
        fields = '__all__'