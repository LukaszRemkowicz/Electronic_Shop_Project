from django.urls import path
from .views import LandingArticles


urlpatterns = [
    path("blog/<int:article_id>/", LandingArticles.as_view(), name="articles"),
]
