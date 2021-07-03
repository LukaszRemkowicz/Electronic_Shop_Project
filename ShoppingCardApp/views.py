from django.shortcuts import render
from django.http import JsonResponse

import json

from ProductApp.models import MainProductDatabase 
from .models import Order, OrderItem

def address_checkout(request):
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else: 
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        
    context = {'items': items, 'order': order}
    
    return render(request,'Shoppingcart/address-checkout.html', context)

def update_item(request):
    data = json.loads(request.body)
    product_id = data['productId']
    action = data['action']
    
    customer = request.user.customer
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


def cart(request):
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else: 
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        
    context = {'items': items, 'order': order}
    
    return render(request, 'Shoppingcart/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else: 
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
     
    context = {'items': items, 'order': order}

    return render(request, 'Shoppingcart/cart.html', context)