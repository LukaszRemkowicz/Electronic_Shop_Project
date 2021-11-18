from re import T
from django import template

from ProductApp.models import MainProductDatabase

register = template.Library()


def search_for_url(url: str, param: str, what_to_lf: str) -> bool:
    if param in url:
        for element in url.split('&'):
            if param in element:
                element = element.split(f'{param}=')
                try:
                    boolean = element[1]
                    if boolean == what_to_lf:
                        return True
                except Exception:
                    return False
        return False
    else:
        return False


@register.filter
def find_producent(url: str) -> str:
    url = url.split('&')
    for urll in url:
        if 'producent=' in urll:
            return urll.split('producent=')[1]

@register.filter
def find_grid (url: str) -> bool:
    return search_for_url(url, 'grid', 'true')


@register.filter
def get_attr(dictionary: dict, name: str) -> str:
    return dictionary.get(name)


@register.filter
def check_curved(url: str) -> bool:
    return search_for_url(url, 'curved', 'Yes')


@register.filter
def check_smart(url: str) -> bool:
    return search_for_url(url, 'smart', 'Yes')


@register.filter
def get_main_product_id (product):

    product = MainProductDatabase.objects.get(ean=product.ean)
    return product.id

@register.filter
def get_aplied_filters(request):
    url_queryset = { key:str(value[0]) for key, value in request.GET.lists()}
    result = {key.replace('_', ' ') for key, _ in url_queryset.items() if key not in ('page', 'grid', 'filter')}

    if 'filter' in url_queryset:
        result.add(url_queryset['filter'])
    return result

@register.filter
def check_like(product, request):
    product = MainProductDatabase.objects.get(ean=product.ean)
    many_to_many = [user for user in product.likes.all() if user == request.user]
    if len(many_to_many) >= 1:
        return True
    else:
        return False
