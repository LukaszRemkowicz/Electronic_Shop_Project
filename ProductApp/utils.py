from typing import Dict, List, Any

from django.core.exceptions import ObjectDoesNotExist
from django.db.models.query import QuerySet
from django.forms.models import model_to_dict
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpRequest, HttpResponse


from ProductApp import models


#TODO: Functions must be refactored

def check_no_data(obj: Any) -> Any:
    """ Filter to find out if there is 'No data' value """
    return [element for element in obj if element != 'No data']


def filter_products(cattegory: str, product: models.MainProductDatabase) -> Dict:

    if cattegory == 'Phones':
        product_model = product.phones_product_data.model
        same_products = models.MainProductDatabase.objects.filter(phones_product_data__model=product_model)[:4]
        same_products_data = {
            'items' : same_products,
            'colors' : check_no_data({element.phones_product_data.color for element in same_products}),
            'memory' : check_no_data({element.phones_product_data.memory for element in same_products}),
            'ram' : check_no_data({element.phones_product_data.ram for element in same_products}),
            'battery' : check_no_data({element.phones_product_data.battery for element in same_products}),
            'items_id' : [element.id for element in same_products]
        }
        # print(same_products_data)
        return same_products_data

    elif cattegory == 'Laptops':

        product_model = product.laptops_product_data.model
        same_products = models.MainProductDatabase.objects.filter(laptops_product_data__model=product_model)
        same_products_data = {
            'items' : same_products,
            'p_c_i_e' : check_no_data({element.laptops_product_data.p_c_i_e for element in same_products}),
            'ram' : check_no_data({element.laptops_product_data.ram for element in same_products}),
            'system' : check_no_data({element.laptops_product_data.system for element in same_products}),
            'processor' : check_no_data({element.laptops_product_data.processor for element in same_products}),
            'items_id' : [element.id for element in same_products]
        }
        if product.laptops_product_data.producent == 'Apple':
            same_products_data['colors'] = {element.laptops_product_data.color for element in same_products}
            same_products_data['system'] = ''
            same_products_data['processor'] = ''

        return same_products_data

    elif cattegory == 'PC':

        product_model = product.pc_product_data.model
        same_products = models.MainProductDatabase.objects.filter(pc_product_data__model=product_model)
        same_products_data = {
            'items' : same_products,
            'p_c_i_e' : check_no_data({element.pc_product_data.p_c_i_e for element in same_products}),
            'ram' : check_no_data({element.pc_product_data.ram for element in same_products}),
            'system' : check_no_data({element.pc_product_data.system for element in same_products}),
            'graph' : check_no_data({element.pc_product_data.graph for element in same_products}),
            'processor' : check_no_data({element.pc_product_data.processor for element in same_products}),
            'items_id' : [element.id for element in same_products]
        }

        return same_products_data

    elif cattegory == 'Monitors':

        product_model = product.monitors_product_data.model
        same_products = models.MainProductDatabase.objects.filter(monitors_product_data__model=product_model)
        same_products_data = {
            'items' : same_products,
            'colors' : check_no_data({element.monitors_product_data.color for element in same_products}),
            'refresh_rate' : check_no_data({element.monitors_product_data.refresh_rate for element in same_products}),
            'power_consumption' : check_no_data({element.monitors_product_data.power_consumption for element in same_products}),
            'diagonal' : check_no_data({element.monitors_product_data.diagonal for element in same_products}),
            'items_id' : [element.id for element in same_products]
        }

        return same_products_data

    elif cattegory == 'SSD':

        product_model = product.ssd_product_data.model
        same_products = models.MainProductDatabase.objects.filter(ssd_product_data__model=product_model)
        same_products_data = {
            'items' : same_products,
            'capacity' : check_no_data({element.ssd_product_data.capacity for element in same_products}),
            'reading_speed' : check_no_data({element.ssd_product_data.reading_speed for element in same_products}),
            'writing_speed' : check_no_data({element.ssd_product_data.writing_speed for element in same_products}),
            'items_id' : [element.id for element in same_products]
        }

        return same_products_data

    elif cattegory == 'Ram':

        product_model = product.ram_product_data.model
        same_products = models.MainProductDatabase.objects.filter(ram_product_data__model=product_model)
        same_products_data = {
            'items' : same_products,
            'capacity' : check_no_data({element.ram_product_data.capacity for element in same_products}),
            'modules_number' : check_no_data({element.ram_product_data.modules_number for element in same_products}),
            'delay' : check_no_data({element.ram_product_data.delay for element in same_products}),
            'frequency' : check_no_data({element.ram_product_data.frequency for element in same_products}),
            'items_id' : [element.id for element in same_products]
        }

        return same_products_data

    elif cattegory == 'Pendrives':

        product_model = product.pendrive_product_data.model
        same_products = models.MainProductDatabase.objects.filter(pendrive_product_data__model=product_model)
        same_products_data = {
            'items' : same_products,
            'capacity' : check_no_data({element.pendrive_product_data.capacity for element in same_products}),
            'items_id' : [element.id for element in same_products]
        }

        return same_products_data

    elif cattegory == 'Switches':

        product_model = product.switch_product_data.model
        same_products = models.MainProductDatabase.objects.filter(switch_product_data__model=product_model)
        same_products_data = {
            'items' : same_products,
            'num_of_poe' : check_no_data({element.switch_product_data.num_of_poe for element in same_products}),
            'ports_num' : check_no_data({element.switch_product_data.ports_num for element in same_products}),
            'bus_speed' : check_no_data({element.switch_product_data.bus_speed for element in same_products}),
            'items_id' : [element.id for element in same_products]
        }

        return same_products_data

    elif cattegory == 'TV':

        product_model = product.tv_product_data.model
        same_products = models.MainProductDatabase.objects.filter(tv_product_data__model=product_model)
        same_products_data = {
            'items' : same_products,
            'diagonal' : check_no_data({element.tv_product_data.diagonal for element in same_products}),
            'items_id' : [element.id for element in same_products]
        }

        return same_products_data

    elif cattegory == 'Headphones':

        product_model = product.headphone_product_data.model
        same_products = models.MainProductDatabase.objects.filter(headphone_product_data__model=product_model)
        same_products_data = {
            'items' : same_products,
            'colors' : check_no_data({element.headphone_product_data.color for element in same_products}),
            'items_id' : [element.id for element in same_products]
        }

        return same_products_data

    elif cattegory == 'Accesories for laptops':

        product_model = product.accesories_for_laptop.model
        same_products = models.MainProductDatabase.objects.filter(accesories_for_laptop__model=product_model)
        same_products_data = {
            'items' : same_products,
            'color' : check_no_data({element.accesories_for_laptop.color for element in same_products}),
            'diagonal' : check_no_data({element.accesories_for_laptop.diagonal_for_cases for element in same_products}),
            'items_id' : [element.id for element in same_products]
        }

        return same_products_data

