from django.urls import path
from . import views 

urlpatterns = [
    path('cart/', views.cart, name="shopping-cart"),
    path('cart/sumarry', views.address_checkout, name="summary-cart"),
]
