from django.db import models
from django.conf import settings
from django.db.models.expressions import F

from AddressBookApp.models import AddressBook
from MessagesApp.models import Complaint, Question
from ShoppingCardApp.models import Order

User = settings.AUTH_USER_MODEL

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    number = models.IntegerField(blank=True, null=True)
    orders = models.ManyToManyField(Order, blank=True, null=True)
    address_book = models.OneToOneField(AddressBook, on_delete=models.CASCADE, blank=True, null=True)
    questions = models.OneToOneField(Question, on_delete=models.CASCADE, blank=True, null=True)
    complain = models.OneToOneField(Complaint, on_delete=models.CASCADE, blank=True, null=True)
    keep_me = models.BooleanField(default=False)
    newsletter = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self) -> str:
        return self.user.username
