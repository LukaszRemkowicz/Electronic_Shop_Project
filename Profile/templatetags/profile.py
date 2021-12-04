from django import template
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from datetime import datetime

register = template.Library()

@register.filter
def ennumerate_obj(obj):
    """ Create ennumerate obj to Boostrap Carusela """

    return [
        ('First' if num+1 == 1 else
         'Second' if num+1 == 2 else
         'Third', element) for num, element in enumerate(obj)
            ]

@register.filter
def format_datetime(value):
    """ Return date in proper way. Its used by JavaScript """


    return value.strftime("%Y-%m-%d %H:%M:%S")
