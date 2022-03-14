from django.conf import settings
from django.db import models

from ProductApp.models import MainProductDatabase as Product

User = settings.AUTH_USER_MODEL

CHOICES = [
    ("Sent", "Sent"),
    ("Cancelled", "Cancelled"),
    ("In progress", "In progress"),
    ("Received", "Received"),
]


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    email = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self) -> str:
        return str(self.email) if self.email else self.user.email


class Order(models.Model):

    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, blank=True, null=True
    )
    date_order = models.DateTimeField(auto_now_add=True)
    complete = models.CharField(max_length=200, choices=CHOICES, default="Received")
    transaction_id = models.CharField(max_length=200, blank=True, default="")
    transaction_status = models.BooleanField(default=False)
    transaction_finished = models.DateTimeField(blank=True, null=True)

    def __str__(self) -> str:
        return str(self.id)

    @property
    def get_cart_total(self) -> float:
        orderitems = self.orderitem_set.all()
        # listed = [item for item in orderitems]
        total = sum([item.get_total for item in orderitems])

        return total

    @property
    def get_cart_items(self) -> int:
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])

        return total


class OrderItem(models.Model):

    status = [("Colecting", "Collecting"), ("Collected", "Collected"), ("Sent", "Sent")]

    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, blank=True, null=True
    )
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, choices=status, default="Collecting")
    bought = models.IntegerField(default=0, null=True, blank=True)

    @property
    def get_total(self) -> float:

        if self.product.promotion:
            try:
                total = self.product.promotion * self.quantity
            except TypeError:
                total = 0
        else:
            try:
                total = self.product.price * self.quantity
            except TypeError:
                total = 0

        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, blank=True, null=True
    )
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    data_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.address


class ShoppingCard(models.Model):
    pass
    # product_id = models.OneToOneField(Product, on_delete=models.CASCADE)
