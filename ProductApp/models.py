from typing import Any, Dict, List, Optional, Tuple, Union
import os, codecs, math, uuid
from datetime import date

from django.db import models, reset_queries
from django.utils import tree, timezone
from django import utils
# from django.db.models.base import Model
# from django.db.models.expressions import F
from django.utils.safestring import mark_safe
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings

from ProductApp.utilss.models_utils import *

# User = get_user_model()
User = settings.AUTH_USER_MODEL


CHOICES = [
        ("Laptops", "Laptops"),
        ("Phones", 'Phones'),
        ("PC", "PC"),
        ("Monitors", "Monitors"),
        ("Accesories for laptops", "Accesories for laptops"),
        ("SSD", "SSD"),
        ("Graphs", "Graphs"),
        ("Ram", "Ram"),
        ("Pendrives", "Pendrives"),
        ("Routers", "Routers"),
        ("Switches", "Switches"),
        ("Motherboard", "Motherboard"),
        ("CPU", "CPU"),
        ("TV", "TV"),
        ("Headphones", "Headphones"),
    ]


def product_image_file_path(instance, filename):
    """ Generate file path for new product image """

    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/products/', filename)


class Inherit(models.Model):

    name = models.CharField(max_length=200, default='')
    model = models.CharField(max_length=100, null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    pieces = models.IntegerField(default=0)
    promotion = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    producent = models.CharField(max_length=100, default='')
    producent_code = models.CharField(max_length=100, default='', null=True, blank=True)
    ean = models.BigIntegerField(unique=True, null=True)
    color = models.CharField(max_length=50, null=True, blank=True)
    distribution = models.CharField(max_length=10, default='EU')
    cattegory = models.CharField(choices=CHOICES, max_length=50, default='')
    describe = models.CharField(max_length=30000, null=True, blank=True, default='')
    width = models.FloatField(blank=True, null=True)
    deep = models.FloatField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)

    main_photo = models.ImageField(upload_to=product_image_file_path, null=True, blank=True)
    main_photo = models.ImageField(upload_to=product_image_file_path, null=True, blank=True)
    second_photo = models.ImageField(upload_to=product_image_file_path, null=True, blank=True)
    third_photo = models.ImageField(upload_to=product_image_file_path, null=True, blank=True)
    html_file = models.FileField(upload_to=product_image_file_path, default="", null=True, blank=True)
    product_of_the_day = models.BooleanField(default=False)
    bought_num = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

    def render_html(self) -> Any:
        path = self.html_file.path
        if os.path.exists(path):
            html_string = codecs.open(path, 'r').read()
            return mark_safe(html_string)
        return None

    @property
    def get_star_avg(self) -> Tuple[str, List[bool]]:
        """ Method to get product review avarage """

        product = MainProductDatabase.objects.get(ean=self.ean)

        opinions = len(Reviews.objects.filter(product=product.id, checked_by_employer=True))
        stars = sum([element.stars for element in Reviews.objects.filter(product=product.id,checked_by_employer=True)])
        if stars > 0:
            result = stars/opinions
            frac, whole = math.modf(result)

            ranger = [True if num  in [element for element in range(1, int(whole) +1 )]
                      else False for num in range(1, int(6))]

            if frac > 0:
                return str(result), ranger
            else:
                return str(int(whole)), ranger
        else:
            return str(0), [False for _ in range(5)]

    @property
    def get_stars(self) -> Dict[str, int]:
        """ Help method to generate progress bars """

        product = MainProductDatabase.objects.get(ean=self.ean)

        stars = [element.stars for element in Reviews.objects.filter(product=product.id, checked_by_employer=True)]
        stars_dict = {key:0 for key in range(1, 6)}

        if len(stars) > 0:

            for element in stars:
                if element not in stars_dict:
                    stars_dict[element] = 1
                else:
                    stars_dict[element] += 1

            for key, value in stars_dict.items():
                percentage = (100*value) / len(stars)
                stars_dict[key] = (value, int(percentage))

        return stars_dict

    @staticmethod
    def get_producents(query):
        producent_dictionary = {}
        for product in query:
            if product.producent in producent_dictionary:
                producent_dictionary[product.producent] += 1
            else:
                producent_dictionary[product.producent] = 1

        return producent_dictionary

    @staticmethod
    def change_decimal(num) -> Union[float, int]:
        frac, whole = math.modf(num)
        if frac:
            return num
        else:
            return int(whole)

    def change_width(self) -> Union[float, int]:
        return Inherit.change_decimal(self.width)

    def change_deep(self) -> Union[float, int]:
        return Inherit.change_decimal(self.deep)

    def change_high(self) -> Union[float, int]:
        return Inherit.change_decimal(self.high)

    def change_weight(self) -> Union[float, int]:
        return Inherit.change_decimal(self.weight)

    @property
    def return_images(self) -> List:
        images_dictionary = dict()
        if self.main_photo:
            images_dictionary['main_photo'] = self.main_photo.url
        if self.second_photo:
            images_dictionary['second_photo'] = self.second_photo.url
        if self.third_photo:
            images_dictionary['third_photo'] = self.third_photo.url

        return images_dictionary

    @property
    def get_num_of_reviews(self) -> int:
        product = MainProductDatabase.objects.get(ean=self.ean)
        return len(Reviews.objects.filter(product=product.id, checked_by_employer=True))

    @property
    def get_num_of_questions(self) -> int:
        product = MainProductDatabase.objects.get(ean=self.ean)
        return len(Questions.objects.filter(product=product.id, checked_by_employer=True))

    class Meta:
        abstract = True


