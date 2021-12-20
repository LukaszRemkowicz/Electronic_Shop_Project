import itertools, os

from ProductApp.products import phones, monitors, laptops, pcs, accesories, ssds, graphs, rams, \
                                pendrives, switches, motherboards, cpus, tvs, headphones, routers
from django.core.files import File
from ProductApp.models import *
from ProductApp.products import *

products = [phones, monitors, laptops, pcs, accesories, ssds, graphs, rams, pendrives,
            switches, motherboards, cpus, tvs, headphones, routers]
folders = ['phones', 'monitors', 'laptops', 'pcs', 'accesories', 'ssds', 'graphs', 'rams', 'pendrives',
           'switches', 'motherboards', 'cpus', 'tvs', 'headphones', 'routers']


models = {
    'phones': lambda **item: Phones.objects.create(**item),
    'monitors': lambda **item: Monitors.objects.create(**item),
    'laptops': lambda **item: Laptops.objects.create(**item),
    'pcs': lambda **item: Pc.objects.create(**item),
    'accesories': lambda **item: AccesoriesForLaptops.objects.create(**item),
    'ssds': lambda **item: Ssd.objects.create(**item),
    'graphs': lambda **item: Graphs.objects.create(**item),
    'rams': lambda **item: Ram.objects.create(**item),
    'pendrives': lambda **item: Pendrives.objects.create(**item),
    'switches': lambda **item: Switches.objects.create(**item),
    'motherboards': lambda **item: Motherboard.objects.create(**item),
    'cpus': lambda **item: Cpu.objects.create(**item),
    'tvs': lambda **item: Tv.objects.create(**item),
    'headphones': lambda **item: Headphones.objects.create(**item),
    'routers': lambda **item: Routers.objects.create(**item),
}



for prod, folder in zip(products, folders):
    for product, fold in zip(prod, itertools.repeat(folder)):
        PATH = rf'electronic_shop/static/images/products/{fold}/'
        try:
            itt = models[fold](**product)
        except FileNotFoundError:
            pass
        itt.main_photo.save(product['main_photo'], File(open(PATH + product['main_photo'], 'rb')))
        try:
            itt.second_photo.save(product['second_photo'], File(open(PATH + product['second_photo'], 'rb')))
        except:
            pass
        try:
            itt.third_photo.save(product['third_photo'], File(open(PATH + product['third_photo'], 'rb')))
        except:
            pass