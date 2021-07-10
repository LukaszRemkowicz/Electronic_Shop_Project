from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from ..models import AddressBook


def create_user(*args, **kwargs) -> User:
    """ Help function to create user """
    return get_user_model().objects.create_user(**kwargs)

class TestAdressBookApp(TestCase):
    
    def setUp(self) -> None:
        self.payload = {
            'username': 'Test',
            'password': 'TestingFunc123',
            'email': 'test123@test.com',
        }  
    
    def test_address_book_model(self) -> None:
        
        user = create_user(**self.payload)
        
        address_data = {
            'name': 'Lukas',
            'last_name': 'Lukas Last Name',
            'city': 'Elblag',
            'post_code': '12-345',
            'phone_number': '111-222-333',
            'user': user,
        }
        
        address = AddressBook.objects.create(**address_data)
        
        self.assertEqual(address.user.username, 'Test')
        self.assertEqual(address.city, 'Elblag')