class MainProductDatabase(models.Model):

    main_photo = models.ImageField(null=True, blank=True, upload_to=product_image_file_path)
    second_photo = models.ImageField(null=True, blank=True, upload_to=product_image_file_path)
    third_photo = models.ImageField(null=True, blank=True, upload_to=product_image_file_path)
    name = models.CharField(max_length=100, default='')
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    pieces = models.IntegerField(default=0)
    promotion = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    product_of_the_day = models.BooleanField(default=False)
    product_of_the_day_added = models.DateTimeField(null=True, blank=True)
    selected = models.BooleanField(default=False)

    phones_product_data = models.ForeignKey('Phones', on_delete=models.CASCADE, null=True, blank=True)
    monitors_product_data = models.ForeignKey('Monitors', on_delete=models.CASCADE, null=True, blank=True)
    laptops_product_data = models.ForeignKey('Laptops', on_delete=models.CASCADE, default='', null=True, blank=True)
    pc_product_data = models.ForeignKey('Pc', on_delete=models.CASCADE, default='', null=True, blank=True)
    accesories_for_laptop = models.ForeignKey('AccesoriesForLaptops', on_delete=models.CASCADE, default='', null=True, blank=True)
    ssd_product_data = models.ForeignKey('Ssd', on_delete=models.CASCADE, default='', null=True, blank=True)
    graph_product_data = models.ForeignKey('Graphs', on_delete=models.CASCADE, default='', null=True, blank=True)
    ram_product_data = models.ForeignKey('Ram', on_delete=models.CASCADE, default='', null=True, blank=True)
    pendrive_product_data = models.ForeignKey('Pendrives', on_delete=models.CASCADE, default='', null=True, blank=True)
    switch_product_data = models.ForeignKey('Switches', on_delete=models.CASCADE, default='', null=True, blank=True)
    motherboard_product_data = models.ForeignKey('Motherboard', on_delete=models.CASCADE, default='', null=True, blank=True)
    cpu_product_data = models.ForeignKey('Cpu', on_delete=models.CASCADE, default='', null=True, blank=True)
    tv_product_data = models.ForeignKey('Tv', on_delete=models.CASCADE, default='', null=True, blank=True)
    headphone_product_data = models.ForeignKey('Headphones', on_delete=models.CASCADE, default='', null=True, blank=True)
    router_product_data = models.ForeignKey('Routers', on_delete=models.CASCADE, default='', blank=True, null=True,)

    ean = models.BigIntegerField(null=True, blank=True, unique=True)
    cattegory =  models.CharField(choices=CHOICES, max_length=50, default='')
    color = models.CharField(max_length=100, default='', blank=True, null=True)
    bought_num = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    producent = models.CharField(max_length=100, default='')
    model = models.CharField(max_length=100, null=True, blank=True)

    likes = models.ManyToManyField(User, default=None, blank=True)

    class Meta:
        ordering = ['created']

    def __str__(self) -> str:
        return f'Product: {self.name}'

    @property
    def get_img(self) -> str:
        try:
            url = self.main_photo.url
        except ObjectDoesNotExist:
            url=''

        return url


    @property
    def get_star_avg(self) -> Tuple[str, List[bool]]:
        """ Method to get product review avarage """

        opinions = len(Reviews.objects.filter(product=self.id, checked_by_employer=True))
        stars = sum([element.stars for element in Reviews.objects.filter(product=self.id,checked_by_employer=True)])
        if stars > 0:
            result = stars/opinions
            frac, whole = math.modf(result)

            ranger = [True if num  in [element for element in range(1, int(whole) +1 )]
                      else False for num in range(1, int(6))]

            if frac > 0:
                return str(result), ranger
            else:
                return str(int(whole)), ranger
        else:
            return str(0), [False for _ in range(5)]

    # @property
    # def get_stars(self) -> Dict[str, int]:
    #     """ Help method to generate progress bars """

    #     stars = [element.stars for element in Reviews.objects.filter(product=self.id, checked_by_employer=True)]
    #     stars_dict = {key:0 for key in range(1, 6)}

    #     if len(stars) > 0:

    #         for element in stars:
    #             if element not in stars_dict:
    #                 stars_dict[element] = 1
    #             else:
    #                 stars_dict[element] += 1

    #         for key, value in stars_dict.items():
    #             percentage = (100*value) / len(stars)
    #             stars_dict[key] = (value, int(percentage))

    #     return stars_dict



