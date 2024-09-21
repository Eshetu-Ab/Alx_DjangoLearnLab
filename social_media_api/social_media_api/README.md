Social Media API
This project sets up the foundational elements of a social media API, including environment setup, user registration, and token-based authentication using Django and Django REST Framework (DRF).

Setup Process
1. Install Dependencies
Make sure to install Django and Django REST Framework:

bash
Copy code
pip install django djangorestframework
2. Create a Django Project
Create a new Django project named social_media_api:

bash
Copy code
django-admin startproject social_media_api
cd social_media_api
3. Create the accounts App
Create a new Django app named accounts for user-related functionalities:

bash
Copy code
python manage.py startapp accounts
4. Update INSTALLED_APPS
In social_media_api/settings.py, add rest_framework, rest_framework.authtoken, and accounts to INSTALLED_APPS:

python
Copy code
INSTALLED_APPS = [
    ...,
    'rest_framework',
    'rest_framework.authtoken',
    'accounts',
]
5. Apply Migrations
Run the migrations to set up your database schema:

bash
Copy code
python manage.py migrate
User Registration and Authentication
Custom User Model
The project uses a custom user model (CustomUser) that extends Django’s default AbstractUser. This model includes additional fields like bio, profile_picture, and followers (a self-referential many-to-many field).

accounts/models.py:
python
Copy code
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)

    def __str__(self):
        return self.username
Update settings.py to use this custom user model:

python
Copy code
AUTH_USER_MODEL = 'accounts.CustomUser'
User Registration
Users can register by providing a username and password. Optional fields include bio and profile_picture.

accounts/serializers.py:
python
Copy code
from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'password', 'bio', 'profile_picture', 'followers')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user
accounts/views.py:
python
Copy code
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from django.contrib.auth import get_user_model

class RegisterView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
User Login and Token Authentication
Token-based authentication allows users to log in and receive an authentication token.

Token Authentication
Add token authentication by including rest_framework.authtoken in INSTALLED_APPS and creating the login route in accounts/urls.py.

accounts/urls.py:
python
Copy code
from django.urls import path
from .views import RegisterView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),
]
Testing the API
1. Run the Development Server
bash
Copy code
python manage.py runserver
2. Test Registration
Use a tool like Postman or curl to send a POST request to /accounts/register/ with the following body:

json
Copy code
{
    "username": "testuser",
    "password": "password123"
}
3. Test Login
Send a POST request to /accounts/login/ with the following body:

json
Copy code
{
    "username": "testuser",
    "password": "password123"
}
A token will be returned upon successful login.

Overview of the User Model
The CustomUser model extends Django’s AbstractUser and adds the following fields:

bio: A text field where users can write a biography.
profile_picture: An optional image field for the user's profile picture.
followers: A self-referential many-to-many field to allow users to follow other users.