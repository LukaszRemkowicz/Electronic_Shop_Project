from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


from ProductApp.models import MainProductDatabase
from OrdersApp.models import Order



class Complaint(models.Model):
    type = models.CharField(default="RMA", max_length=20)
    product = models.OneToOneField(MainProductDatabase, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    CHOICES = [
        ("In progress", "In progress"),
        ("Sent", "Sent"),
        ("Closed", "Closed")
    ]

    status = models.CharField(choices=CHOICES, max_length=50, default="checking the complaint")
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=10000)
    order_number = models.OneToOneField(Order, on_delete=models.CASCADE)

    def __str__(self):
        return f"RMA nr. {self.id}"


class Question(models.Model):
    type = models.CharField(default="Question", max_length=300)
    subject = models.CharField(blank=True, max_length=20)
    message = models.CharField(max_length=10000)
    date = models.DateField(auto_now_add=True)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)

    CHOICES = [
        ("Answered", "Answered"),
        ("Readed", "Readed"),
        ("Closed", "Closed")
    ]

    state = models.CharField(max_length=50, choices=CHOICES)

    def __str__(self):
        return self.subject