def find_new_product(product_items_list: List,
                     product_data: str,
                     product_parametr: str,
                     main_product: models.MainProductDatabase) -> models.MainProductDatabase:

    for id in product_items_list:

        if main_product.cattegory == "Phones":

            if product_parametr == 'color':
                try:
                    product = models.MainProductDatabase.objects.get(id=int(id), color=product_data)
                    return product
                except:
                    pass

            elif product_parametr == 'memory':
                try:
                    product = models.MainProductDatabase.objects.get(id=int(id), phones_product_data__memory=product_data)
                    return product
                except:
                    pass

            elif product_parametr == 'ram':
                try:
                    product = models.MainProductDatabase.objects.get(id=int(id), phones_product_data__ram=product_data)
                    return product
                except:
                    pass

            elif product_parametr == 'battery':
                try:
                    product = models.MainProductDatabase.objects.get(id=int(id), phones_product_data__battery=product_data)
                    return product
                except:
                    pass

        elif main_product.cattegory == "PC":

            if product_parametr == 'ram':
                try:
                    product = models.MainProductDatabase.objects.get(id=int(id), pc_product_data__ram=product_data)
                    return product
                except:
                    pass

            elif product_parametr == 'p_c_i_e':
                try:
                    product = models.MainProductDatabase.objects.get(id=int(id), pc_product_data__p_c_i_e=product_data)
                    return product
                except:
                    pass

            elif product_parametr == 'processor':
                try:
                    product = models.MainProductDatabase.objects.get(id=int(id), pc_product_data__processor=product_data)
                    return product
                except:
                    pass

            elif product_parametr == 'system':
                try:
                    product = models.MainProductDatabase.objects.get(id=int(id), pc_product_data__system=product_data)
                    return product
                except:
                    pass

            elif product_parametr == 'graph':
                try:
                    product = models.MainProductDatabase.objects.get(id=int(id), pc_product_data__graph=product_data)
                    return product
                except:
                    pass

        elif main_product.cattegory == "Laptops":

            if product_parametr == 'ram':
                try:
                    product = models.MainProductDatabase.objects.get(id=int(id), laptops_product_data__ram=product_data)
                    return product
                except:
                    pass

            elif product_parametr == 'p_c_i_e':
                try:
                    product = models.MainProductDatabase.objects.get(id=int(id), laptops_product_data__p_c_i_e=product_data)
                    return product
                except:
                    pass


            elif product_parametr == 'processor':
                try:
                    product = models.MainProductDatabase.objects.get(id=int(id), laptops_product_data__processor=product_data)
                    return product
                except:
                    pass

            elif product_parametr == 'system':
                try:
                    product = models.MainProductDatabase.objects.get(id=int(id), laptops_product_data__system=product_data)
                    return product
                except:
                    pass

            elif product_parametr == 'color':
                try:
                    product = models.MainProductDatabase.objects.get(id=int(id), laptops_product_data__color=product_data)
                    return product
                except:
                    pass

        elif main_product.cattegory == "Monitors":

            if product_parametr == 'color':
                try:
                    product = models.MainProductDatabase.objects.get(id=int(id), color=product_data)
                    return product
                except:
                    pass

            elif product_parametr == 'power_consumption':
                try:
                    product = models.MainProductDatabase.objects.get(id=int(id), monitors_product_data__power_consumption=product_data)
                    return product
                except:
                    pass

            elif product_parametr == 'diagonal':
                try:
                    product = models.MainProductDatabase.objects.get(id=int(id), monitors_product_data__diagonal=product_data)
                    return product
                except:
                    pass

            elif product_parametr == 'refresh_rate':
                try:
                    product = models.MainProductDatabase.objects.get(id=int(id), monitors_product_data__refresh_rate=product_data)
                    return product
                except:
                    pass

        elif main_product.cattegory == "Accesories for laptops":

            if product_parametr == 'color':
                try:
                    product = models.MainProductDatabase.objects.get(id=int(id), color=product_data)
                    return product
                except:
                    pass

            elif product_parametr == 'diagonal_for_cases':
                try:
                    product = models.MainProductDatabase.objects.get(id=int(id), accesories_for_laptop__diagonal_for_cases=product_data)
                    return product
                except:
                    pass

        elif main_product.cattegory == "SSD":

            if product_parametr == 'color':
                try:
                    product = models.MainProductDatabase.objects.get(id=int(id), color=product_data)
                    return product
                except:
                    pass

            elif product_parametr == 'capacity':
                try:
                    product = models.MainProductDatabase.objects.get(id=int(id), ssd_product_data__capacity=product_data)
                    return product
                except:
                    pass

            elif product_parametr == 'reading_speed':
                try:
                    product = models.MainProductDatabase.objects.get(id=int(id), ssd_product_data__reading_speed=product_data)
                    return product
                except:
                    pass

            elif product_parametr == 'writing_speed':
                try:
                    product = models.MainProductDatabase.objects.get(id=int(id), ssd_product_data__writing_speed=product_data)
                    return product
                except:
                    pass

        elif main_product.cattegory == "Ram":

            if product_parametr == 'modules_number':
                try:
                    product = models.MainProductDatabase.objects.get(id=int(id), ram_product_data__modules_number=product_data)
                    return product
                except:
                    pass

            elif product_parametr == 'frequency':
                try:
                    product = models.MainProductDatabase.objects.get(id=int(id), ram_product_data__frequency=product_data)
                    return product
                except:
                    pass

            elif product_parametr == 'delay':
                try:
                    product = models.MainProductDatabase.objects.get(id=int(id), ram_product_data__delay=product_data)
                    return product
                except:
                    pass

            elif product_parametr == 'capacity':
                try:
                    product = models.MainProductDatabase.objects.get(id=int(id), ram_product_data__capacity=product_data)
                    return product
                except:
                    pass

        elif main_product.cattegory == "Pendrives":

            try:
                product = models.MainProductDatabase.objects.get(id=int(id), ram_product_data__capacity=product_data)
                return product
            except:
                pass

        elif main_product.cattegory == "Switches":

                if product_parametr == 'num_of_poe':
                    try:
                        product = models.MainProductDatabase.objects.get(id=int(id), switch_product_data__num_of_poe=product_data)
                        return product
                    except:
                        pass

                elif product_parametr == 'ports_num':
                    try:
                        product = models.MainProductDatabase.objects.get(id=int(id), switch_product_data__ports_num=product_data)
                        return product
                    except:
                        pass

                elif product_parametr == 'bus_speed':
                    try:
                        product = models.MainProductDatabase.objects.get(id=int(id), switch_product_data__bus_speed=product_data)
                        return product
                    except:
                        pass

        elif main_product.cattegory == "TV":

                try:
                    product = models.MainProductDatabase.objects.get(id=int(id), tv_product_data__diagonal=product_data)
                    return product
                except:
                    pass

        elif main_product.cattegory == "Headphones":

            if product_parametr == 'color':
                try:
                    product = models.MainProductDatabase.objects.get(id=int(id), color=product_data)
                    return product
                except:
                    pass

