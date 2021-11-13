from django.core.exceptions import FieldDoesNotExist, FieldError, ObjectDoesNotExist
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
                    if value == 'Yes':
                        products = filter[key](value, products)
                if key == 'curved' and value != 'True':
                    pass
                elif products.filter(**{key:value}).exists():
                    products = filter[key](value, products)
            except (FieldError, ObjectDoesNotExist, KeyError, FieldDoesNotExist) as e:
                pass

    return products

def filter_monitors_products(request: HttpRequest) -> QuerySet:
    """ Create queryset by user filters applied """

    filter = {
        'producent': lambda x, products: products.filter(producent=x),
        'resolution': lambda x, products: products.filter(resolution=x),
        'diagonal': lambda x, products: products.filter(diagonal=x),
        'screen': lambda x, products: products.filter(screen=x),
        'matrix_type': lambda x, products: products.filter(matrix_type=x),
        'curved': lambda x, products: products.filter(curved=x),
        'format': lambda x, products: products.filter(format=x),
        'refresh_rate': lambda x, products: products.filter(refresh_rate=x),
    }

    products = Monitors.objects.all()

    url_queryset = { key:str(value[0]) for key, value in request.GET.lists()}

    for key, value in url_queryset.items():
        if key != 'page' and key != 'grid' and key != 'filter':
            if key == 'curved' and value != 'Yes':
                pass
            else:
                try:
                    if products.filter(**{key:value}).exists():
                        products = filter[key](value, products)
                except (FieldError, ObjectDoesNotExist, KeyError, FieldDoesNotExist) as e:
                    print('Error in filter_monitors_products function', e)
    return products


def filter_pcs_products(request: HttpRequest) -> QuerySet:
    """ Create queryset by user filters applied """

    filter = {
        'producent': lambda x, products: products.filter(producent=x),
        'processor': lambda x, products: products.filter(processor=x),
        'socket': lambda x, products: products.filter(socket=x),
        'system': lambda x, products: products.filter(system=x),
        'motherboard_chipset': lambda x, products: products.filter(motherboard_chipset=x),
        'disc': lambda x, products: products.filter(disc=x),
        'ram': lambda x, products: products.filter(ram=x),
        'ram_type': lambda x, products: products.filter(ram_type=x),
        'p_c_i_e': lambda x, products: products.filter(p_c_i_e=x),
        'bluetooth': lambda x, products: products.filter(bluetooth=x),
    }

    products = Pc.objects.all()

    url_queryset = { key:str(value[0]) for key, value in request.GET.lists()}

    # for key, value in url_queryset.items():
    #     if key != 'page' and key != 'grid' and key != 'filter':
    #         if key == 'curved' and value != 'Yes':
    #             pass
    #         else:
    #             try:
    #                 if products.filter(**{key:value}).exists():
    #                     products = filter[key](value, products)
    #             except (FieldError, ObjectDoesNotExist, KeyError, FieldDoesNotExist) as e:
    #                 pass

    return products

def filter_ssd_products(request: HttpRequest) -> QuerySet:
    """ Create queryset by user filters applied """

    filter = {
        'producent': lambda x, products: products.filter(producent=x),
        'processor': lambda x, products: products.filter(processor=x),
        'socket': lambda x, products: products.filter(socket=x),
        'system': lambda x, products: products.filter(system=x),
        'motherboard_chipset': lambda x, products: products.filter(motherboard_chipset=x),
        'disc': lambda x, products: products.filter(disc=x),
        'ram': lambda x, products: products.filter(ram=x),
        'ram_type': lambda x, products: products.filter(ram_type=x),
        'p_c_i_e': lambda x, products: products.filter(p_c_i_e=x),
        'bluetooth': lambda x, products: products.filter(bluetooth=x),
    }

    products = Ssd.objects.all()

    url_queryset = { key:str(value[0]) for key, value in request.GET.lists()}

    # for key, value in url_queryset.items():
    #     if key != 'page' and key != 'grid' and key != 'filter':
    #         if key == 'curved' and value != 'Yes':
    #             pass
    #         else:
    #             try:
    #                 if products.filter(**{key:value}).exists():
    #                     products = filter[key](value, products)
    #             except (FieldError, ObjectDoesNotExist, KeyError, FieldDoesNotExist) as e:
    #                 pass

    return products

