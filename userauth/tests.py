from django.test import TestCase
from rest_framework.test import APITestCase
from .models import CustomUser

# Create your tests here.
class AuthenticationAPITest(APITestCase):
    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        self.user = CustomUser.objects.create_user(**self.user_data)


    def tearDown(self):
        self.user.delete()