def get_product(model: str, instance: Any) -> models.MainProductDatabase:
    """ Help function for signals. Get product with specific model """

    if model.lower() == "Phones".lower():
        return models.MainProductDatabase.objects.get(phones_product_data=instance).phones_product_data
    elif model.lower() == "Monitors".lower():
        return models.MainProductDatabase.objects.get(monitors_product_data=instance).monitors_product_data
    elif model.lower() == 'Laptops'.lower():
        return models.MainProductDatabase.objects.get(laptops_product_data=instance).laptops_product_data
    elif model.lower() == 'Pc'.lower():
        return models.MainProductDatabase.objects.get(pc_product_data=instance).pc_product_data
    elif model.lower() == 'AccesoriesForLaptops'.lower():
        return models.MainProductDatabase.objects.get(accesories_for_laptop=instance).accesories_for_laptop
    elif model.lower() == 'Ssd'.lower():
        return models.MainProductDatabase.objects.get(ssd_product_data=instance).ssd_product_data
    elif model.lower() == 'Graphs'.lower():
        return models.MainProductDatabase.objects.get(graph_product_data=instance).graph_product_data
    elif model.lower() == 'Ram'.lower():
        return models.MainProductDatabase.objects.get(ram_product_data=instance).ram_product_data
    elif model.lower() == 'Pendrives'.lower():
        return models.MainProductDatabase.objects.get(pendrive_product_data=instance).pendrive_product_data
    elif model.lower() == 'Switches'.lower():
        return models.MainProductDatabase.objects.get(switch_product_data=instance).switch_product_data
    elif model.lower() == 'Motherboard'.lower():
        return models.MainProductDatabase.objects.get(motherboard_product_data=instance).motherboard_product_data
    elif model.lower() == 'Cpu'.lower():
        return models.MainProductDatabase.objects.get(cpu_product_data=instance).cpu_product_data
    elif model.lower().lower() == 'Tv'.lower().lower():
        return models.MainProductDatabase.objects.get(tv_product_data=instance).tv_product_data
    elif model.lower() == 'Headphones'.lower():
        return models.MainProductDatabase.objects.get(headphone_product_data=instance).headphone_product_data
    elif model.lower() == 'Routers'.lower():
        return models.MainProductDatabase.objects.get(router_product_data=instance).router_product_data

