from rest_framework import serializers
from models import AshOutput

class AshOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = AshOutput
        fields = '__all__'