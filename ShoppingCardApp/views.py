from django.shortcuts import render
from django.http import HttpResponse

from .utils import cart_data


def address_checkout(request) -> HttpResponse:
    """ checkout order """

    items, order, address_list = cart_data(request)
    context = {'items': items, 'order': order, 'address_list': address_list}

    return render(request, 'ShoppingCardApp/address-checkout.html', context)


def cart(request) -> HttpResponse:
    """ Render cart template """

    items, order, address_list = cart_data(request)
    context = {'items': items, 'order': order}

    return render(request, 'ShoppingCardApp/cart.html', context)