def choose_model(model: str, instance) -> models.MainProductDatabase:
    """ Help function for signals. Create objects for specific model """

    if model == "Phones":
        return models.MainProductDatabase.objects.create(phones_product_data=instance)
    elif model == "Monitors":
        return models.MainProductDatabase.objects.create(monitors_product_data=instance)
    elif model == 'Laptops':
        return models.MainProductDatabase.objects.create(laptops_product_data=instance)
    elif model == 'Pc':
        return models.MainProductDatabase.objects.create(pc_product_data=instance)
    elif model == 'AccesoriesForLaptops':
        return models.MainProductDatabase.objects.create(accesories_for_laptop=instance)
    elif model == 'Ssd':
        return models.MainProductDatabase.objects.create(ssd_product_data=instance)
    elif model == 'Graphs':
        return models.MainProductDatabase.objects.create(graph_product_data=instance)
    elif model == 'Ram':
        return models.MainProductDatabase.objects.create(ram_product_data=instance)
    elif model == 'Pendrives':
        return models.MainProductDatabase.objects.create(pendrive_product_data=instance)
    elif model == 'Switches':
        return models.MainProductDatabase.objects.create(switch_product_data=instance)
    elif model == 'Motherboard':
        return models.MainProductDatabase.objects.create(motherboard_product_data=instance)
    elif model == 'Cpu':
        return models.MainProductDatabase.objects.create(cpu_product_data=instance)
    elif model == 'Tv':
        return models.MainProductDatabase.objects.create(tv_product_data=instance)
    elif model == 'Headphones':
        return models.MainProductDatabase.objects.create(headphone_product_data=instance)
    elif model == 'Routers':
        return models.MainProductDatabase.objects.create(router_product_data=instance)


