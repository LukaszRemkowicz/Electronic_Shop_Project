from decimal import Decimal

from django.db.models.fields.files import FieldFile, ImageFieldFile

def recurssive(product):
    for key,value in product.items():
        if isinstance(value, ImageFieldFile):
            product[key] = ''
        if isinstance(value, Decimal):
            product[key] = float(value)
        if isinstance(value, FieldFile):
            product[key] = ''
        if isinstance(value, dict):
            recurssive(value)
    return product