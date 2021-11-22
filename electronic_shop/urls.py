from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("Profile.urls"), name="home"),
    path('', include("ProductApp.urls"), name="products"),
    path('', include('ShoppingCardApp.urls'), name="shopping_cart"),
    path('api/', include('API.urls', namespace='api')),
    path('articles/', include('Articles.urls'), name='articles'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
