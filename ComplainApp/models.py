from django.db import models

from ProductApp.models import Product
from OrdersApp.models import Order
from MessagesApp.models import Message


class Complain(models.Model):
    rma = models.IntegerField(blank=False)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    CHOICES = [
        ("In progress", "In progress"),
        ("Sent", "Sent"),
        ("Closed", "Closed")
    ]

    status = models.CharField(choices=CHOICES, max_length=50)
    user_id = models.IntegerField(blank=False)
    tread = models.OneToOneField(Message, on_delete=models.CASCADE)
    order_number = models.OneToOneField(Order, on_delete=models.CASCADE)

    def __str__(self):
        return self.rma

