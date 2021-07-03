from django.test import TestCase
from django.contrib.auth import get_user_model
from ..models import Profile


class TestModel(TestCase):
    """ test user and profile model """
    
    def test_user_creation(self):
        payload = {'username': 'test60',
                   'password': 'TestPass123!',
                   'email': 'jan@test60.pl',
                   }
        
        user = get_user_model().objects.create_user(
            username = payload['username'],
            password = payload['password'],
            email = payload['email']
        )
        
        self.assertEqual(user.email, payload['email'])
        self.assertTrue(user.check_password(payload['password']))
        
    
            
        