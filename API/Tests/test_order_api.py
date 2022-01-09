import json

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from ProductApp import models
from ShoppingCardApp import models as shopping_model
from .products_data import PRODUCT_DATA, SECOND_PRODUCT

"""Help functions """

""" create user """


def create_user(data) -> get_user_model:
    return get_user_model().objects.create_user(**data)


""" Add COOKIES function"""


def add_cookie(data, client) -> Client:
    cookie = client.cookies["cart"] = json.dumps(data)

    return cookie


""" create product function"""


def create_product(data) -> models.Phones:
    return models.Phones.objects.create(**data)


class TestOrderApiUnauthorisedUser(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        create_product(PRODUCT_DATA)
        create_product(SECOND_PRODUCT)

    def setUp(self) -> None:
        self.client = Client()
        self.url_unauthorised = reverse('api:order-cart-unauthorised-user')
        self.random_product_id = list(
            models.MainProductDatabase.objects.all()
        )[0].id
        self.random_product_id_two = list(
            models.MainProductDatabase.objects.all()
        )[1].id

        self.payload = {
            'password': 'TestingFunc123',
            'email': 'test123@test.com',
        }

    def test_unauthorised_user_view(self) -> None:
        """ Test add one product to basket/cookie for unauthorised user"""

        data = {"products": {str(self.random_product_id): {"quantity": 1}}}
        add_cookie(data, self.client)

        main_product = models.MainProductDatabase.objects.get(
            id=self.random_product_id
        )
        res = self.client.post(
            self.url_unauthorised,
            content_type="application/json"
        )
        self.assertEqual(res.status_code, 200)

        res_data = json.loads(res.data)
        self.assertEqual(
            main_product.price, res_data['items'][0]['get_total']
        )

    def test_unauthorised_two_products(self) -> None:
        """ Test two products in basket/cookie - unauthorised user"""

        data = {"products": {str(
            self.random_product_id): {"quantity": 1},
            str(self.random_product_id_two): {"quantity": 2}}
                }
        add_cookie(data, self.client)

        res = self.client.post(
            self.url_unauthorised,
            content_type="application/json"
        )
        self.assertEqual(res.status_code, 200)

        res_data = json.loads(res.data)

        first_product = models.MainProductDatabase.objects.get(
            id=self.random_product_id
        )
        first_product_quantity = data["products"][str(
            self.random_product_id
        )]["quantity"]
        second_product = models.MainProductDatabase.objects.get(
            id=self.random_product_id_two
        )
        second_product_quantity = data["products"][str(
            self.random_product_id_two
        )]["quantity"]
        first_prod = first_product_quantity * first_product.price
        sec_prod = second_product_quantity * second_product.price
        basket_total = first_prod + sec_prod

        self.assertEqual(basket_total, res_data["order"]["get_cart_total"])
        self.assertEqual(first_product_quantity + second_product_quantity, 3)


class TestFinishOrder(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.url = reverse('API:order-finished')
        self.main_products = models.Phones.objects.create(**SECOND_PRODUCT)
        self.random_product_id = list(
            models.MainProductDatabase.objects.all()
        )[0].id
        self.payload = {
            'password': 'TestingFunc123',
            'email': 'test123@test.com',
        }

    def test_finish_order_unauthorised_user(self) -> None:
        """ Finish order for unauthorised user """

        data_cookie = {
            "products": {str(self.random_product_id): {"quantity": 1}}
        }
        add_cookie(data_cookie, self.client)

        data = {
            'price': 300,
            'payment': 'Blik',
            'customerName': "Test test",
            'customerCity': 'Warszawa',
            'customerState': 'Pomorskie',
            'customerZipcode': '12-345',
            'customerStreet': 'Testing 12',
            'customerEmail': 'test@tyest.com',
        }

        response = self.client.post(
            self.url,
            json.dumps(data),
            content_type="application/json"
        )

        order = shopping_model.Order.objects.filter(
            customer__email=data['customerEmail']
        )
        order = list(order)[-1]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(order.customer.email, 'test@tyest.com')
        self.assertTrue(order.transaction_status)

        address = shopping_model.ShippingAddress.objects.get(order=order)

        self.assertEqual(address.zipcode, data['customerZipcode'])
        self.assertEqual(order.get_cart_total, data['price'])

    def test_finish_order_authorised_user(self) -> None:
        """ Finish order for authorised user  """

        user = create_user(self.payload)
        self.client.login(
            email=self.payload['email'],
            password=self.payload['password']
        )

        customer = shopping_model.Customer.objects.create(
            user=user, email=self.payload['email']
        )
        order = shopping_model.Order.objects.create(customer=customer)
        product = models.MainProductDatabase.objects.get(
            id=self.random_product_id
        )
        shopping_model.OrderItem.objects.create(
            product=product, order=order, quantity=1
        )

        data = {
            'price': 300.00,
            'payment': 'Blik',
            'customerName': "Test test",
            'customerCity': 'Warszawa',
            'customerState': 'Pomorskie',
            'customerZipcode': '12-345',
            'customerStreet': 'Testing 12',
            'customerEmail': 'test@tyest.com',
        }

        response = self.client.post(
            self.url,
            json.dumps(data),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)

        order = shopping_model.Order.objects.get(customer=customer)
        address = shopping_model.ShippingAddress.objects.get(order=order)

        self.assertEqual(order.transaction_status, True)
        self.assertEqual(address.customer, customer)
        self.assertEqual(address.zipcode, '12-345')
