from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField(max_length=10)

    def __str__(self):
        return self.name
