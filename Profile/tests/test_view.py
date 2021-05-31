from django.http import response
from django.test import Client
from django.test.testcases import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

def create_user(*args, **kwargs):
    return get_user_model().objects.create_user(**kwargs)

CREATE_USER_URL = reverse('register')

class TestProfile(TestCase):
    
    def setUp(self):
        client = Client()
        
        
    ''' test user register '''
    
    def test_user_register(self):
        response = self.client.post(CREATE_USER_URL, 
                                    {'username': 'test1', 
                                     'password1':'test123',
                                     'password2':'test123',
                                     'email': 'jan@test.pl'})

        
        self.assertEqual(response.status_code, 201)
        
    ''' test if user can log in '''
        
    def test_user_login(self):
        user = create_user(username='test1', password='test123')
        self.client.login(username='test1', password='test123')
        response=self.client.get('/account/')
        
        self.assertEqual(response.status_code, 200)
        
    
    ''' test if no existing user can acces account page '''
            
    def test_login_not_existed_user(self):
        user = self.client.login(username='test2', password='test1234')
        response=self.client.get('/account/')
        
        self.assertNotEqual(response.status_code, 200)
        
        