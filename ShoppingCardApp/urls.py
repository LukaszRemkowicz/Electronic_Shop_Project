from django.urls import path
from .views import update_item, cart, address_checkout, order_finished

urlpatterns = [
    path('update-item/', update_item, name="update_item"),
    path('update-cart-items/', update_item, name="update_cart_items"),
    path('cart/', cart, name="shopping-cart"),
    path('cart/sumarry', address_checkout, name="summary-cart"),
    path('order-completed/', order_finished, name='order-finished')
]
