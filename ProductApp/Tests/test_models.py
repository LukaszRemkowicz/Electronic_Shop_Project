from django.test import TestCase

from ..models import Phones, MainProductDatabase


class TestProduct(TestCase):
    """test product model"""

    def test_product_creation(self) -> None:
        """test if product is created"""

        data = {
            "name": "Iphone 10",
            "price": 360,
            "pieces": 2,
            "ram": 8,
            "memory": 8,
            "modem": 8,
            "color": "grey",
            "describe": "The best model",
            "producent": "Apple",
            "producent_code": "AABB123",
            "ean": 2343356,
            "waterproof": True,
            "distribution": "EU",
            "system": "IOS",
            "model": " ",
            "processor": "Intel",
            "cpu_clock": "400Mhz",
            "memory_card": "10GB",
            "usb": "3.0",
            "audio_jack": "Yes",
            "screen": "100x200",
            "screen_diagonal": 7.2,
            "battery": 100,
            "high": 10,
            "width": 10,
            "deep": 10,
            "weight": 0.5,
            "cattegory": "phones",
        }

        product = Phones.objects.create(**data)

        self.assertEqual(product.name, data["name"])

        self.assertEqual(str(product), data["name"])

    def test_if_mainproduct_is_created(self) -> None:
        """check if main product is created"""

        data = {
            "name": "Iphone 10",
            "price": 3000,
            "pieces": 2,
            "ram": 8,
            "memory": 8,
            "modem": 8,
            "color": "grey",
            "describe": "The best model",
            "producent": "Apple",
            "producent_code": "AABB123",
            "ean": 123456,
            "model": " ",
            "waterproof": True,
            "distribution": "EU",
            "system": "IOS",
            "processor": "Intel",
            "cpu_clock": "400Mhz",
            "memory_card": "10GB",
            "usb": "3.0",
            "audio_jack": "Yes",
            "screen": "100x200",
            "screen_diagonal": 7.2,
            "battery": 100,
            "high": 10,
            "width": 10,
            "deep": 10,
            "weight": 0.5,
            "cattegory": "phones",
        }

        product = Phones.objects.create(**data)
        main_model = MainProductDatabase.objects.get(ean=product.ean)

        self.assertEqual(main_model.ean, data["ean"])