def try_to_get_product(product: "models.MainProductDatabase", instance: Any) -> "models.MainProductDatabase":
    """ Help function for signals. Try to get specific product from model """

    instance_obj = models.MainProductDatabase.objects.get(ean=product.ean)

    check_if_obj_is_instance_of = {

        'pc_product_data': lambda obj: isinstance(obj, models.Pc) if True else '',
        'monitors_product_data': lambda obj: isinstance(obj, models.Monitors) if True else '',
        'phones_product_data': lambda obj: isinstance(obj, models.Phones) if True else '',
        'laptops_product_data': lambda obj: isinstance(obj, models.Laptops) if True else '',
        'accesories_for_laptop': lambda obj: isinstance(obj, models.AccesoriesForLaptops) if True else '',
        'ssd_product_data': lambda obj: isinstance(obj, models.Ssd) if True else '',
        'graph_product_data': lambda obj: isinstance(obj, models.Graphs) if True else '',
        'ram_product_data': lambda obj: isinstance(obj, models.Ram) if True else '',
        'pendrive_product_data': lambda obj: isinstance(obj, models.Pendrives) if True else '',
        'switch_product_data': lambda obj: isinstance(obj, models.Switches) if True else '',
        'motherboard_product_data': lambda obj: isinstance(obj, models.Motherboard) if True else '',
        'cpu_product_data': lambda obj: isinstance(obj, models.Cpu) if True else '',
        'tv_product_data': lambda obj: isinstance(obj, models.Tv) if True else '',
        'headphone_product_data': lambda obj: isinstance(obj, models.Headphones) if True else '',
        'router_product_data': lambda obj: isinstance(obj, models.Routers) if True else '',

    }

    for key, value in model_to_dict(instance_obj).items():

        if getattr(instance_obj, key) != None:

            get_instance_attribute = getattr(instance_obj, key)

            try:
                if check_if_obj_is_instance_of[key](get_instance_attribute):
                    return get_instance_attribute
            except:
                pass


