from django.urls import path, re_path
from .views import ProductPage

urlpatterns = [
    path('product/<int:MainProductDatabase_id>/', ProductPage.as_view(), name="product_page")
]
