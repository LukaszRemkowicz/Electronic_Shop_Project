from django.db import models
from django.contrib.auth.models import User


class AddressBook(models.Model):
    name = models.CharField(blank=False, max_length=50)
    last_name = models.CharField(blank=False, max_length=50)
    city = models.CharField(blank=False, max_length=50)
    post_code = models.CharField(blank=False, max_length=10)
    phone_number = models.CharField(blank=False, max_length=15)
    default = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.city
