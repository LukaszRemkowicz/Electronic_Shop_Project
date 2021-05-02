from django.db import models

from ProductApp.models import Product


class Order(models.Model):
    number = models.IntegerField(blank=False)
    user_id = models.IntegerField(blank=False)
    date = models.DateField(blank=False)

    # CHOICESs = ((str(prod.name), str(prod.name)) for prod in Product.objects.filter())

    product = models.ManyToManyField(Product)

    CHOICES = [
        ("Sent", "Sent"),
        ("Cancelled", "Cancelled"),
        ("In progress", "In progress"),
        ("Received", "Received")
    ]

    state = models.CharField(max_length=200, choices=CHOICES)
    cost = models.CharField(blank=False, max_length=50)
    # products = models.ManyToOneRel()

    def __str__(self):
        return str(self.number)
