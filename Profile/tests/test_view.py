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

    def setUp(self) -> None:
        self.client = Client()
        self.payload = {
            'username': 'test60',
            'password1': 'TestPass123!',
            'password2': 'TestPass123!',
            'email': 'jan@test60.pl',
        }

    def test_user_register(self) -> None: 
        """ test user register """

        response = self.client.post(CREATE_USER_URL, self.payload)
        # import pdb; pdb.set_trace()

        user = get_user_model().objects.get(username='test60', email='jan@test60.pl')

        self.assertEqual(user.email, self.payload['email'])
        self.assertEqual(user.username, self.payload['username'])
        
        
    def test_if_password_is_too_short(self) -> None:
        """ check if user can create an account with short password """
        
        wrong_pass = {
            'username': 'test60',
            'password1': 'test',
            'password2': 'test',
            'email': 'jan@test60.pl',
        }
        
        response = self.client.post(CREATE_USER_URL, wrong_pass)
        user = get_user_model().objects.filter(username='test60', email='jan@test60.pl').exists()
        
        self.assertNotEqual(user, True)
        
    def test_wrong_email(self) -> None:
        """ test if user can create and accoutn with bad email """
        
        wrong_email = {
            'username': 'test60',
            'password1': 'TestPass123!',
            'password2': 'TestPass123!',
            'email': 'jantest60.pl',
        }
        
        response = self.client.post(CREATE_USER_URL, wrong_email)
        user = get_user_model().objects.filter(username='test60', email='jan@test60.pl').exists()
        
        self.assertNotEqual(user, True)
        
        
    def test_profile_creation(self) -> None:
        """ Test if profile is created after User creation """
        
        payload = {'username': 'test60',
                   'password': 'TestPass123!',
                   'email': 'jan@test60.pl',
                   }
        
        user = create_user(**payload)
        profile = Profile.objects.get(user_id=user.id)
        # import pdb; pdb.set_trace()
        self.assertEqual(profile.id, user.id) 


    def test_user_login(self) -> None:
        ''' test if user can log in '''

        user = create_user(username='test1', password='test123')
        login = self.client.login(username='test1', password='test123')
        response = self.client.get('/account/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(login, True)
        
        
    def test_user_logout(self) -> None:
        """Test if user can logout"""
        
        user = create_user(username='test1', password='test123')
        login = self.client.login(username='test1', password='test123')
        
        logout = self.client.logout()
        
        response = self.client.get('/account/')
        self.assertNotEqual(response.status_code, 200)
        
        
    def test_login_not_existed_user(self) -> None:
        ''' test if no existing user can acces account page '''

        user = self.client.login(username='test2', password='test1234')
        response = self.client.get('/account/')

        self.assertNotEqual(response.status_code, 200)
        
    def test_if_logged_user_can_enter_urls(self) -> None:
        
        user = create_user(username='test1', password='test123')
        login = self.client.login(username='test1', password='test123')
        
        url = reverse('register')
        
        response = self.client.get(url)
        
        self.assertNotEqual(response.status_code, 200)
        
        
    def test_user_profile(self) -> None:
        """ Testing user profile template """
        
        user = create_user(username='test1', password='test123')
        login = self.client.login(username='test1', password='test123')
        
        url = reverse('account')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/account.html')
        
        
    def test_not_authorised_user(self) -> None:
        """ test not authorised user if can enter account url """
        
        url = reverse('account')
        response = self.client.get(url)
        
        self.assertNotEqual(response.status_code, 200)
        
        
    def test_landing_page_template(self) -> None:
        """ test main template """
        
        url = reverse('landing-page')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'landing_page.html')
