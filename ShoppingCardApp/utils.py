import json
from decimal import Decimal


from ProductApp.models import MainProductDatabase
from .models import Order, Customer, OrderItem
from AddressBookApp.models import AddressBook


def order_cart(request):
    
    try:
        cart = json.loads(request.COOKIES['cart'])['products']
    except:
        cart = {}
    
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


def cart_data(request):
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        address_list = AddressBook.objects.filter(user= request.user)
        
    else: 
        address_list = []
        items, order, cart_items = order_cart(request)
    
    return items, order, address_list


def complete_unauthorised_user_order(request, data):
    name = data['customerName']
    email = data['customerEmail']
    
    items, order, cart_items = order_cart(request)
        
    customer, created = Customer.objects.get_or_create(email=email)
    customer.name = name
    customer.save()
    
    order = Order.objects.create(
        customer = customer,
        complete = False,
    )
    
    for item in items:
        product = MainProductDatabase.objects.get(id=item['product']['id'])
        
        order_item = OrderItem.objects.create(
            product=product,
            order=order,
            quantity=item['quantity']
        )
    
    return customer, order
    
    
class DecimalEncoder(json.JSONEncoder):
    
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return json.JSONEncoder.default(self, obj)