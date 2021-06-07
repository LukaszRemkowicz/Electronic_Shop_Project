from django.urls import path, re_path
from .views import ProductPage, ProductsCart

urlpatterns = [
    path('product/<int:MainProductDatabase_id>/', ProductPage.as_view(), name="product_page"),
    re_path(r'products/$', ProductsCart.as_view(), name="products_cart"),
]
