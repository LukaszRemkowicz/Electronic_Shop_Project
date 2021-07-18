from django.urls import path, include

from .views import CreateUserView, CreateTokenView, ManageUserView

app_name = "API"

urlpatterns = [
    path('create-user/', CreateUserView.as_view(), name='create_user'),
    path('token/', CreateTokenView.as_view(), name='token'),
    path('account-update/', ManageUserView.as_view(), name='account_update'),
]
