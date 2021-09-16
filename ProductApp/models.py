from typing import Any, Dict, List, Tuple
import os
import codecs
import math

from django.db import models, reset_queries
from django.db.models.base import Model
from django.db.models.expressions import F
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist 


CHOICES = [
        ("Laptops", "Laptops"),
        ("Phones", 'Phones'),
        ("PC", "PC"),
        ("Monitor", "Monitor"),
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


class Inherit(models.Model):
    
    name = models.CharField(max_length=60, default='')
    model = models.CharField(max_length=20, null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    pieces = models.IntegerField(default=0)
    promotion = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    producent = models.CharField(max_length=100, default='')
    producent_code = models.CharField(max_length=100, default='')
    ean = models.BigIntegerField(unique=True, null=True)
    color = models.CharField(max_length=40, null=True, blank=True)
    distribution = models.CharField(max_length=10, default='EU')
    cattegory = models.CharField(choices=CHOICES, max_length=50, default='')
    describe = models.CharField(max_length=30000, null=True, blank=True, default='')
    width = models.FloatField(blank=True, null=True)
    deep = models.FloatField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    high = models.CharField(max_length=10, blank=True, null=True)
    
    main_photo = models.ImageField(upload_to='monitors', null=True, blank=True)
    content_photo1 = models.ImageField(upload_to='monitors', null=True, blank=True)
    content_photo2 = models.ImageField(upload_to='monitors', null=True, blank=True)
    content_photo3 = models.ImageField(upload_to='monitors', null=True, blank=True)
    html_file = models.FileField(upload_to="monitors", default="", null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name
    
    def render_html(self) -> Any:
        path = self.html_file.path
        if os.path.exists(path):
            html_string = codecs.open(path, 'r').read()
            return mark_safe(html_string)
        return None
    
    class Meta:
        abstract = True
        
    
class MainProductDatabase(models.Model):
    
    img = models.ImageField(null=True, blank=True, upload_to='products_pic')
    name = models.CharField(max_length=100, default='')
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    pieces = models.IntegerField(default=0)
    promotion = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    product_of_the_day = models.BooleanField(default=False)
    
    phones_product_data = models.OneToOneField('Phones', on_delete=models.CASCADE, null=True, blank=True)
    monitors_product_data = models.OneToOneField('Monitors', on_delete=models.CASCADE, null=True, blank=True)
    laptops_product_data = models.OneToOneField('Laptops', on_delete=models.CASCADE, default='', null=True, blank=True)
    pc_product_data = models.OneToOneField('Pc', on_delete=models.CASCADE, default='', null=True, blank=True)
    accesories_for_laptop = models.OneToOneField('AccesoriesForLaptops', on_delete=models.CASCADE, default='', null=True, blank=True)
    ssd_product_data = models.OneToOneField('Ssd', on_delete=models.CASCADE, default='', null=True, blank=True)
    graph_product_data = models.OneToOneField('Graphs', on_delete=models.CASCADE, default='', null=True, blank=True)
    ram_product_data = models.OneToOneField('Ram', on_delete=models.CASCADE, default='', null=True, blank=True)
    pendrive_product_data = models.OneToOneField('Pendrives', on_delete=models.CASCADE, default='', null=True, blank=True)
    switch_product_data = models.OneToOneField('Switches', on_delete=models.CASCADE, default='', null=True, blank=True)
    motherboard_product_data = models.OneToOneField('Motherboard', on_delete=models.CASCADE, default='', null=True, blank=True)
    cpu_product_data = models.OneToOneField('Cpu', on_delete=models.CASCADE, default='', null=True, blank=True)
    tv_product_data = models.OneToOneField('Tv', on_delete=models.CASCADE, default='', null=True, blank=True)
    headphone_product_data = models.OneToOneField('Headphones', on_delete=models.CASCADE, default='', null=True, blank=True)
    router_product_data = models.OneToOneField('Routers', on_delete=models.CASCADE, default='', null=True, blank=True)
    
    ean = models.BigIntegerField(null=True, blank=True, unique=True)
    cattegory =  models.CharField(choices=CHOICES, max_length=50, default='')
    color = models.CharField(max_length=100, default='', blank=True, null=True)

    def __str__(self) -> str:
        return f'Product: {self.name}'
    
    @property
    def get_img(self) -> str:
        try:
            url = self.img.url
        except ObjectDoesNotExist:
            url=''
        
        return url
    
    @property
    def get_star_avg(self) -> Tuple[str, List[bool]]:
        """ Method to get product review avarage """
        
        opinions = len(Reviews.objects.filter(product=self.id, checked_by_employer=True))
        stars = sum([element.stars for element in Reviews.objects.filter(checked_by_employer=True)])
        
        result = stars/opinions
        frac, whole = math.modf(result)
        
        ranger = [True if num  in [element for element in range(1, int(whole) +1 )] else False for num in range(1, int(6))]
           
        if frac > 0:
            return str(result), ranger
        else:
            return str(int(whole)), ranger   
        
    @property
    def get_stars(self) -> Dict[str, int]:
        """ Help method to generate progress bars """
        
        stars = [element.stars for element in Reviews.objects.filter(product=self.id, checked_by_employer=True)]
        stars_dict = {key:0 for key in range(1, 6)}
        
        for element in stars:
            if element not in stars_dict:
                stars_dict[element] = 1
            else:
                stars_dict[element] += 1
                
        for key, value in stars_dict.items():
            percentage = (100*value) / len(stars)
            stars_dict[key] = (value, int(percentage))
        
        return stars_dict

    @property
    def get_num_of_reviews(self) -> int:
        return len(Reviews.objects.filter(product=self.id, checked_by_employer=True))
        

class Phones(Inherit):
    
    ram = models.IntegerField(default=0)
    memory = models.IntegerField(default=0)
    modem = models.IntegerField(default=0)

    waterproof = models.BooleanField(default=False)
    system = models.CharField(max_length=10, default='')
    processor = models.CharField(max_length=20, default='')
    cpu_clock = models.CharField(max_length=100, default='')
    memory_card = models.CharField(max_length=10, default='')
    usb = models.CharField(max_length=10, default='')
    audio_jack = models.CharField(max_length=10, default='')
    screen = models.CharField(max_length=30, default='')
    screen_diagonal = models.CharField(max_length=10, default='')
    battery = models.IntegerField(default=0)
    
    
class Monitors(Inherit):

    resolution = models.CharField(max_length=20, default='')
    refresh_rate = models.IntegerField(default=0)
    power_consumption = models.IntegerField(default=0)
    screen = models.CharField(max_length=30, default='')
    screen_diagonal = models.CharField(max_length=10, default='')
        
    
class Laptops(Inherit):
    
    resolution = models.CharField(max_length=20, default='')
    energy_time = models.IntegerField(default=0)
    battery = models.IntegerField(default=0)
    screen = models.CharField(max_length=30, default='')
    screen_diagonal = models.CharField(max_length=10, default='')
    system = models.CharField(max_length=20, default='')
    graph = models.CharField(max_length=20, default='')
    disc = models.IntegerField(default=0)
    ram = models.IntegerField(default=0)
    ram_model = models.CharField(max_length=20, default='')
    p_c_i_e = models.IntegerField(default=0)
    wifi = models.CharField(max_length=20, default='')
    bluetooth = models.CharField(max_length=10, default='Yes')
    
     
class Pc(Inherit):
    
    resolution = models.CharField(max_length=20, default='')
    system = models.CharField(max_length=20, default='')
    graph = models.CharField(max_length=20, default='')
    disc = models.IntegerField(default=0)
    ram = models.IntegerField(default=0)
    ram_model = models.CharField(max_length=20, default='')
    p_c_i_e = models.IntegerField(default=0)
    wifi = models.CharField(max_length=20, default='')
    bluetooth = models.CharField(max_length=10, default='')
    

class AccesoriesForLaptops(Inherit):
    pass


class Ssd(Inherit):
    
    format = models.CharField(max_length=30, default='')
    capacity = models.IntegerField(default=0)
    reading_speed = models.IntegerField(default=0)
    writing_speed = models.IntegerField(default=0)
    work_time = models.IntegerField(default=0)
    
     
class Graphs(Inherit):
    
    chipset = models.CharField(max_length=30, default='')
    chipset_producent = models.CharField(max_length=50, default='')
    phisic_lenght = models.IntegerField(default=0)
    ram = models.IntegerField(default=0)
    ram_type = models.CharField(max_length=50, default='')
    core_clock = models.IntegerField(default=0)
    connector_type = models.CharField(max_length=60, default='')
    

class Ram(Inherit):
    
    capacity = models.IntegerField(default=0)
    frequency = models.IntegerField(default=0)
    module_number = models.IntegerField(default=0)
    profile = models.CharField(max_length=30, default='')
    voltage = models.FloatField(default=0)
    lights = models.CharField(max_length=20, default='')
    

class Pendrives(Inherit):
    
    capacity = models.IntegerField(default=0)
    connector = models.CharField(max_length=20, default='')
    case = models.CharField(max_length=50, default='')
    

class Switches(Inherit):
    
    num_of_connectors = models.IntegerField(default=0)
    num_of_poe = models.IntegerField(default=0)
    case_kind = models.CharField(max_length=40, default='')
    manageable = models.BooleanField(default=False)
    ports_num = models.IntegerField(default=4)
    bus_speed = models.IntegerField(default=0)
    

class Motherboard(Inherit):
    chipset = models.CharField(max_length=50, default='')
    processor_socket = models.CharField(max_length=50, default='')
    ram_slots = models.IntegerField(default=4)
    card_standard = models.CharField(max_length=20, default='')
    raid_controler = models.CharField(max_length=100, default='')
    ram = models.CharField(max_length=10, default='')
    ram_max_cap = models.IntegerField(default=0)
    graph_integrated = models.BooleanField(default=False)
    sound = models.CharField(max_length=20, default='')
    network_card = models.CharField(max_length=50, default='')
    wifi = models.BooleanField(default=False)
    connections = models.CharField(max_length=200, default='')
    
    def get_connections(self):
        return self.connections.replace(',', ',\n')


class Cpu(Inherit):
    cooler = models.BooleanField(default=False)
    socket = models.CharField(max_length=50, default='')
    cores_num = models.IntegerField(default=0)
    threat_num = models.IntegerField(default=0)
    clock_frequency = models.FloatField(default=0)
    supported_memory = models.CharField(default='', max_length=20)
    

class Tv(Inherit):
    diagonal = models.IntegerField(default=0)
    matrix_type = models.CharField(max_length=20, default='')
    resolution = models.CharField(max_length=50, default='')
    curved = models.BooleanField(default=False)
    hdr = models.BooleanField(default=False)
    refresh_rate = models.IntegerField(default=0)
    smart_tv = models.BooleanField(default=False)
    wifi = models.BooleanField(default=False)
    bluetooth = models.BooleanField(default=False)
    hdmi_ports = models.IntegerField(default=0)
    usb_ports = models.IntegerField(default=0)
    energy_class = models.IntegerField(default=0)
    power_consumption = models.IntegerField(default=0)
    

class Headphones(Inherit):
    bluetooth = models.BooleanField(default=False)
    bluetooth_range = models.IntegerField(default=0, blank=True, null=True)
    cable = models.BooleanField(default=False)
    jack = models.CharField(max_length=50, default='', blank=True, null=True)
    cable_lenght = models.IntegerField(default=0, blank=True, null=True)
    microphone = models.BooleanField(default=False)
    work_time = models.IntegerField(default=0, blank=True, null=True)
    
    

class Routers(Inherit):
    wifi = models.BooleanField(default=False)
    wifi_standard = models.CharField(default='', max_length=100, blank=True, null=True)
    portable = models.BooleanField(default=False)
    vpn = models.BooleanField(default=False)
    encryption_standard = models.CharField(default='', max_length=50) 
    wan_ports = models.CharField(max_length=100, default='')
    lan_ports = models.CharField(max_length=100, default='')
    usb_ports = models.IntegerField(default=0)
    sim = models.BooleanField(default=False)
    antennas = models.BooleanField(default=False)
    antennas_num = models.IntegerField(default=0, blank=True, null=True)
    wifi_2_4ghz_speed = models.CharField(default='', max_length=100, blank=True, null=True)
    wifi_5ghz_speed = models.CharField(default='', max_length=100, blank=True, null=True)


class Reviews(models.Model):
    
    product = models.ForeignKey(MainProductDatabase, on_delete=models.CASCADE)
    review = models.CharField(max_length=5000, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    stars = models.IntegerField(default=1)
    checked_by_employer = models.BooleanField(default=False)
    question_checked_by_employer = models.BooleanField(default=False)
    
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    checked_by_employer = models.BooleanField(default=False)
    employer_reply = models.CharField(max_length=5000, blank=True, null=True)
    
    def __str__(self) -> str:
        return f'Question of {self.product.name}/ Product ID: {self.product.id}'
    
    
    @property
    def get_time(self) -> str:
        return str(self.date) 