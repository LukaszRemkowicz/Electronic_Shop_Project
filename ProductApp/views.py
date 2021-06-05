from django.shortcuts import render
from django.views.generic import ListView
from .models import MainProductDatabase


class ProductPage(ListView):
    template_name = 'productapp/product.html'
    model = MainProductDatabase
