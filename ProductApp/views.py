from typing import Any, Dict

from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.models import User

from ShoppingCardApp.models import Customer, Order, OrderItem
from .models import MainProductDatabase
from .utils import filter_products



class ProductPage(ListView):
    template_name = 'productapp/product.html'
    model = MainProductDatabase
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super(ProductPage, self).get_context_data(**kwargs)
        id = self.kwargs['MainProductDatabase_id']
        product = MainProductDatabase.objects.get(id=id)
        
        try:
            customer = Customer.objects.get(user=self.request.user)
            order = Order.objects.get(customer=customer, complete=False)
            orderItem = OrderItem.objects.get(order=order)
            pieces = product.pieces - orderItem.quantity     
        except:
            orderItem = ''
            pieces = product.pieces
            
        same_products = filter_products(product.cattegory, product)
        print(same_products)
        
        if pieces <= 10:
                pieces_range = range(1, pieces+1)
        else: 
            pieces_range = range(1, 11)
            
                
        context['pieces_range'] = pieces_range
        context['same_products'] = same_products
        context['product'] = product
        context['pieces'] = pieces
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