from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from ProductApp.models import Phones, MainProductDatabase
from ..models import Customer, Order, OrderItem, ShippingAddress

import json


def create_user(*args, **kwargs) -> User:
    """ Help function to create user """
    return get_user_model().objects.create_user(**kwargs)

def create_customer(user: User) -> Customer:
    """ Help function to create customer """
    return Customer.objects.create(user=user, email=user.email)

class TestShoppingCartViews(TestCase):
    
    def setUp(self) -> None:
        
        self.client = Client()
        self.product_data={
                'name': 'Iphone 10',
                'model': 'Iphone 10',
                'price': 3000,
                'pieces': 2,
                'ram': 8,
                'memory': 8,
                'modem': 8,
                'color': 'grey',
                'describe': 'The best model',
                'producent': 'Apple',
                'producent_code': 'AABB123',
                'ean': 12345644,
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
                'battery': 5000,
                'high':'10cm',
                'width': '10cm',
                'deep': '10cm',
                'weight': '500g',
                'cattegory': 'Monitor'
            }
        
        self.product_monitor = {
            'name':'LG',
            'model': 'Samsung',
            'price' : 1000,
            'pieces' : 20,
            'color' : 'White',
            'resolution': '100x200',
            'refresh_rate' : 400,
            'power_consumption' : 20,
            'producent' : 'Samsung',
            'producent_code' : 'AA@@SS',
            'ean' : 1122343,
            'distribution' : 'EU',
            'screen': 'Mat',
            'screen_diagonal' : '15\'',
            'high' : '200',
            'width' : '100',
            'deep' : '10',
            'weight' : '20kg',
        }
        
        self.payload = {
            'username': 'Test',
            'password': 'TestingFunc123',
            'email': 'test123@test.com',
        }  
        self.data = {
            'date_order': '2021-07-04 14:30:59',
            'transaction_id': '12A',
        }
    
    def test_address_checkout(self) -> None:
        """ testing address checkout endpoint """
        
        url = reverse('summary-cart')
        
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Shoppingcart/address-checkout.html')
    
    
    def test_check_if_cart_get_templete(self) -> None:
        """ testing cart endpoint """
        
        url = reverse('shopping-cart')
        
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Shoppingcart/cart.html')
        
    def test_update_item_api(self) -> None:
        """ check if user can add item to the basket """
        
        url = reverse('api:update_item')

        user = create_user(**self.payload)
        login = self.client.login(**self.payload)
        customer = create_customer(user)
        product = Phones.objects.create(**self.product_data)
        product_main = MainProductDatabase.objects.get(ean=product.ean)
        order = Order.objects.create(customer=customer, date_order=self.data['date_order'], transaction_id='11')
        order_item = OrderItem.objects.create(order=order, product=product_main, quantity=3, date_ordered=self.data['date_order'])
         
        body = {
            'productId': product.id,
            'action': 'add',
        }
        
        """ add 5 items """
        
        for num_of_iteration in range(1,6):
            
            order_item_testing = OrderItem.objects.get(order=order)       
            response = self.client.post(url, 
                                        json.dumps(body), 
                                        content_type="application/json")
    
            self.assertEqual(response.status_code, 200)
            order_item_testing = OrderItem.objects.get(order=order)
        
            self.assertEqual(order_item.quantity + num_of_iteration, order_item_testing.quantity)
 

    def test_substract_item_api(self) -> None:
        """ check if user can substract item from the basket """
        
        url = reverse('api:update_item')

        user = create_user(**self.payload)
        login = self.client.login(**self.payload)
        customer = create_customer(user)
        product = Phones.objects.create(**self.product_data)
        product_main = MainProductDatabase.objects.get(ean=product.ean)
        order = Order.objects.create(customer=customer, date_order=self.data['date_order'], transaction_id='11')
        order_item = OrderItem.objects.create(order=order, product=product_main, quantity=2, date_ordered=self.data['date_order'])
        
        body = {
            'productId': product.id,
            'action': 'remove',
        }
        
        response = self.client.post(url, json.dumps(body), content_type="application/json")
        self.assertEqual(response.status_code, 200)
        
        order_item_testing = OrderItem.objects.get(order=order)
        
        self.assertEqual(order_item.quantity - 1, order_item_testing.quantity)
        
        """ delete order_item """
        
        response = self.client.post(url, json.dumps(body), content_type="application/json")
        order_item_testing = OrderItem.objects.filter(order=order).exists()
        
        self.assertNotEqual(order_item_testing, True)


    def test_order_complete_API(self) -> None:
        """ check complete order """
        
        url = reverse('api:order-finished')
        
        user = create_user(**self.payload)
        login = self.client.login(**self.payload)
        
        customer = create_customer(user)
        product = Phones.objects.create(**self.product_data)
        product_main = MainProductDatabase.objects.get(ean=product.ean)
        order = Order.objects.create(customer=customer, date_order=self.data['date_order'])
        order_item = OrderItem.objects.create(order=order, product=product_main, quantity=2, date_ordered=self.data['date_order'])
                
        body = {
            'price': float(order.get_cart_total),
            'payment': 'paypal',
            'customerName' : 'Test Test',
            'customerCity' : 'Warszawa',
            'customerState' : 'Testowo 1',
            'customerZipcode' : '12-300',
            'customerStreet' : 'TestStreet',
            'customerEmail' : 'test@test.com',
        }

        response = self.client.post(url, json.dumps(body), content_type="application/json")

        shipping = ShippingAddress.objects.get(order=order)
        order = Order.objects.get(customer=customer)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(order.complete, True)
        self.assertEqual(shipping.city, body['customerCity'])
        