def sort_by_product_rate(products: QuerySet) -> List[QuerySet]:
    """ Sorting products by stars rate """

    product_dict = { product:product.get_star_avg[0] for product in products}
    product_sorted = sorted(product_dict.items(), key=lambda item: item[1], reverse=True)

    for product in product_sorted:
        product[0].rate = product[0].get_star_avg[0]

    return [product[0] for product in product_sorted]


def paginate_view(products: QuerySet, result: int, page: int) -> range:
    """ create paginator from model query """

    paginator = Paginator(products, result)

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        products = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        products = paginator.page(page)

    left_index = (int(page)-2)

    if left_index < 1:
        left_index = 1

    right_index = (int(page)+3)
    if right_index > paginator.num_pages:
            right_index = paginator.num_pages +1

    return range(left_index, right_index), paginator, products


# def get_model_queryset(catt, producent=''):

#     if producent:

#         if producent == 'All':
#             return models.MainProductDatabase.objects.filter(cattegory=catt)

#         get_queryset = {

#         'PC': lambda producent: models.Pc.objects.filter(producent=producent),
#         'Monitors': lambda producent: models.Monitors.objects.filter(producent=producent),
#         'Phones': lambda producent: models.Phones.objects.filter(producent=producent),
#         'Laptops': lambda producent: models.Laptops.objects.filter(producent=producent),
#         'Accesories for laptops': lambda producent: models.AccesoriesForLaptops.objects.filter(producent=producent),
#         'SSD': lambda producent: models.Ssd.objects.filter(producent=producent),
#         'Graphs': lambda producent: models.Graphs.objects.filter(producent=producent),
#         'Ram': lambda producent: models.Ram.objects.filter(producent=producent),
#         'Pendrives': lambda producent: models.Pendrives.objects.filter(producent=producent),
#         'Switches': lambda producent: models.Switches.objects.filter(producent=producent),
#         'Motherboard': lambda producent: models.Motherboard.objects.filter(producent=producent),
#         'CPU': lambda producent: models.Cpu.objects.filter(producent=producent),
#         'TV': lambda producent: models.Tv.objects.filter(producent=producent),
#         'Headphones': lambda producent: models.Headphones.objects.filter(producent=producent),
#         'Routers': lambda producent: models.Routers.objects.filter(producent=producent),
#         }

#         return get_queryset[catt](producent)

#     else:


#         get_queryset = {

#             'PC': models.Pc.objects.all(),
#             'Monitors': models.Monitors.objects.all(),
#             'Phones': models.Phones.objects.all(),
#             'Laptops': models.Laptops.objects.all(),
#             'Accesories for laptops': models.AccesoriesForLaptops.objects.all(),
#             'SSD': models.Ssd.objects.all(),
#             'Graphs': models.Graphs.objects.all(),
#             'Ram': models.Ram.objects.all(),
#             'Pendrives': models.Pendrives.objects.all(),
#             'Switches': models.Switches.objects.all(),
#             'Motherboard': models.Motherboard.objects.all(),
#             'CPU': models.Cpu.objects.all(),
#             'TV': models.Tv.objects.all(),
#             'Headphones': models.Headphones.objects.all(),
#             'Routers': models.Routers.objects.all(),
#         }

#         return get_queryset[catt]


