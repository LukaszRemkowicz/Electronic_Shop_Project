from django.db import models

from ProductApp.models import Product


class ShoppingCard(models.Model):
    pass
    # product_id = models.OneToOneField(Product, on_delete=models.CASCADE)
