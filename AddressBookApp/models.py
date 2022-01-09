from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class AddressBook(models.Model):
    name = models.CharField(blank=False, max_length=50)
    last_name = models.CharField(blank=False, max_length=50)
    city = models.CharField(blank=False, max_length=50)
    street = models.CharField(blank=False, max_length=100, default='')
    post_code = models.CharField(blank=False, max_length=10)
    state = models.CharField(blank=True, max_length=30)
    phone_number = models.CharField(blank=False, max_length=15)
    default = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.city
