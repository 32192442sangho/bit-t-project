from rest_framework import serializers
from models import MinOutput

class MinOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = MinOutput
        fields = '__all__'