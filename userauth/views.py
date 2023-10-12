from django.shortcuts import render
from .serializers import UserRegisterSerializer
from rest_framework import generics
from .models import CustomUser
from rest_framework import validators

# Create your views here.


class CustomUserCreation(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegisterSerializer



