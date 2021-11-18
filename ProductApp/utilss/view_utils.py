from math import prod
from django.core.exceptions import FieldDoesNotExist, FieldError, ObjectDoesNotExist
from django.http.request import HttpRequest
from django.db.models.query import QuerySet
from django.db.models import Q

from ProductApp.models import *


def filter_tv_products(request: HttpRequest) -> QuerySet:
    """ Create queryset by user filters applied """

    filter = {
        'producent': lambda x, products: products.filter(producent=x),
        'smart': lambda x, products: products.filter(smart_tv=x),
        'curved': lambda x, products: products.filter(curved=x),
        'refresh_rate': lambda x, products: products.filter(refresh_rate=x),
        'resolution': lambda x, products: products.filter(resolution=x),
        'matrix_type': lambda x, products: products.filter(matrix_type=x),
    }

    products = Tv.objects.all()

    url_queryset = { key:str(value[0]) for key, value in request.GET.lists() if key != 'page' and key != 'grid' and key != 'filter'}
    print(url_queryset)

    for key, value in url_queryset.items():
        try:
            if key == 'stars':
                products_list = [product.id for product in products if product.get_star_avg[0] == value]
                products = Tv.objects.filter(id__in=products_list)
            elif key == 'diagonal':
                if value == '70\' and more':
                    products = Tv.objects.filter(diagonal__gt=70)
                else:
                    value = value.replace('\'', '').split('-')
                    products = Tv.objects.filter(Q(diagonal__lt=value[1]), Q(diagonal__gt=value[0]))
            else:
                products = filter[key](value, products)
        except (FieldError, ObjectDoesNotExist, KeyError, FieldDoesNotExist) as e:
            print('Error in Tv function', e)


    return products

def filter_monitors_products(request: HttpRequest) -> QuerySet:
    """ Create queryset by user filters applied """

    filter = {
        'producent': lambda x, products: products.filter(producent=x),
        'resolution': lambda x, products: products.filter(resolution=x),
        'screen': lambda x, products: products.filter(screen=x),
        'matrix_type': lambda x, products: products.filter(matrix_type=x),
        'curved': lambda x, products: products.filter(curved=x),
        'format': lambda x, products: products.filter(format=x),
        'refresh_rate': lambda x, products: products.filter(refresh_rate=x),
    }

    products = Monitors.objects.all()

    url_queryset = { key:str(value[0]) for key, value in request.GET.lists() if key != 'page' and key != 'grid' and key != 'filter'}

    for key, value in url_queryset.items():
        try:
            if key == 'stars':
                products_list = [product.id for product in products if product.get_star_avg[0] == value]
                products = Monitors.objects.filter(id__in=products_list)
            elif key == 'diagonal':
                value = value.replace('\'', '').split('-')
                products = Monitors.objects.filter(Q(diagonal__lt=value[1]), Q(diagonal__gt=value[0]))
            else:
                products = filter[key](value, products)
        except (FieldError, ObjectDoesNotExist, KeyError, FieldDoesNotExist) as e:
            print('Error in Monitors function', e)

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

    url_queryset = { key:str(value[0]) for key, value in request.GET.lists() if key != 'page' and key != 'grid' and key != 'filter'}

    for key, value in url_queryset.items():
        try:
            if key == 'stars':
                products_list = [product.id for product in products if product.get_star_avg[0] == value]
                products = Pc.objects.filter(id__in=products_list)
            else:
                products = filter[key](value, products)
        except (FieldError, ObjectDoesNotExist, KeyError, FieldDoesNotExist) as e:
            print('Error in Pcs function', e)

    return products

