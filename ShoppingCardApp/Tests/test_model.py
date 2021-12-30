from django.contrib.auth import get_user_model
from django.test import TestCase

from ..models import Customer, Order, OrderItem, ShippingAddress
from ProductApp.models import Phones, MainProductDatabase

def create_user(*args, **kwargs):
    """ Help function to create user """
    return get_user_model().objects.create_user(**kwargs)

def create_customer(user):
    """ Help function to create customer """
    return Customer.objects.create(user=user, email=user.email)


class TestOrderModel(TestCase):
    """ Customer model """

    def setUp(self) -> None:

        self.payload = {
        'password': 'TestingFunc123',
        'email': 'test123@test.com',
    }

        self.data = {
            'date_order': '2021-07-04 14:30:59',
            'transaction_id': '12A',
        }

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
                'high':10,
                'width': 10,
                'deep': 10,
                'weight': 0.5,
                'cattegory': 'phones'
            }

        self.shipping_data = {
            'address':'testing 12',
            'city': 'Test',
            'state': 'Warminsko-Mazurskie',
            'zipcode': '11-222',
        }


    def test_if_customer_can_be_create(self) -> None:
        """ test customer model """

        user = create_user(**self.payload)
        customer = create_customer(user)

        self.assertEqual(customer.email, user.email)

    def test_Order_creation(self) -> None:
        """ test order model """

        user = create_user(**self.payload)
        customer = create_customer(user)
        order = Order.objects.create(customer=customer, **self.data)

        self.assertEqual(order.customer.email, user.email)

    def test_order_item(self) -> None:
        """ test order item model """

        user = create_user(**self.payload)
        customer = create_customer(user)
        order = Order.objects.create(customer=customer, **self.data)
        product = Phones.objects.create(**self.product_data)
        main_product_instance = MainProductDatabase.objects.get(ean=product.ean)

        order_item = OrderItem.objects.create(
            product=main_product_instance,
            order=order,
            quantity=1,
            date_ordered=self.data['date_order']
        )

        self.assertEqual(order_item.product.name, 'Iphone 10')

        self.assertEqual(order_item.get_total, order_item.quantity * product.price)

    def test_shipping_address(self) -> None:
        """ test shipping model """

        user = create_user(**self.payload)
        customer = create_customer(user)
        order = Order.objects.create(customer=customer, **self.data)

        shipping = ShippingAddress.objects.create(
            customer=customer,
            order=order,
            data_added = self.data['date_order'],
            **self.shipping_data
        )

        self.assertEqual(shipping.customer.user.email, 'test123@test.com')
        self.assertEqual(shipping.state, 'Warminsko-Mazurskie')

    def test_models_methods(self) -> None:
        user = create_user(**self.payload)
        customer = create_customer(user)
        order = Order.objects.create(customer=customer, **self.data)
        product = Phones.objects.create(**self.product_data)
        main_product_instance = MainProductDatabase.objects.get(ean=product.ean)

        order_item = OrderItem.objects.create(
            product=main_product_instance,
            order=order,
            quantity=1,
            date_ordered=self.data['date_order']
        )

        shipping = ShippingAddress.objects.create(
            customer=customer,
            order=order,
            data_added = self.data['date_order'],
            **self.shipping_data
        )

        orderitems = OrderItem.objects.all()
        total = sum([item.get_total for item in orderitems])

        """ check OrderItem get_total method """
        self.assertEqual(order_item.get_total, order_item.quantity * product.price)

        """ check Order get_cart_total method """
        self.assertEqual(order.get_cart_total, total)

        """ check Order get_cart_items method """
        total = sum([item.quantity for item in orderitems])
        self.assertEqual(order.get_cart_items, total)

        """ check Order __str__ method """
        self.assertEqual(str(order), str(order.id))

        """ Check Customer __str__ method """
        self.assertEqual(str(customer), user.email)

        """ Check ShippingAddress __str__ method """
        self.assertEqual(str(shipping), shipping.address)
