from django.urls import path, re_path
from .views import ProductPage, ProductsCart

urlpatterns = [
    path('product/<int:MainProductDatabase_id>/', ProductPage.as_view(), name="product_page"),
    path('products/<str:cattegory>/', ProductsCart.as_view(), name="products_cart"),
]
