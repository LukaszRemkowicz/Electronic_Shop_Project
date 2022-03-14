from django.test import TestCase
from django.contrib.auth import get_user_model

from ..models import AddressBook


def create_user(*args, **kwargs) -> get_user_model:
    """Help function to create user"""
    return get_user_model().objects.create_user(**kwargs)


class TestAdressBookApp(TestCase):
    def setUp(self) -> None:
        self.payload = {
            "password": "TestingFunc123",
            "email": "test123@test.com",
        }

    def test_address_book_model(self) -> None:
        user = create_user(**self.payload)

        address_data = {
            "name": "Lukas",
            "last_name": "Lukas Last Name",
            "city": "Elblag",
            "post_code": "12-345",
            "phone_number": "111-222-333",
            "user": user,
        }

        address = AddressBook.objects.create(**address_data)

        address_data_two = {
            "name": "Lukas",
            "last_name": "Lukas Last Name",
            "city": "Gdansk",
            "post_code": "12-345",
            "phone_number": "111-222-333",
            "user": user,
        }

        """ Check if user can create more addresses """
        address_two = AddressBook.objects.create(**address_data_two)

        self.assertEqual(address.user.email, "test123@test.com")
        self.assertEqual(address.city, "Elblag")
        self.assertEqual(address_two.city, "Gdansk")
