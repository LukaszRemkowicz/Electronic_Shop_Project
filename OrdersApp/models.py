from django.db import models


class Order(models.Model):
    number = models.IntegerField(blank=False)
    user_id = models.IntegerField(blank=False)
    date = models.DateField(blank=False)

    CHOICES = [
        ("Sent","Sent"),
        ("Cancelled", "Cancelled"),
        ("In progress", "In progress"),
        ("Received", "Received")
    ]

    state = models.CharField(max_length=200, choices=CHOICES)
    cost = models.CharField(blank=False, max_length=50)

    def __str__(self):
        return self.number
