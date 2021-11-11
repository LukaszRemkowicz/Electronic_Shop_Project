from django.core.exceptions import ObjectDoesNotExist
from django.http.request import HttpRequest
from django.db.models.query import QuerySet

from ProductApp.models import *


def filter_tv_products(request: HttpRequest) -> QuerySet:
    """ Create queryset by user filters applied """

    filter = {
        'producent': lambda x, products: products.filter(producent=x),
        'smart': lambda x, products: products.filter(smart_tv=x),
        'curved': lambda x, products: products.filter(curved=x),

    }

    products = Tv.objects.all()

    url_queryset = { key:str(value[0]) for key, value in request.GET.lists()}

    for key, value in url_queryset.items():
        if key != 'page' and key != 'grid' and key != 'filter':
            try:
                existss = products.filter(**{'smart_tv':value}).exists()
                if key == 'smart' and existss:
                    products = filter[key](value, products)
                elif products.filter(**{key:value}).exists():
                    products = filter[key](value, products)
            except ObjectDoesNotExist:
                pass

    return products
