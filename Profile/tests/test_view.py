from django.http import response
from django.test import Client
from django.test.testcases import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test.client import RequestFactory



CREATE_USER_URL = '/register/'

def create_user(*args, **kwargs):
    ''' Help function to create user by ORM '''
    return get_user_model().objects.create_user(**kwargs)

class TestProfile(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        
    def test_user_register(self):
        ''' test user register '''

        payload ={'username': 'test1', 
                    'password1':'test12344test12344',
                    'password2':'test12344test12344',
                    'email': 'jan@test.pl',
                    }
        # print(self.client.__dict__)
        
        response = self.client.post(CREATE_USER_URL, payload)
        
        # request = self.factory.get('/register/')
        # response = Register.as_view()(request)
        
        # print(response.context)
        # import pdb;pdb.set_trace()

        
        # self.assertEqual(response.status_code, 200)
        # print('First assertion ', "passed" if response.status_code==200 else "didn't passed")
        
        user = get_user_model().objects.get(username='test1', password='test12344')
        
        self.assertTrue(user.check_password(payload['password1']))
             
        
    def test_user_login(self):
        
        ''' test if user can log in '''

        user = create_user(username='test1', password='test123')
        login = self.client.login(username='test1', password='test123')
        response=self.client.get('/account/')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(login, True)
        
    
            
    def test_login_not_existed_user(self):
        
        ''' test if no existing user can acces account page '''

        user = self.client.login(username='test2', password='test1234')
        response=self.client.get('/account/')
        
        self.assertNotEqual(response.status_code, 200)
        
        