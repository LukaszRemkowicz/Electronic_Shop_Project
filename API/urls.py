from django.urls import path, include

from . import views

app_name = "API"


urlpatterns = [
    path('create-user/', views.CreateUserView.as_view(), name='create_user'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('account-update/', views.ManageUserView.as_view(), name='account_update'),
    path('order-cart-unauthorised-user/', views.UnauthorisedUserOrderView.as_view(), name='order-cart-unauthorised-user'),
    path('order-completed/', views.FinishOrderView.as_view(), name='order-finished'),
    path('update-item/', views.UpdateItemView.as_view(), name="update_item"),
]
