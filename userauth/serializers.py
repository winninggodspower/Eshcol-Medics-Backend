from rest_framework.serializers import ModelSerializer
from django.contrib.auth.hashers import make_password
from .models import CustomUser

class UserRegisterSerializer(ModelSerializer):
    class Meta:
        model = CustomUser  
        fields = ['id', 'email', 'password', 'is_expert']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

class UserLoginSerializer(ModelSerializer):
    class Meta:
        models = CustomUser
    