class Phones(Inherit):

    ram = models.CharField(max_length=50, default='')
    memory = models.CharField(max_length=50, default='')
    modem = models.CharField(max_length=20 ,default='')

    waterproof = models.BooleanField(default=False)
    system = models.CharField(max_length=50, default='')
    processor = models.CharField(max_length=100, default='')
    cpu_clock = models.CharField(max_length=100, default='')
    memory_card = models.CharField(max_length=50, default='')
    max_memory_card = models.CharField(max_length=50, default='')
    usb = models.CharField(max_length=10, default='')
    audio_jack = models.CharField(max_length=50, default='')
    screen = models.CharField(max_length=30, default='')
    screen_diagonal = models.CharField(max_length=50, default='')
    battery = models.CharField(max_length=50, default='')

    @classmethod
    def data_products_to_filter(cls, querySet='') -> Dict:

        if querySet:
            phones = querySet
        else:
            phones = Phones.objects.all()

        return filter_phones(phones)


class Monitors(Inherit):

    resolution = models.CharField(max_length=50, default='')
    refresh_rate = models.CharField(max_length=20, default='')
    format = models.CharField(max_length=10, default='')
    power_consumption = models.CharField(max_length=20, default='')
    matrix_type = models.CharField(max_length=20, default='')
    screen = models.CharField(max_length=30, default='')
    diagonal = models.CharField(max_length=10, default='')
    curved = models.CharField(max_length=10, default='')


    @classmethod
    def data_products_to_filter(cls, querySet='') -> Dict:

        if querySet:
            monitors = querySet
        else:
            monitors = Monitors.objects.all()

        return filter_monitors(monitors)


class Laptops(Inherit):

    resolution = models.CharField(max_length=50, default='')
    energy_time = models.IntegerField(default=0)
    battery = models.CharField(max_length=30, default='')
    screen = models.CharField(max_length=30, default='')
    screen_diagonal = models.CharField(max_length=10, default='')
    system = models.CharField(max_length=50, default='')
    graph = models.CharField(max_length=50, default='')
    second_graph = models.CharField(max_length=50, default='', blank=True, null=True)
    disc = models.CharField(max_length=100, default='')
    ram = models.IntegerField(default=0)
    ram_model = models.CharField(max_length=20, default='')
    max_ram = models.IntegerField(default=0)
    ram_freq = models.CharField(max_length=50, default='')
    p_c_i_e = models.CharField(max_length=50, default='')
    wifi = models.CharField(max_length=50, default='')
    bluetooth = models.CharField(max_length=10, default='Yes')
    processor = models.CharField(max_length=50, default='')
    processor_clock = models.CharField(max_length=50, default='')
    processor_cores_threads = models.CharField(max_length=50, default='')


    @classmethod
    def data_products_to_filter(cls, querySet='') -> Dict:

        if querySet:
            laptops = querySet
        else:
            laptops = Laptops.objects.all()

        return filter_laptops(laptops)



