from django.http import response
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status 


URL = reverse('API:create_user')
URL_TOKEN = reverse('API:token')
URL_ACCOUNT_UPDATE = reverse('API:account_update')


def create_user(**kwargs) -> User:
    return get_user_model().objects.create_user(**kwargs)


class TestView(TestCase):
    
    def setUp(self) -> None:
        self.client = APIClient()
        self.user_data = {
            'username': 'Test',
            'password': 'Test12340!',
            'email': 'test@testing.com',
        }
        
    
    def test_user_creation(self) -> None:
        """ Test user creation """
                
        response = self.client.post(URL, self.user_data)
                
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        user = get_user_model().objects.get(**response.data)
        
        self.assertTrue(user.check_password(self.user_data['password']))
        self.assertNotIn('password', response.data)
        
    
    def test_user_exists(self) -> None:
        """ Test creating user that already exists """
        
        user = create_user(**self.user_data)
        response = self.client.post(URL, self.user_data)
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    
    def test_password_too_short(self) -> None:
        """ Test if user can create an account if password is too short"""
        
        data ={
            'username': 'Test',
            'password': 'Abc!abc!abc!abc!',
            'email': 'test@testing.com',
        }
        
        response = self.client.post(URL, data)
                
        if len(data['password']) >= 5:
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        else:
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
            user = get_user_model().objects.filter(email=data['email']).exists()
            
            self.assertFalse(user)        
        
    def test_create_token_for_user(self) -> None:
        """ test creating token for user """
        
        data = {
            'username': 'Test',
            'email': 'test@testing.com',
            'password': 'Test12340!',       
        }
        
        user = create_user(**data)
        response = self.client.post(URL_TOKEN, data)
        
        self.assertIn('token', response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    
    def test_create_invalid_tokent_credentials(self) -> None:
        """ test if token is not created if invalid credentials are given """
    
        user = create_user(**self.user_data)
        wrong_credentials = {
            'username': 'Test',
            'password': 'Test12!',
            'email': 'test@testing.com',
        }
        response = self.client.post(URL_TOKEN, wrong_credentials)
        
        self.assertNotIn('token', response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_create_token_no_user(self) -> None:
        """ test if token is not created if user doesn't exist """
        
        response = self.client.post(URL_TOKEN, self.user_data)
        
        self.assertNotIn('token', response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_create_token_missing_field(self) -> None:
        """ test that requaried fields are passed """
        
        wrong_data = {'email': 'email', 'password': ''} 
        response = self.client.post(URL_TOKEN, wrong_data)
        
        self.assertNotIn('token', response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        
    def test_if_unauthenticated_user_can_update(self) -> None:
        """ Test endpoint to not allow unauthorised user to access """
        
        response = self.client.get(URL_ACCOUNT_UPDATE)
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
        
class TestPrivteUser(TestCase):
    
    def setUp(self) -> None:
        self.user = create_user(
            email='test@testing.com', 
            username='Test', 
            password='Testing112!'
            )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        
    def test_profile_access_success(self) -> None:
        """ Test if logged user can access update endpoint """
        
        response = self.client.get(URL_ACCOUNT_UPDATE)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            'username': self.user.username,
            'email': self.user.email,
            'last_name': '',
            'first_name': '',
        })
        
    def test_post_is_not_allowed(self) -> None:
        
        response = self.client.post(URL_ACCOUNT_UPDATE, {})
        
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED) 
     
        
    def test_update_account(self) -> None:
        """ Test update account data """
        
        user_data = {
            'first_name': 'Lukas',
            'last_name': 'tester',
            'password': 'testing12341234'
        }
        
        response = self.client.patch(URL_ACCOUNT_UPDATE, user_data)    
        self.user.refresh_from_db()
        
        self.assertEqual(self.user.first_name, user_data['first_name'])
        self.assertEqual(self.user.last_name, user_data['last_name'])
        self.assertTrue(self.user.check_password(user_data['password']))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        
        
  