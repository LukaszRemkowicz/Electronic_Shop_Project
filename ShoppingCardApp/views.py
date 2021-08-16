import json
import datetime

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.contrib import messages

from ProductApp.models import MainProductDatabase 
from .models import Customer, Order, OrderItem, ShippingAddress
from AddressBookApp.models import AddressBook


""" Creating cart items """

def order_cart(cart):
    
    items = []
    order = {'get_cart_total': 0, 'get_cart_items': 0}
    cart_items = order['get_cart_items']
    
    for item_id in cart:
            cart_items += cart[item_id]["quantity"]
            
            product = MainProductDatabase.objects.get(id=item_id)
            total = (product.price * cart[item_id]['quantity'])
            
            order['get_cart_total'] += total
            order['get_cart_items'] += cart[item_id]['quantity']
            
            item = {
                'product': {
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'get_img': product.get_img,
                    'cattegory': product.cattegory
                },
                'quantity': cart[item_id]['quantity'], 
                'get_total': total
            }
            
            
            items.append(item)
    
    return items, order, cart_items


""" Get data for unauthorised user """
def order_cart_unauthorised_user(request) -> JsonResponse:

    try:
        cart = json.loads(request.COOKIES['cart'])['products']
    except:
        cart = {}
        
    print('cart unauthorised: ', cart)
        
    items, order, cart_items = order_cart(cart)
        
    context = {'items': items, 'order': order}
    
    return JsonResponse(context, safe=False)

""" Finish order """

def order_finished(request) -> JsonResponse:
    
    data = json.loads(request.body)
    payment_method = data['payment']
    name = data['customerName']
    email = data['customerEmail']
    
    transaction_id = datetime.datetime.now().timestamp()
     
    if request.user.is_authenticated:
        customer = request.user.customer
    else:
        customer = Customer.objects.create(email=data['customerEmail'])
        
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    total = float(data['price']) 
    order.transaction_id = transaction_id 
    
    if total == float(order.get_cart_total):
        order.complete = True
    order.save()
    
    ShippingAddress.objects.create(
        customer = customer,
        order = order,
        address = data['customerStreet'],
        city = data['customerCity'],
        state = data['customerState'],
        zipcode = data['customerZipcode'], 
    )
        
    return JsonResponse('order saved.. ', safe=False)


""" checkout order """

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


""" Update item function """

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
    elif action == 'delete':
        orderItem.quantity = 0
        
    orderItem.save()
    
    if orderItem.quantity <= 0:
        orderItem.delete()
        
    data = {
        'items' : orderItem.quantity,
        'summaryItem': orderItem.get_total,
        'subtotal': order.get_cart_total,
        'totalItems': order.get_cart_items,
    }
        
    return JsonResponse(json.dumps(data),safe=False)


""" Render cart template """

def cart(request) -> HttpResponse:
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else: 
        
        try:
            cart = json.loads(request.COOKIES['cart'])['products']
        except:
            cart = {}
            
        items, order, cart_items = order_cart(cart)
        
    context = {'items': items, 'order': order}
        
    return render(request, 'Shoppingcart/cart.html', context)



# def checkout(request) -> HttpResponse:
    
#     if request.user.is_authenticated:
#         customer = request.user.customer
#         order, created = Order.objects.get_or_create(customer=customer, complete=False)
#         items = order.orderitem_set.all()
#     else: 
#         items = []
#         order = {'get_cart_total': 0, 'get_cart_items': 0}
     
#     context = {'items': items, 'order': order}

#     return render(request, 'Shoppingcart/cart.html', context)