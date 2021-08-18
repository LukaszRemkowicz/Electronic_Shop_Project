import json
import datetime

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.contrib import messages

from ProductApp.models import MainProductDatabase 
from .models import Customer, Order, OrderItem, ShippingAddress
from AddressBookApp.models import AddressBook
from .utils import order_cart, cart_data, complete_unauthorised_user_order, DecimalEncoder


""" checkout order """

def address_checkout(request) -> HttpResponse:
    
    items, order, address_list = cart_data(request) 
    context = {'items': items, 'order': order, 'address_list': address_list}
    
    return render(request,'Shoppingcart/address-checkout.html', context)


""" Render cart template """

def cart(request) -> HttpResponse:
    
    items, order, address_list = cart_data(request)
    context = {'items': items, 'order': order}
        
    return render(request, 'Shoppingcart/cart.html', context)

