from django.urls import path
from .views import update_item, cart

urlpatterns = [
    path('update-item/', update_item, name="update_item"),
    path('cart/', cart, name="shopping-cart")
]
