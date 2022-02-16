from datetime import datetime, timedelta

from django import template
from django.core.exceptions import ObjectDoesNotExist

from ShoppingCardApp.models import OrderItem

register = template.Library()


@register.filter
def ennumerate_obj(obj):
    """ Create ennumerate obj to Boostrap Carusela """

    return [
        ('First' if num + 1 == 1 else
         'Second' if num + 1 == 2 else
         'Third', element) for num, element in enumerate(obj)
    ]


@register.filter
def format_datetime(value, new_date=''):
    """ Return date in proper way. Its used by JavaScript """

    try:
        if new_date:
            result = value - timedelta(days=int(new_date))
            result = result.strftime("%Y-%m-%d %H:%M:%S")
        else:
            result = value.strftime("%Y-%m-%d %H:%M:%S")

    except AttributeError:
        result = ''

    return result


@register.filter
def get_promotion_buy_num(product):
    order = OrderItem.objects.filter(
        order__transaction_status=True,
        product__ean=product.ean,
        order__date_order__gte=product.product_of_the_day_added
    )

    return len(order)


@register.filter
def check_orders(product):
    try:
        ordet_item_pieces = OrderItem.objects.get(
            order__transaction_status=False,
            product=product
        ).quantity
    except ObjectDoesNotExist:
        ordet_item_pieces = 0

    return product.pieces - ordet_item_pieces
