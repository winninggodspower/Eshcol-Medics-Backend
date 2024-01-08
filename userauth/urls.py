from django.urls import path
from .views import CustomUserCreation, authentication_route

urlpatterns = [
    path('register/', CustomUserCreation.as_view(), name='user-create'),
    path('authentication-route/', authentication_route, name='auth-route')
]
