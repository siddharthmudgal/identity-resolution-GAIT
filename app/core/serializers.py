from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """serializer that serializes the main user class"""
    class Meta:
        model = User
        fields = ('userid', 'sensordata_x', 'sensordata_y', 'sensordata_z')


class ResultSerializer(serializers.Serializer):
    """serializer to send back the result of authentication"""
    corr_result = serializers.CharField(max_length=255)