def filter_ssd_products(request: HttpRequest) -> QuerySet:
    """ Create queryset by user filters applied """

    filter = {
        'producent': lambda x, products: products.filter(producent=x),
        'format': lambda x, products: products.filter(format=x),
        'capacity': lambda x, products: products.filter(capacity=x),
        'reading_speed': lambda x, products: products.filter(reading_speed=x),
        'writing_speed': lambda x, products: products.filter(writing_speed=x),
        'life_time': lambda x, products: products.filter(life_time=x),
    }

    products = Ssd.objects.all()

    url_queryset = { key:str(value[0]) for key, value in request.GET.lists() if key != 'page' and key != 'grid' and key != 'filter'}

    for key, value in url_queryset.items():
        print(products)
        try:
            if key == 'stars':
                products_list = [product.id for product in products if product.get_star_avg[0] == value]
                products = Ssd.objects.filter(id__in=products_list)
            else:
                products = filter[key](value, products)
        except (FieldError, ObjectDoesNotExist, KeyError, FieldDoesNotExist) as e:
            print('Error in Ssds function', e)

    return products

def filter_graphs_products(request: HttpRequest) -> QuerySet:
    """ Create queryset by user filters applied """

    filter = {
        'producent': lambda x, products: products.filter(producent=x),
        'chipset': lambda x, products: products.filter(chipset=x),
        'chipset_producent': lambda x, products: products.filter(chipset_producent=x),
        'ram': lambda x, products: products.filter(ram=x),
        'ram_type': lambda x, products: products.filter(ram_type=x),
        'connector_type': lambda x, products: products.filter(connector_type=x),
    }

    products = Graphs.objects.all()

    url_queryset = { key:str(value[0]) for key, value in request.GET.lists() if key != 'page' and key != 'grid' and key != 'filter'}

    for key, value in url_queryset.items():
        print(products)
        try:
            if key == 'stars':
                products_list = [product.id for product in products if product.get_star_avg[0] == value]
                products = Graphs.objects.filter(id__in=products_list)
            else:
                products = filter[key](value, products)
        except (FieldError, ObjectDoesNotExist, KeyError, FieldDoesNotExist) as e:
            print('Error in Graphs function', e)

    return products


def filter_rams_products(request: HttpRequest) -> QuerySet:
    """ Create queryset by user filters applied """

    filter = {
        'producent': lambda x, products: products.filter(producent=x),
        'capacity': lambda x, products: products.filter(capacity=x),
        'frequency': lambda x, products: products.filter(frequency=x),
        'modules_number': lambda x, products: products.filter(modules_number=x),
        'delay': lambda x, products: products.filter(delay=x),
        'voltage': lambda x, products: products.filter(voltage=x),
        'type': lambda x, products: products.filter(type=x),
    }

    products = Ram.objects.all()

    url_queryset = { key:str(value[0]) for key, value in request.GET.lists() if key != 'page' and key != 'grid' and key != 'filter'}

    for key, value in url_queryset.items():
        print(products)
        try:
            if key == 'stars':
                products_list = [product.id for product in products if product.get_star_avg[0] == value]
                products = Ram.objects.filter(id__in=products_list)
            else:
                products = filter[key](value, products)
        except (FieldError, ObjectDoesNotExist, KeyError, FieldDoesNotExist) as e:
            print('Error in ram function', e)

    return products


def filter_pendrives_products(request: HttpRequest) -> QuerySet:
    """ Create queryset by user filters applied """

    filter = {
        'producent': lambda x, products: products.filter(producent=x),
        'capacity': lambda x, products: products.filter(capacity=x),
    }

    products = Pendrives.objects.all()

    url_queryset = { key:str(value[0]) for key, value in request.GET.lists() if key != 'page' and key != 'grid' and key != 'filter'}

    for key, value in url_queryset.items():
        print(products)
        try:
            if key == 'stars':
                products_list = [product.id for product in products if product.get_star_avg[0] == value]
                products = Pendrives.objects.filter(id__in=products_list)
            else:
                products = filter[key](value, products)
        except (FieldError, ObjectDoesNotExist, KeyError, FieldDoesNotExist) as e:
            print('Error in Pendrives function', e)

    return products


