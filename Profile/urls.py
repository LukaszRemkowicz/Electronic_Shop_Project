from django.urls import path
from django.contrib.auth.views import LogoutView as Logout

from .views import UserAccount 
from .views import Register, LandingPage




urlpatterns = [
    path('account/', UserAccount.as_view(), name='account'),
    path('register/', Register.as_view(), name='register'),
    path('logout/', Logout.as_view(next_page='landing-page'), name='logout'),
    # path('login/', LoginView.as_view(), name='login'),
    path('', LandingPage.as_view(), name='landing-page'),
]