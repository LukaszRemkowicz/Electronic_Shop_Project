from decimal import Decimal
from math import prod

from django.db.models.fields.files import FieldFile, ImageFieldFile
from django.forms.models import model_to_dict
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings

from ProductApp import models as product_app

User = settings.AUTH_USER_MODEL


def recurssive(product, new_dict):
    for key,value in product.items():
        if isinstance(value, ImageFieldFile) and value != '':
            new_dict[key] = str(value)
        elif isinstance(value, Decimal):
            new_dict[key] = float(value)
        elif isinstance(value, FieldFile):
            new_dict[key] = str(value)
        elif isinstance(value, dict):
            recurssive(value, new_dict)
        elif key == 'likes':
            pass
        else:
            new_dict[key] = value


    return new_dict

def change_model_to_dict(product_model):
    products_dict = {
                'phones_product_data' : lambda x: product_app.Phones.objects.get(id=x),
                'monitors_product_data' : lambda x: product_app.Monitors.objects.get(id=x),
                'laptops_product_data' : lambda x: product_app.Laptops.objects.get(id=x),
                'pc_product_data' : lambda x: product_app.Pc.objects.get(id=x),
                'accesories_for_laptop' : lambda x: product_app.AccesoriesForLaptops.objects.get(id=x),
                'ssd_product_data' : lambda x: product_app.Ssd.objects.get(id=x),
                'graph_product_data' : lambda x: product_app.Graphs.objects.get(id=x),
                'ram_product_data' : lambda x: product_app.Ram.objects.get(id=x),
                'pendrive_product_data' : lambda x: product_app.Pendrives.objects.get(id=x),
                'switch_product_data' : lambda x: product_app.Switches.objects.get(id=x),
                'motherboard_product_data' : lambda x: product_app.Motherboard.objects.get(id=x),
                'cpu_product_data' : lambda x: product_app.Cpu.objects.get(id=x),
                'tv_product_data' : lambda x: product_app.Tv.objects.get(id=x),
                'headphone_product_data' : lambda x: product_app.Headphones.objects.get(id=x),
                'router_product_data' : lambda x: product_app.Routers.objects.get(id=x),
            }

    product = model_to_dict(product_model)

    for key, value in products_dict.items():
        try:
            new_product_id = product[key]
            new_product = model_to_dict(value(new_product_id))
            product['main'] = new_product
        except ObjectDoesNotExist:
            pass


    new_dict = {}
    product = recurssive(product, new_dict)

    return product

