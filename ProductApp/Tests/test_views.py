from django import urls
from django.http import response
from django.test import TestCase, Client
from django.urls import reverse

from ..models import Phones, MainProductDatabase

class TestProductView(TestCase):
    
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
    
    def test_main_product_signal(self) -> None:
        """ test if main product is created """
        
        product = Phones.objects.create(**self.product_data)
        product_main = MainProductDatabase.objects.get(ean=product.ean)
        
        self.assertEqual(product_main.ean, product.ean)
        
    
    def test_product_page_templete(self):
        """ test if good product template is used """
        product = Phones.objects.create(**self.product_data)
        product_main = MainProductDatabase.objects.get(ean=product.ean)
                
        url = f'/product/{product.id}/?id={product.id}'
                        
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'productapp/product.html')
        
        
    def test_products_cart(self):
        """ test products templete used """
        
        url = reverse('products_cart')
        
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        
        