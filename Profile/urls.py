from django.urls import path
from django.contrib.auth.views import LogoutView as Logout

from .views import UserAccount as user_account
from .views import Register




urlpatterns = [
    path('account/', user_account.as_view(), name='account'),
    path('register/', Register.as_view(), name='register'),
    path('logout/', Logout.as_view(next_page='landing-page'), name='logout'),
]