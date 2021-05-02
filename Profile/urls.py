from django.urls import path
from .views import UserAccount as user_account


urlpatterns = [
    path('account/', user_account.as_view())
]