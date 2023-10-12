from django.urls import path
from .views import CustomUserCreation

urlpatterns = [
    path('register/', CustomUserCreation.as_view(), name='user-create')
]
