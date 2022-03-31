import json
from decimal import Decimal
import logging

from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist

from ProductApp.models import MainProductDatabase
from .models import Order, Customer, OrderItem
from AddressBookApp.models import AddressBook


logger = logging.getLogger(f'project.{__name__}')


def order_cart(request):

    try:
        # new_request = request.COOKIES["cart"].replace("\'", "\"")
        cart = json.loads(request.COOKIES["cart"])["products"]
    except KeyError:
        cart = {}

    items = []
    order = {"get_cart_total": 0, "get_cart_items": 0}
    cart_items = order["get_cart_items"]

    for item_id in cart:

        cart_items += cart[item_id]["quantity"]

        try:

            product = MainProductDatabase.objects.get(id=item_id)
            total = product.price * cart[item_id]["quantity"]

            order["get_cart_total"] += total
            order["get_cart_items"] += cart[item_id]["quantity"]

            if product.main_photo == "" or not product.main_photo:
                photo = ""
            else:
                photo = product.get_img

            item = {
                "product": {
                    "id": product.id,
                    "name": product.name,
                    "price": product.price,
                    "get_img": photo,
                    "cattegory": product.cattegory,
                    "pieces": product.pieces,
                },
                "quantity": cart[item_id]["quantity"],
                "get_total": total,
            }

            items.append(item)

        except ObjectDoesNotExist:
            pass

    return items, order, cart_items


def cart_data(request):

    if request.user.is_authenticated:
        customer = Customer.objects.filter(user=request.user)
        if customer.exists():
            customer = customer[0]
        else:
            customer = Customer.objects.create(user=request.user)
        try:
            order, created = Order.objects.get_or_create(
                customer=customer, transaction_status=False
            )
        except MultipleObjectsReturned:
            order = Order.objects.filter(
                customer=customer, transaction_status=False
            ).order_by("-date_order")[0]
        items = order.orderitem_set.all()
        address_list = AddressBook.objects.filter(user=request.user)

    else:
        address_list = []
        items, order, cart_items = order_cart(request)

    return items, order, address_list


def complete_unauthorised_user_order(request, data):
    name = data["customerName"]
    email = data["customerEmail"]

    items, order, cart_items = order_cart(request)

    customer, created = Customer.objects.get_or_create(email=email)
    customer.name = name
    customer.save()

    order = Order.objects.create(
        customer=customer,
        transaction_status=False,
    )

    for item in items:
        product = MainProductDatabase.objects.get(id=item["product"]["id"])

        OrderItem.objects.create(
            product=product, order=order, quantity=item["quantity"]
        )

    return customer, order


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return json.JSONEncoder.default(self, obj)
