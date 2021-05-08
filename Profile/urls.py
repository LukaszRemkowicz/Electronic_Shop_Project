from django.urls import path
from .views import UserAccount as user_account
from .views import Register as register


urlpatterns = [
    path('account/', user_account.as_view()),
    path('register/', register.as_view(), name='register')
]