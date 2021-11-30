from django import template
from django.db.models.query import QuerySet
from django.http.request import HttpRequest


register = template.Library()

@register.filter
def ennumerate_obj(obj):
    print(obj)
    return [
        ('First' if num+1 == 1 else
         'Second' if num+1 == 2 else
         'Third', element) for num, element in enumerate(obj)
            ]