from django.forms.forms import Form
from Profile.forms import RegisterForm
from django.http import request, response
from django.test import Client
from django.test.testcases import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test.client import RequestFactory
from ..views import Register
from django.contrib.messages.storage.fallback import FallbackStorage



MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'
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

        payload ={'username': 'test60', 
                    'password1':'Solaris4290',
                    'password2':'Solaris4290',
                    'email': 'jan@test60.pl',
                    }
                # print(self.client.__dict__)
        
        # response = self.client.post(CREATE_USER_URL, payload)
        
        # request = self.factory.post('/register/', payload)
        # setattr(request, 'session', 'session')
        # setattr(request, '_messages', FallbackStorage(request))
        # responde = Register.as_view()(request)
        
        form = RegisterForm(data=payload)
        print(form)
        form.save()
                
        import pdb;pdb.set_trace()
        

        # request = self.factory.get('/register/')
    
        
        # response = Register.as_view()(request)
        
        # print(response.context)

        
        # self.assertEqual(response.status_code, 200)
        # print('First assertion ', "passed" if response.status_code==200 else "didn't passed")
        
        user = get_user_model().objects.get(username='test60', email='jan@test60.pl')
        
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
        
        