from django.shortcuts import render
from .serializers import UserRegisterSerializer
from rest_framework import generics
from .models import CustomUser
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class CustomUserCreation(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegisterSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def authentication_route(request):
    return Response({'details': "worked"})