def filter_switches_products(request: HttpRequest) -> QuerySet:
    """ Create queryset by user filters applied """

    filter = {
        'producent': lambda x, products: products.filter(producent=x),
        'num_of_poe': lambda x, products: products.filter(num_of_poe=x),
        'case_kind': lambda x, products: products.filter(case_kind=x),
        'manageable': lambda x, products: products.filter(manageable=x),
    }

    products = Switches.objects.all()

    url_queryset = { key:str(value[0]) for key, value in request.GET.lists() if key != 'page' and key != 'grid' and key != 'filter'}

    for key, value in url_queryset.items():
        print(key, type(value))
        try:
            if key == 'stars':
                products_list = [product.id for product in products if product.get_star_avg[0] == value]
                products = Switches.objects.filter(id__in=products_list)
            else:
                products = filter[key](value, products)
        except (FieldError, ObjectDoesNotExist, KeyError, FieldDoesNotExist) as e:
            print('Error in Switches function', e)

    return products


def filter_motherboard_products(request: HttpRequest) -> QuerySet:
    """ Create queryset by user filters applied """

    filter = {
        'producent': lambda x, products: products.filter(producent=x),
        'chipset': lambda x, products: products.filter(chipset=x),
        'processor_socket': lambda x, products: products.filter(processor_socket=x),
        'ram_slots': lambda x, products: products.filter(ram_slots=x),
        'card_standard': lambda x, products: products.filter(card_standard=x),
        'raid_controler': lambda x, products: products.filter(raid_controler=x),
        'ram': lambda x, products: products.filter(ram=x),
        'wifi': lambda x, products: products.filter(wifi=x),
    }

    products = Motherboard.objects.all()

    url_queryset = { key:str(value[0]) for key, value in request.GET.lists() if key != 'page' and key != 'grid' and key != 'filter'}

    for key, value in url_queryset.items():
        print(products)
        try:
            if key == 'stars':
                products_list = [product.id for product in products if product.get_star_avg[0] == value]
                products = Motherboard.objects.filter(id__in=products_list)
            else:
                products = filter[key](value, products)
        except (FieldError, ObjectDoesNotExist, KeyError, FieldDoesNotExist) as e:
            print('Error in Motherboard function', e)

    return products

def filter_cpus_products(request: HttpRequest) -> QuerySet:
    """ Create queryset by user filters applied """

    filter = {
        'producent': lambda x, products: products.filter(producent=x),
        'cooler': lambda x, products: products.filter(cooler=x),
        'socket': lambda x, products: products.filter(socket=x),
        'cores_num': lambda x, products: products.filter(cores_num=x),
        'threat_num': lambda x, products: products.filter(threat_num=x),
        'clock_frequency': lambda x, products: products.filter(clock_frequency=x),
        'supported_memory': lambda x, products: products.filter(ram=x),
    }

    products = Cpu.objects.all()

    url_queryset = { key:str(value[0]) for key, value in request.GET.lists() if key != 'page' and key != 'grid' and key != 'filter'}

    for key, value in url_queryset.items():
        print(products)
        try:
            if key == 'stars':
                products_list = [product.id for product in products if product.get_star_avg[0] == value]
                products = Cpu.objects.filter(id__in=products_list)
            else:
                products = filter[key](value, products)
        except (FieldError, ObjectDoesNotExist, KeyError, FieldDoesNotExist) as e:
            print('Error in Cpu function', e)

    return products

def filter_headphones_products(request: HttpRequest) -> QuerySet:
    """ Create queryset by user filters applied """

    filter = {
        'producent': lambda x, products: products.filter(producent=x),
        'connection': lambda x, products: products.filter(connection=x),
    }

    products = Headphones.objects.all()

    url_queryset = { key:str(value[0]) for key, value in request.GET.lists() if key != 'page' and key != 'grid' and key != 'filter'}

    for key, value in url_queryset.items():
        print(products)
        try:
            if key == 'stars':
                products_list = [product.id for product in products if product.get_star_avg[0] == value]
                products = Headphones.objects.filter(id__in=products_list)
            else:
                products = filter[key](value, products)
        except (FieldError, ObjectDoesNotExist, KeyError, FieldDoesNotExist) as e:
            print('Error in Headphones function', e)

    return products