class Pc(Inherit):

    processor = models.CharField(max_length=50, default='')
    socket = models.CharField(max_length=20, default='')
    cooler = models.CharField(max_length=20, default='')
    system = models.CharField(max_length=20, default='')
    graph = models.CharField(max_length=50, default='')
    motherboard_chipset = models.CharField(max_length=20, default='')
    power_suply = models.CharField(max_length=20, default='')
    mouse = models.CharField(max_length=10, default='', blank=True, null=True)
    keyboard = models.CharField(max_length=10, default='', blank=True, null=True)
    disc = models.CharField(max_length=20, default='')
    ram = models.IntegerField(default=0)
    ram_type = models.CharField(max_length=20, default='')
    p_c_i_e = models.CharField(max_length=50 ,default='')
    wifi = models.CharField(max_length=20, default='')
    bluetooth = models.CharField(max_length=10, default='')


    @classmethod
    def data_products_to_filter(cls, querySet='') -> Dict:

        print('query set w modelach', querySet)
        if querySet:
            pcs = querySet
        else:
            pcs = Pc.objects.all()
        print('pcs len', filter_pcs(pcs))

        return filter_pcs(pcs)


class AccesoriesForLaptops(Inherit):
    diagonal_for_cases = models.CharField(max_length=20, blank=True, null=True)

    @classmethod
    def data_products_to_filter(cls, queryset='') -> None:

        pass


class Ssd(Inherit):

    format = models.CharField(max_length=30, default='')
    capacity = models.CharField(max_length=30, default='')
    reading_speed = models.CharField(max_length=30, default='')
    writing_speed = models.CharField(max_length=30, default='')
    life_time = models.CharField(max_length=30 ,default='')


    @classmethod
    def data_products_to_filter(cls, querySet='') -> Dict:

        if querySet:
            ssd = querySet
        else:
            ssd = Ssd.objects.all()

        return filter_ssd(ssd)


class Graphs(Inherit):

    chipset = models.CharField(max_length=30, default='')
    chipset_producent = models.CharField(max_length=50, default='')
    phisic_lenght = models.CharField(max_length=50, default='')
    ram = models.CharField(max_length=50, default='')
    ram_type = models.CharField(max_length=50, default='')
    core_clock = models.CharField(max_length=50, default='')
    connector_type = models.CharField(max_length=60, default='')

    @classmethod
    def data_products_to_filter(cls, querySet='') -> Dict:

        if querySet:
            graphs = querySet
        else:
            graphs = Graphs.objects.all()

        return filter_graphs(graphs)


class Ram(Inherit):

    capacity = models.CharField(max_length=30, default='')
    frequency = models.CharField(max_length=30, default='')
    modules_number = models.IntegerField(default=0)
    delay = models.CharField(max_length=30, default='')
    voltage = models.CharField(max_length=30, default='')
    lights = models.CharField(max_length=20, default='No')
    type = models.CharField(max_length=20, default='')


    @classmethod
    def data_products_to_filter(cls, querySet='') -> Dict:

        if querySet:
            rams = querySet
        else:
            rams = Ram.objects.all()

        return filter_rams(rams)


class Pendrives(Inherit):

    capacity = models.CharField(max_length=20, default='')
    connector = models.CharField(max_length=20, default='')
    case = models.CharField(max_length=50, default='')

    @classmethod
    def data_products_to_filter(cls, querySet='') -> Dict:

        if querySet:
            pendrives = querySet
        else:
            pendrives = Pendrives.objects.all()

        return filter_pendrives(pendrives)


class Switches(Inherit):

    num_of_poe = models.CharField(max_length=40, default='', null=True, blank=True)
    case_kind = models.CharField(max_length=40, default='')
    manageable = models.CharField(max_length=40, default='')
    ports_num = models.CharField(max_length=50 ,default='')
    bus_speed = models.CharField(max_length=50 ,default='')

    @property
    def split_ports(self):
        return self.ports_num.split('\n')

    @classmethod
    def data_products_to_filter(cls, querySet='') -> Dict:

        if querySet:
            switches = querySet
        else:
            switches = Switches.objects.all()

        return filter_switches(switches)


class Motherboard(Inherit):
    chipset = models.CharField(max_length=50, default='')
    processor_socket = models.CharField(max_length=50, default='')
    ram_slots = models.IntegerField(default=4)
    card_standard = models.CharField(max_length=20, default='')
    raid_controler = models.CharField(max_length=100, default='')
    ram = models.CharField(max_length=10, default='')
    ram_max_cap = models.CharField(max_length=20, default='')
    graph_integrated = models.CharField(max_length=20, default='')
    sound = models.CharField(max_length=20, default='')
    network_card = models.CharField(max_length=100, default='')
    wifi = models.CharField(max_length=50, default='')

    @property
    def split_raid(self):
        return self.raid_controler.split('\n')

    @classmethod
    def data_products_to_filter(cls, querySet='') -> Dict:

        if querySet:
            motherboards = querySet
        else:
            motherboards = Motherboard.objects.all()

        return filter_motherboards(motherboards)


