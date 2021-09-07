from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from ProductApp.models import Phones, MainProductDatabase
from ShoppingCardApp.models import Customer, Order
from ..models import Complaint, Question


def create_user(*args, **kwargs) -> User:
    """ Help function to create user """
    return get_user_model().objects.create_user(**kwargs)

def create_customer(user: User):
    """ Help function to create customer """
    return Customer.objects.create(user=user, email=user.email)


class TestMessageApp(TestCase):
    
    def setUp(self) -> None:
        client = Client()
        self.product_data={
                'name': 'Iphone 10',
                'price': 3000,
                'pieces': 2,
                'ram': 8,
                'memory': 8,
                'modem': 8,
                'color': 'grey',
                'describe': 'The best model',
                'producent': 'Apple',
                'producent_code': 'AABB123',
                'ean': 123456,
                'waterproof': True,
                'distibution': 'EU',
                'system': 'IOS',
                'processor': 'Intel',
                'cpu_clock': '400Mhz',
                'memory_card': '10GB',
                'usb': '3.0',
                'audio_jack': "Yes",
                'screen': '100x200',
                'screen_diagonal': 7.2,
                'battery': 100,
                'high':'10cm',
                'width': '10cm',
                'deep': '10cm',
                'weight': '500g',
                'cattegory': 'phones'
            }
        
        self.payload = {
            'username': 'Test',
            'password': 'TestingFunc123',
            'email': 'test123@test.com',
        }  
    
    def test_complaint_model(self) -> None:
        """ test if complaint can be created """
        
        user = create_user(**self.payload)
        login = self.client.login(**self.payload)
        customer = create_customer(user)
        product = Phones.objects.create(**self.product_data)
        product_main = MainProductDatabase.objects.get(ean=product.ean)
        order = Order.objects.create(customer=customer, transaction_id='11')
                
        complaint_data = {
            'product': product_main,
            'status': 'In progress',
            'user': user,
            'message': 'Lorem Ipsum',
            'order': order,
        }
        
        complaint = Complaint.objects.create(**complaint_data)

        self.assertEqual(complaint.user.username, 'Test')
        self.assertEqual(complaint.order.transaction_id, '11')
        
    
    def test_question_model(self):
        """ test if question can be asked """
        
        user = create_user(**self.payload)
        
        question_data = {
            'subject': 'Lorem',
            'message': 'Lorem Ipsum',
            'user': user,
            'state': 'In progress',
        }
        
        question = Question.objects.create(**question_data)
        
        self.assertEqual(question.subject, 'Lorem')
        self.assertEqual(question.user.username, 'Test')