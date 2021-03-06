from django.urls import path
from .views import ProductPage, ProductsCart, QueryResult, Wishlist

urlpatterns = [
    path("products/", ProductsCart.as_view(), name="all-products"),
    path("products/<str:cattegory>/", ProductsCart.as_view(), name="products_cart"),
    path(
        "products/<str:cattegory>/<int:MainProductDatabase_id>/",
        ProductPage.as_view(),
        name="product_page",
    ),
    path("search/result/", QueryResult.as_view(), name="query-result"),
    path("wishlist/", Wishlist.as_view(), name="wishlist"),
]