class Cpu(Inherit):
    cooler = models.CharField(default='', max_length=20)
    socket = models.CharField(max_length=50, default='')
    cores_num = models.IntegerField(default=0)
    threat_num = models.CharField(default='', max_length=20)
    clock_frequency = models.CharField(default='', max_length=20)
    supported_memory = models.CharField(default='', max_length=20)

    @classmethod
    def data_products_to_filter(cls, querySet='') -> Dict:

        if querySet:
            cpus = querySet
        else:
            cpus = Cpu.objects.all()

        return filter_cpus(cpus)


class Tv(Inherit):
    diagonal = models.CharField(max_length=20, default='')
    matrix_type = models.CharField(max_length=20, default='')
    resolution = models.CharField(max_length=50, default='')
    curved = models.CharField(max_length=10, default='No')
    hdr = models.CharField(max_length=10, default='No')
    refresh_rate = models.CharField(max_length=50, default='')
    smart_tv = models.CharField(max_length=10, default='No')
    wifi = models.CharField(max_length=10, default='No')
    bluetooth = models.CharField(max_length=10, default='No')
    hdmi_ports = models.IntegerField(default=0)
    usb_ports = models.IntegerField(default=0)
    energy_class = models.CharField(max_length=10, default='')
    power_consumption = models.CharField(max_length=50, default='')

    @classmethod
    def data_products_to_filter(cls, querySet='') -> Dict:

        if querySet:
            tvs = querySet
        else:
            tvs = Tv.objects.all()

        return filter_tvs(tvs)



class Headphones(Inherit):
    bluetooth_range = models.CharField(max_length=50, default='', blank=True, null=True)
    jack = models.CharField(max_length=50, default='', blank=True, null=True)
    cable_lenght = models.CharField(max_length=50, default='', blank=True, null=True)
    microphone = models.BooleanField(default=False)
    work_time = models.CharField(max_length=50, default='', blank=True, null=True)
    connection = models.CharField(max_length=50, default='')

    @classmethod
    def data_products_to_filter(cls, querySet='') -> Dict:

        if querySet:
            headphones = querySet
        else:
            headphones = Headphones.objects.all()

        return filter_headphones(headphones)



class Routers(Inherit):
    wifi = models.CharField(default='', max_length=100, blank=True, null=True)
    case = models.CharField(default='', max_length=100, blank=True, null=True)
    vpn = models.CharField(default='', max_length=100, blank=True, null=True)
    encryption_standard = models.CharField(default='', max_length=50, blank=True, null=True)
    wan_ports = models.CharField(max_length=100, default='')
    lan_ports = models.CharField(max_length=100, default='')
    usb_ports = models.IntegerField(default=0)
    sim = models.BooleanField(default=False)
    antennas = models.IntegerField(default=0, blank=True, null=True)
    wifi_2_4ghz_speed = models.CharField(default='', max_length=100, blank=True, null=True)
    wifi_5ghz_speed = models.CharField(default='', max_length=100, blank=True, null=True)


    @classmethod
    def data_products_to_filter(cls, querySet='') -> Dict:

        if querySet:
            routers = querySet
        else:
            routers = Routers.objects.all()

        return filter_routers(routers)


class Reviews(models.Model):

    product = models.ForeignKey(MainProductDatabase, on_delete=models.CASCADE)
    review = models.TextField(max_length=5000, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    stars = models.IntegerField(default=1)
    checked_by_employer = models.BooleanField(default=False)
    question_checked_by_employer = models.BooleanField(default=False)

    class Meta:
        unique_together = [['product', 'user']]

    def __str__(self) -> str:
        return f'Review of {self.product.name}/ Product ID: {self.product.id}'

    @property
    def get_time(self) -> str:
        return str(self.date)

    @property
    def get_range_stars(self) -> List[bool]:
        """ return array with representation (True or False) of stars given to a product """

        return [True if num in [el for el in range(1, self.stars+1)] else False for num in range(1, 6)]


class Questions(models.Model):

    product = models.ForeignKey(MainProductDatabase, on_delete=models.CASCADE)
    question = models.CharField(max_length=5000, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='User')
    name = models.CharField(max_length=50, default='')
    date = models.DateField(auto_now_add=True)
    checked_by_employer = models.BooleanField(default=False)
    employer_reply = models.CharField(max_length=5000, blank=True, null=True)

    def __str__(self) -> str:
        return f'Question of {self.product.name}/ Product ID: {self.product.id}'


    @property
    def get_time(self) -> str:
        return str(self.date)