def filter_graphs_products(request: HttpRequest) -> QuerySet:
    """ Create queryset by user filters applied """

    filter = {
        'producent': lambda x, products: products.filter(producent=x),
        'processor': lambda x, products: products.filter(processor=x),
        'socket': lambda x, products: products.filter(socket=x),
        'system': lambda x, products: products.filter(system=x),
        'motherboard_chipset': lambda x, products: products.filter(motherboard_chipset=x),
        'disc': lambda x, products: products.filter(disc=x),
        'ram': lambda x, products: products.filter(ram=x),
        'ram_type': lambda x, products: products.filter(ram_type=x),
        'p_c_i_e': lambda x, products: products.filter(p_c_i_e=x),
        'bluetooth': lambda x, products: products.filter(bluetooth=x),
    }

    products = Graphs.objects.all()

    url_queryset = { key:str(value[0]) for key, value in request.GET.lists()}

    # for key, value in url_queryset.items():
    #     if key != 'page' and key != 'grid' and key != 'filter':
    #         if key == 'curved' and value != 'Yes':
    #             pass
    #         else:
    #             try:
    #                 if products.filter(**{key:value}).exists():
    #                     products = filter[key](value, products)
    #             except (FieldError, ObjectDoesNotExist, KeyError, FieldDoesNotExist) as e:
    #                 pass

    return products


def filter_rams_products(request: HttpRequest) -> QuerySet:
    """ Create queryset by user filters applied """

    filter = {
        'producent': lambda x, products: products.filter(producent=x),
        'processor': lambda x, products: products.filter(processor=x),
        'socket': lambda x, products: products.filter(socket=x),
        'system': lambda x, products: products.filter(system=x),
        'motherboard_chipset': lambda x, products: products.filter(motherboard_chipset=x),
        'disc': lambda x, products: products.filter(disc=x),
        'ram': lambda x, products: products.filter(ram=x),
        'ram_type': lambda x, products: products.filter(ram_type=x),
        'p_c_i_e': lambda x, products: products.filter(p_c_i_e=x),
        'bluetooth': lambda x, products: products.filter(bluetooth=x),
    }

    products = Ram.objects.all()

    url_queryset = { key:str(value[0]) for key, value in request.GET.lists()}

    # for key, value in url_queryset.items():
    #     if key != 'page' and key != 'grid' and key != 'filter':
    #         if key == 'curved' and value != 'Yes':
    #             pass
    #         else:
    #             try:
    #                 if products.filter(**{key:value}).exists():
    #                     products = filter[key](value, products)
    #             except (FieldError, ObjectDoesNotExist, KeyError, FieldDoesNotExist) as e:
    #                 pass

    return products


def filter_pendrives_products(request: HttpRequest) -> QuerySet:
    """ Create queryset by user filters applied """

    filter = {
        'producent': lambda x, products: products.filter(producent=x),
        'processor': lambda x, products: products.filter(processor=x),
        'socket': lambda x, products: products.filter(socket=x),
        'system': lambda x, products: products.filter(system=x),
        'motherboard_chipset': lambda x, products: products.filter(motherboard_chipset=x),
        'disc': lambda x, products: products.filter(disc=x),
        'ram': lambda x, products: products.filter(ram=x),
        'ram_type': lambda x, products: products.filter(ram_type=x),
        'p_c_i_e': lambda x, products: products.filter(p_c_i_e=x),
        'bluetooth': lambda x, products: products.filter(bluetooth=x),
    }

    products = Pendrives.objects.all()

    url_queryset = { key:str(value[0]) for key, value in request.GET.lists()}

    # for key, value in url_queryset.items():
    #     if key != 'page' and key != 'grid' and key != 'filter':
    #         if key == 'curved' and value != 'Yes':
    #             pass
    #         else:
    #             try:
    #                 if products.filter(**{key:value}).exists():
    #                     products = filter[key](value, products)
    #             except (FieldError, ObjectDoesNotExist, KeyError, FieldDoesNotExist) as e:
    #                 pass

    return products


