from rest_framework import serializers
from .models import CustomUser  # Ensure this points to your custom user model
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser  # Use your CustomUser model
        fields = ('username', 'email', 'password', 'bio', 'profile_picture')  # Add bio and profile_picture if needed

    def create(self, validated_data):
        # Create a user
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),  # Optional bio
            profile_picture=validated_data.get('profile_picture')  # Optional profile picture
        )
        # Create a token for the new user
        Token.objects.create(user=user)
        return user




