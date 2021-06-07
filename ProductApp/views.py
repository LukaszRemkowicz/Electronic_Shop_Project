from django.shortcuts import render
from django.views.generic import ListView
from .models import MainProductDatabase
from typing import Any, Dict


class ProductPage(ListView):
    template_name = 'productapp/product.html'
    model = MainProductDatabase
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super(ProductPage, self).get_context_data(**kwargs)
        id = self.request.GET.get('id') 
        product = MainProductDatabase.objects.get(id=id)
        context['product'] = product
        return context
    
class ProductsCart(ListView):
    template_name = 'productapp/product_cart.html'
    model = MainProductDatabase
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super(ProductsCart, self).get_context_data(**kwargs)
        cattegory = self.request.GET.get('cattegory')
        query = MainProductDatabase.objects.filter(cattegory=cattegory)
        context['query'] = query
        return context