def filter_switches_products(request: HttpRequest) -> QuerySet:
    """ Create queryset by user filters applied """

    filter = {
        'producent': lambda x, products: products.filter(producent=x),
        'processor': lambda x, products: products.filter(processor=x),
        'socket': lambda x, products: products.filter(socket=x),
        'system': lambda x, products: products.filter(system=x),
        'motherboard_chipset': lambda x, products: products.filter(motherboard_chipset=x),
        'disc': lambda x, products: products.filter(disc=x),
        'ram': lambda x, products: products.filter(ram=x),
        'ram_type': lambda x, products: products.filter(ram_type=x),
        'p_c_i_e': lambda x, products: products.filter(p_c_i_e=x),
        'bluetooth': lambda x, products: products.filter(bluetooth=x),
    }

    products = Switches.objects.all()

    url_queryset = { key:str(value[0]) for key, value in request.GET.lists()}

    # for key, value in url_queryset.items():
    #     if key != 'page' and key != 'grid' and key != 'filter':
    #         if key == 'curved' and value != 'Yes':
    #             pass
    #         else:
    #             try:
    #                 if products.filter(**{key:value}).exists():
    #                     products = filter[key](value, products)
    #             except (FieldError, ObjectDoesNotExist, KeyError, FieldDoesNotExist) as e:
    #                 pass

    return products


def filter_motherboard_products(request: HttpRequest) -> QuerySet:
    """ Create queryset by user filters applied """

    filter = {
        'producent': lambda x, products: products.filter(producent=x),
        'processor': lambda x, products: products.filter(processor=x),
        'socket': lambda x, products: products.filter(socket=x),
        'system': lambda x, products: products.filter(system=x),
        'motherboard_chipset': lambda x, products: products.filter(motherboard_chipset=x),
        'disc': lambda x, products: products.filter(disc=x),
        'ram': lambda x, products: products.filter(ram=x),
        'ram_type': lambda x, products: products.filter(ram_type=x),
        'p_c_i_e': lambda x, products: products.filter(p_c_i_e=x),
        'bluetooth': lambda x, products: products.filter(bluetooth=x),
    }

    products = Motherboard.objects.all()

    url_queryset = { key:str(value[0]) for key, value in request.GET.lists()}

    # for key, value in url_queryset.items():
    #     if key != 'page' and key != 'grid' and key != 'filter':
    #         if key == 'curved' and value != 'Yes':
    #             pass
    #         else:
    #             try:
    #                 if products.filter(**{key:value}).exists():
    #                     products = filter[key](value, products)
    #             except (FieldError, ObjectDoesNotExist, KeyError, FieldDoesNotExist) as e:
    #                 pass

    return products

def filter_cpus_products(request: HttpRequest) -> QuerySet:
    """ Create queryset by user filters applied """

    filter = {
        'producent': lambda x, products: products.filter(producent=x),
        'processor': lambda x, products: products.filter(processor=x),
        'socket': lambda x, products: products.filter(socket=x),
        'system': lambda x, products: products.filter(system=x),
        'motherboard_chipset': lambda x, products: products.filter(motherboard_chipset=x),
        'disc': lambda x, products: products.filter(disc=x),
        'ram': lambda x, products: products.filter(ram=x),
        'ram_type': lambda x, products: products.filter(ram_type=x),
        'p_c_i_e': lambda x, products: products.filter(p_c_i_e=x),
        'bluetooth': lambda x, products: products.filter(bluetooth=x),
    }

    products = Cpu.objects.all()

    url_queryset = { key:str(value[0]) for key, value in request.GET.lists()}

    # for key, value in url_queryset.items():
    #     if key != 'page' and key != 'grid' and key != 'filter':
    #         if key == 'curved' and value != 'Yes':
    #             pass
    #         else:
    #             try:
    #                 if products.filter(**{key:value}).exists():
    #                     products = filter[key](value, products)
    #             except (FieldError, ObjectDoesNotExist, KeyError, FieldDoesNotExist) as e:
    #                 pass

    return products

def filter_headphones_products(request: HttpRequest) -> QuerySet:
    """ Create queryset by user filters applied """

    filter = {
        'producent': lambda x, products: products.filter(producent=x),
        'processor': lambda x, products: products.filter(processor=x),
        'socket': lambda x, products: products.filter(socket=x),
        'system': lambda x, products: products.filter(system=x),
        'motherboard_chipset': lambda x, products: products.filter(motherboard_chipset=x),
        'disc': lambda x, products: products.filter(disc=x),
        'ram': lambda x, products: products.filter(ram=x),
        'ram_type': lambda x, products: products.filter(ram_type=x),
        'p_c_i_e': lambda x, products: products.filter(p_c_i_e=x),
        'bluetooth': lambda x, products: products.filter(bluetooth=x),
    }

    products = Headphones.objects.all()

    url_queryset = { key:str(value[0]) for key, value in request.GET.lists()}

    # for key, value in url_queryset.items():
    #     if key != 'page' and key != 'grid' and key != 'filter':
    #         if key == 'curved' and value != 'Yes':
    #             pass
    #         else:
    #             try:
    #                 if products.filter(**{key:value}).exists():
    #                     products = filter[key](value, products)
    #             except (FieldError, ObjectDoesNotExist, KeyError, FieldDoesNotExist) as e:
    #                 pass

    return products

