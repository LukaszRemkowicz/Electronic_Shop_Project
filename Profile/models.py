import uuid

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, \
                                        BaseUserManager, PermissionsMixin

from AddressBookApp.models import AddressBook
from MessagesApp.models import Complaint, Question


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new super user"""

        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """ Custom user model that supports email instead username """

    id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        primary_key=True
    )
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(
        max_length=255,
        default='',
        blank=True, null=True
    )
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=100, default='')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    address_book = models.ForeignKey(
        AddressBook,
        on_delete=models.CASCADE,
        blank=True, null=True,
        related_name='addres_book'
    )
    questions = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        blank=True, null=True,
        related_name='questions'
    )
    complain = models.ForeignKey(
        Complaint,
        on_delete=models.CASCADE,
        blank=True, null=True,
        related_name='complain'
    )
    keep_me = models.BooleanField(default=False)
    newsletter = models.BooleanField(default=False, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self) -> str:
        return self.email
