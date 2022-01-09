import json

from django.test import TestCase, Client
from django.urls import reverse

from ProductApp import models
from . import products_data


def create_product(payload):
    return models.Phones.objects.create(**payload)


class TestProductData(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.url = reverse('api:get_product')
        self.product = create_product(products_data.PRODUCT_DATA)
        self.second_product = create_product(products_data.SECOND_PRODUCT)

        self.data = {'productData': {
            "productClicked": {
                "type": "white",
                "divId": "product-color-data"
            },
            "productId": self.product.id,
            "itemsId": [self.second_product.id, self.product.id, ]
        }}

    def test_get_product_data(self):
        """ test sending data to filter (mock JavaScript data) """

        response = self.client.post(
            self.url,
            json.dumps(self.data),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(int(response.data), self.second_product.id)

    def test_wrong_product_data(self):
        """ test wrong data - object doesnt exists """

        data = {'productData': {
            "productClicked": {
                "type": "blue",
                "divId": "product-color-data"
            },
            "productId": self.product.id,
            "itemsId": [self.second_product.id, self.product.id, ]
        }}

        response = self.client.post(
            self.url, json.dumps(data),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.data, self.second_product.id)
