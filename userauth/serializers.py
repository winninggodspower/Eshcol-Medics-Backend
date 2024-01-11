from rest_framework.serializers import ModelSerializer
from django.contrib.auth.hashers import make_password
from .models import CustomUser

class UserRegisterSerializer(ModelSerializer):
    class Meta:
        model = CustomUser  
        fields = ['id', 'email', 'password',  'phone_number', 'is_expert']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

class UserLoginSerializer(ModelSerializer):
    class Meta:
        models = CustomUser


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['user_type'] = 'expert' if user.is_expert else 'patient' 
        # ...

        return token


