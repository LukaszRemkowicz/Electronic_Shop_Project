import json
import datetime

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.contrib import messages

from ProductApp.models import MainProductDatabase 
from .models import Customer, Order, OrderItem, ShippingAddress
from AddressBookApp.models import AddressBook

def order_finished(request) -> JsonResponse:
    
    
        
    return JsonResponse('order saved.. ', safe=False)

def address_checkout(request) -> HttpResponse:
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        address_list = AddressBook.objects.filter(user= request.user)
    else: 
        items = []
        address_list = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        
    context = {'items': items, 'order': order, 'address_list': address_list}
    
    return render(request,'Shoppingcart/address-checkout.html', context)

def update_item(request) -> JsonResponse:
    data = json.loads(request.body)
    product_id = data['productId']
    action = data['action']
    
    # customer = request.user.customer
    try:
        customer = request.user.customer
    except:
        customer = Customer.objects.create(user=request.user)
    product = MainProductDatabase.objects.get(id=product_id)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
        
    orderItem.save()
    
    if orderItem.quantity <= 0:
        orderItem.delete()
    
    return JsonResponse("item was added", safe=False)


def cart(request) -> HttpResponse:
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else: 
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        
    context = {'items': items, 'order': order}
    
    return render(request, 'Shoppingcart/cart.html', context)

def checkout(request) -> HttpResponse:
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else: 
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
     
    context = {'items': items, 'order': order}

    return render(request, 'Shoppingcart/cart.html', context)