from django.urls import path
from .views import update_item

urlpatterns = [
    path('update-item/', update_item, name="update_item")
]
