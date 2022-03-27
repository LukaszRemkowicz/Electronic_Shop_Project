from django.urls import path
# from django.contrib.auth.views import LogoutView as Logout

from .views import DetailOrder, UserAccount, Logout
from .views import Register

urlpatterns = [
    path(
        "account/order-detail/<int:order_id>/",
        DetailOrder.as_view(),
        name="order-detail",
    ),
    path("account/", UserAccount.as_view(), name="account"),
    path("register/", Register.as_view(), name="register"),
    path("logout/", Logout.as_view(next_page="landing-page"), name="logout"),
    # path('login/', LoginView.as_view(), name='login'),
]
