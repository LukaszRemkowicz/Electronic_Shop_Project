from decimal import Decimal

from django.db.models.fields.files import FieldFile, ImageFieldFile



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
        else:
            new_dict[key] = value

    return new_dict
