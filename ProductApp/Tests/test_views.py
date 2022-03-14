from django.test import TestCase, Client
from django.urls import reverse

from ..models import Phones, MainProductDatabase


class TestProductView(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.product_data = {
            'name': 'Iphone 10',
            'price': 3000,
            'pieces': 2,
            'ram': 8,
            'memory': 8,
            'model': ' ',
            'modem': 8,
            'color': 'grey',
            'describe': 'The best model',
            'producent': 'Apple',
            'producent_code': 'AABB123',
            'ean': 123456,
            'waterproof': True,
            'distribution': 'EU',
            'system': 'IOS',
            'processor': 'Intel',
            'cpu_clock': '400Mhz',
            'memory_card': '10GB',
            'usb': '3.0',
            'audio_jack': "Yes",
            'screen': '100x200',
            'screen_diagonal': 7.2,
            'battery': 100,
            'high': 10,
            'width': 10,
            'deep': 10,
            'weight': 0.5,
            'cattegory': 'Phones',
            'main_photo': ''
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

        url = reverse(
            'product_page',
            kwargs={
                'cattegory': product.cattegory,
                'MainProductDatabase_id': product_main.id
                })

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ProductApp/product.html')

    def test_products_cart(self):
        """ test products templete used """

        url = reverse('products_cart', args=['TV'])

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
