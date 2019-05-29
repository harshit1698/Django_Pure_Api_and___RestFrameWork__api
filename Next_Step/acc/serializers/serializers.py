from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

User = get_user_model()


class UserSerializer(ModelSerializer):
    class Meta:
        password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
        model = User
        fileds = ['username','email','password']

