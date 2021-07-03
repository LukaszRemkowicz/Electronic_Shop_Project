from django.forms.forms import Form
from django.http import request, response
from django.test import Client
from django.test.testcases import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test.client import RequestFactory
from django.contrib.auth.models import User

from ..models import Profile

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'
CREATE_USER_URL = '/register/'


def create_user(*args, **kwargs):
    """ Help function to create user by ORM """
    return get_user_model().objects.create_user(**kwargs)


class TestProfile(TestCase):

    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()


    def test_user_register(self):
        """ test user register """

        payload = {'username': 'test60',
                   'password1': 'TestPass123!',
                   'password2': 'TestPass123!',
                   'email': 'jan@test60.pl',
                   }

        response = self.client.post(CREATE_USER_URL, payload)
        # import pdb; pdb.set_trace()

        user = get_user_model().objects.get(username='test60', email='jan@test60.pl')

        self.assertEqual(user.email, payload['email'])
        self.assertEqual(user.username, payload['username'])
        
        
    def test_profile_creation(self):
        payload = {'username': 'test60',
                   'password': 'TestPass123!',
                   'email': 'jan@test60.pl',
                   }
        
        user = create_user(**payload)
        
        profile = Profile.objects.get(user_id=user.id)
        
        # import pdb; pdb.set_trace()

        
        self.assertEqual(profile.id, user.id) 


    def test_user_login(self):
        ''' test if user can log in '''

        user = create_user(username='test1', password='test123')
        login = self.client.login(username='test1', password='test123')
        response = self.client.get('/account/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(login, True)
        
        
    def test_user_logout(self):
        """Test if user can logout"""
        
        user = create_user(username='test1', password='test123')
        login = self.client.login(username='test1', password='test123')
        
        logout = self.client.logout()
        
        response = self.client.get('/account/')
        self.assertNotEqual(response.status_code, 200)
        
        
    def test_login_not_existed_user(self):
        ''' test if no existing user can acces account page '''

        user = self.client.login(username='test2', password='test1234')
        response = self.client.get('/account/')

        self.assertNotEqual(response.status_code, 200)
        
    def test_if_logged_user_can_enter_urls(self):
        pass
