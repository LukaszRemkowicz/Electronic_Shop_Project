from django.urls import path
from .views import LandingArticles


urlpatterns = [
    path('blog/', LandingArticles.as_view(), name='articles'),
]
