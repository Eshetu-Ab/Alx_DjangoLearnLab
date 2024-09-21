from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User





class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()  # Dynamically get the User model
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = get_user_model().objects.create_user(  # Create a user
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