def filter_routers_products(request: HttpRequest) -> QuerySet:
    """ Create queryset by user filters applied """

    filter = {
        'producent': lambda x, products: products.filter(producent=x),
        'processor': lambda x, products: products.filter(processor=x),
        'socket': lambda x, products: products.filter(socket=x),
        'system': lambda x, products: products.filter(system=x),
        'motherboard_chipset': lambda x, products: products.filter(motherboard_chipset=x),
        'disc': lambda x, products: products.filter(disc=x),
        'ram': lambda x, products: products.filter(ram=x),
        'ram_type': lambda x, products: products.filter(ram_type=x),
        'p_c_i_e': lambda x, products: products.filter(p_c_i_e=x),
        'bluetooth': lambda x, products: products.filter(bluetooth=x),
    }

    products = Routers.objects.all()

    url_queryset = { key:str(value[0]) for key, value in request.GET.lists()}

    # for key, value in url_queryset.items():
    #     if key != 'page' and key != 'grid' and key != 'filter':
    #         if key == 'curved' and value != 'Yes':
    #             pass
    #         else:
    #             try:
    #                 if products.filter(**{key:value}).exists():
    #                     products = filter[key](value, products)
    #             except (FieldError, ObjectDoesNotExist, KeyError, FieldDoesNotExist) as e:
    #                 pass

    return products

def filter_laptops_products(request: HttpRequest) -> QuerySet:
    """ Create queryset by user filters applied """

    filter = {
        'producent': lambda x, products: products.filter(producent=x),
        'processor': lambda x, products: products.filter(processor=x),
        'socket': lambda x, products: products.filter(socket=x),
        'system': lambda x, products: products.filter(system=x),
        'motherboard_chipset': lambda x, products: products.filter(motherboard_chipset=x),
        'disc': lambda x, products: products.filter(disc=x),
        'ram': lambda x, products: products.filter(ram=x),
        'ram_type': lambda x, products: products.filter(ram_type=x),
        'p_c_i_e': lambda x, products: products.filter(p_c_i_e=x),
        'bluetooth': lambda x, products: products.filter(bluetooth=x),
    }

    products = Laptops.objects.all()

    url_queryset = { key:str(value[0]) for key, value in request.GET.lists()}

    # for key, value in url_queryset.items():
    #     if key != 'page' and key != 'grid' and key != 'filter':
    #         if key == 'curved' and value != 'Yes':
    #             pass
    #         else:
    #             try:
    #                 if products.filter(**{key:value}).exists():
    #                     products = filter[key](value, products)
    #             except (FieldError, ObjectDoesNotExist, KeyError, FieldDoesNotExist) as e:
    #                 pass

    return products

def filter_phones_products(request: HttpRequest) -> QuerySet:
    """ Create queryset by user filters applied """

    filter = {
        'producent': lambda x, products: products.filter(producent=x),
        'processor': lambda x, products: products.filter(processor=x),
        'socket': lambda x, products: products.filter(socket=x),
        'system': lambda x, products: products.filter(system=x),
        'motherboard_chipset': lambda x, products: products.filter(motherboard_chipset=x),
        'disc': lambda x, products: products.filter(disc=x),
        'ram': lambda x, products: products.filter(ram=x),
        'ram_type': lambda x, products: products.filter(ram_type=x),
        'p_c_i_e': lambda x, products: products.filter(p_c_i_e=x),
        'bluetooth': lambda x, products: products.filter(bluetooth=x),
    }

    products = Phones.objects.all()

    url_queryset = { key:str(value[0]) for key, value in request.GET.lists()}

    # for key, value in url_queryset.items():
    #     if key != 'page' and key != 'grid' and key != 'filter':
    #         if key == 'curved' and value != 'Yes':
    #             pass
    #         else:
    #             try:
    #                 if products.filter(**{key:value}).exists():
    #                     products = filter[key](value, products)
    #             except (FieldError, ObjectDoesNotExist, KeyError, FieldDoesNotExist) as e:
    #                 pass

    return products