def filter_routers_products(request: HttpRequest) -> QuerySet:
    """ Create queryset by user filters applied """

    filter = {
        'producent': lambda x, products: products.filter(producent=x),
        'wifi': lambda x, products: products.filter(wifi=x),
        'lan_ports': lambda x, products: products.filter(lan_ports=x),
        'wan_ports': lambda x, products: products.filter(wan_ports=x),
        'case': lambda x, products: products.filter(case=x),
        'usb_ports': lambda x, products: products.filter(usb_ports=x),
        'sim': lambda x, products: products.filter(sim=x),
    }

    products = Routers.objects.all()

    url_queryset = { key:str(value[0]) for key, value in request.GET.lists() if key != 'page' and key != 'grid' and key != 'filter'}

    for key, value in url_queryset.items():
        print(key)
        try:
            if key == 'stars':
                products_list = [product.id for product in products if product.get_star_avg[0] == value]
                products = Routers.objects.filter(id__in=products_list)
            elif key == 'lan_ports' and value == 'No LAN ports':
                products = products.filter(lan_ports='')
            elif key == 'wan_ports' and value == 'No WAN ports':
                products = products.filter(wan_ports='')
            elif key == 'wifi' and value == 'No WiFi':
                products = products.filter(wifi='')
            else:
                products = filter[key](value, products)
        except (FieldError, ObjectDoesNotExist, KeyError, FieldDoesNotExist) as e:
            print('Error in Routers function', e)

    return products

def filter_laptops_products(request: HttpRequest) -> QuerySet:
    """ Create queryset by user filters applied """

    filter = {
        'producent': lambda x, products: products.filter(producent=x),
        'resolution': lambda x, products: products.filter(resolution=x),
        'diagonal': lambda x, products: products.filter(diagonal=x),
        'bluetooth': lambda x, products: products.filter(bluetooth=x),
        'screen': lambda x, products: products.filter(screen=x),
        'system': lambda x, products: products.filter(system=x),
        'graph': lambda x, products: products.filter(graph=x),
        'ram_freq': lambda x, products: products.filter(ram_freq=x),
        'ram': lambda x, products: products.filter(ram=x),
        'ram_model': lambda x, products: products.filter(ram_model=x),
        'pcie': lambda x, products: products.filter(pcie=x),
        'processor': lambda x, products: products.filter(processor=x),
        'processor_clock': lambda x, products: products.filter(processor_clock=x),
        'processor_cores_threads': lambda x, products: products.filter(processor_cores_threads=x),
    }

    products = Laptops.objects.all()

    url_queryset = { key:str(value[0]) for key, value in request.GET.lists() if key != 'page' and key != 'grid' and key != 'filter'}

    for key, value in url_queryset.items():
        print(key, value)
        try:
            if key == 'stars':
                products_list = [product.id for product in products if product.get_star_avg[0] == value]
                products = Laptops.objects.filter(id__in=products_list)
            else:
                products = filter[key](value, products)
        except (FieldError, ObjectDoesNotExist, KeyError, FieldDoesNotExist) as e:
            print('Error in Laptops function', e)

    return products

def filter_phones_products(request: HttpRequest) -> QuerySet:
    """ Create queryset by user filters applied """

    filter = {
        'producent': lambda x, products: products.filter(producent=x),
        'battery': lambda x, products: products.filter(battery=x),
        'diagonal': lambda x, products: products.filter(diagonal=x),
        'waterproof': lambda x, products: products.filter(waterproof=x),
        'screen': lambda x, products: products.filter(screen=x),
        'memory_card': lambda x, products: products.filter(memory_card=x),
        'memory': lambda x, products: products.filter(memory=x),
        'ram': lambda x, products: products.filter(ram=x),
        'processor': lambda x, products: products.filter(processor=x),
        'system': lambda x, products: products.filter(system=x),
        'cpu_clock': lambda x, products: products.filter(cpu_clock=x),
    }

    products = Phones.objects.all()

    url_queryset = { key:str(value[0]) for key, value in request.GET.lists() if key != 'page' and key != 'grid' and key != 'filter'}

    for key, value in url_queryset.items():
        print(key, value)
        try:
            if key == 'stars':
                products_list = [product.id for product in products if product.get_star_avg[0] == value]
                products = Phones.objects.filter(id__in=products_list)
            else:
                products = filter[key](value, products)
        except (FieldError, ObjectDoesNotExist, KeyError, FieldDoesNotExist) as e:
            print('Error in Phones function', e)

    return products