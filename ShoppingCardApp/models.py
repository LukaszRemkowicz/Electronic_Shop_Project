from django.db import models
from django.contrib.auth.models import User

from ProductApp.models import MainProductDatabase as Product


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    
    def __str__(self) -> str:
        return self.email
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=200, null=True)
    
    def __str__(self) -> str:
        return str(self.id)
    
class OrderItem(models.Model):
    product = models.OneToOneField(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
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
