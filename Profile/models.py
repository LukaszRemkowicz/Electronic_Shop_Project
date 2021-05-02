from django.db import models
from django.conf import settings

from OrdersApp.models import Order
from AddressBookApp.models import AddressBook
from QuestionApp.models import Question
from ComplainApp.models import Complain

User = settings.AUTH_USER_MODEL


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    number = models.IntegerField(blank=True, null=True)
    orders = models.OneToOneField(Order, on_delete=models.CASCADE, blank=True, null=True)
    address_book = models.OneToOneField(AddressBook, on_delete=models.CASCADE, blank=True, null=True)
    questions = models.OneToOneField(Question, on_delete=models.CASCADE, blank=True, null=True)
    complain = models.OneToOneField(Complain, on_delete=models.CASCADE, blank=True, null=True)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
