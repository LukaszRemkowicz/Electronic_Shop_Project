from django.urls import path

from . import views

app_name = "API"


urlpatterns = [
    path('create-user/', views.CreateUserView.as_view(),
         name='create_user'),
    path('token/', views.CreateTokenView.as_view(),
         name='token'),
    path('account-update/', views.ManageUserView.as_view(),
         name='account_update'),
    path('profile-update/', views.ManageProfileView.as_view(),
         name='profile_update'),
    path('order-cart-unauthorised-user/',
         views.UnauthorisedUserOrderView.as_view(),
         name='order-cart-unauthorised-user'),
    path('order-completed/', views.FinishOrderView.as_view(),
         name='order-finished'),
    path('update-item/',
         views.UpdateItemView.as_view(),
         name="update_item"),
    path('get-product/',
         views.GetProductData.as_view(),
         name="get_product"),
    path('create-review/', views.CreateReview.as_view(),
         name='create-review'),
    path('create-question/', views.CreateQuestion.as_view(),
         name='create-question'),
    path('product-dict/', views.ProductDict.as_view(),
         name='product-dict'),
    path('product/<int:product_id>/', views.ProductView.as_view(),
         name='update-product'),
    path('blog/<int:product_id>/comments/',
         views.UpdateBlogComment.as_view(),
         name='update-blog-comment'),
    path('newsletter/', views.Newsletter.as_view(),
         name='Newsletter'),
    path('product-quantity/<int:product_id>/',
         views.OrderProductQuantity.as_view(),
         name='product-quantity'),
    path('create-product/', views.CreateProduct.as_view(),
         name='create-product'),
]
