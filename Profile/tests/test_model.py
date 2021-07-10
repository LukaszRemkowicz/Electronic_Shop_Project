from django.test import TestCase
from django.contrib.auth import get_user_model

from ..models import Profile

class TestModel(TestCase):
    """ test user model """
    
    def setUp(self) -> None:
        self.payload = {'username': 'test60',
                   'password': 'TestPass123!',
                   'email': 'jan@test60.pl',
                   }
    
    def test_user_creation(self) -> None:
        
        user = get_user_model().objects.create_user(**self.payload)
        
        self.assertEqual(user.email, self.payload['email'])
        self.assertTrue(user.check_password(self.payload['password']))
        
    
    def test_check_signal(self) -> None:
        """ test if profile is created """
        
        user = get_user_model().objects.create_user(**self.payload)
        profile = Profile.objects.get(user=user)
        
        self.assertEqual(str(profile), self.payload['username'])