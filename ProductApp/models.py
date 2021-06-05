from django.db import models
from django.db.models.base import Model
from django.utils.safestring import mark_safe
from typing import Any


import os
import codecs

CHOICES = [
        ("Laptops", "Laptops"),
        ("phones", 'phones'),
        ("PC", "PC"),
        ("Monitor", "Monitor"),
        ("Accesories_for_laptops", "Accesories_for_laptops"),
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


class Phones(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField(max_length=10)
    pieces = models.IntegerField()
    promotion = models.FloatField(blank=True, null=True)
    ram = models.IntegerField()
    memory = models.IntegerField()
    modem = models.IntegerField()
    color = models.CharField(max_length=40)
    describe = models.CharField(max_length=30000, null=True)
    main_photo = models.ImageField(upload_to=f'phones', null=True, blank=True)
    content_photo1 = models.ImageField(upload_to=f'phones', null=True, blank=True)
    content_photo2 = models.ImageField(upload_to=f'phones', null=True, blank=True)
    content_photo3 = models.ImageField(upload_to=f'phones', null=True, blank=True)
    html_file = models.FileField(upload_to="phones", default="", blank=True, null=True)
    producent = models.CharField(max_length=100)
    producent_code = models.CharField(max_length=100)
    ean = models.IntegerField(unique=True)
    waterproof = models.BooleanField(default=False)
    distibution = models.CharField(max_length=10)
    system = models.CharField(max_length=10)
    processor = models.CharField(max_length=20)
    cpu_clock = models.CharField(max_length=100)
    memory_card = models.CharField(max_length=10)
    usb = models.CharField(max_length=10)
    audio_jack = models.CharField(max_length=10)
    screen = models.CharField(max_length=30)
    screen_diagonal = models.CharField(max_length=10)
    battery = models.CharField(max_length=10)
    high = models.CharField(max_length=10)
    width = models.CharField(max_length=10)
    deep = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)
    opinions = models.CharField(max_length=5000, blank=True, null=True)
    
    cattegory = models.CharField(choices=CHOICES, max_length=50, default='')
    

    def __str__(self) -> str:
        return self.name
    
    def render_html(self) -> Any:
        path = self.html_file.path
        if os.path.exists(path):
            html_string = codecs.open(path, 'r').read()
            return mark_safe(html_string)
        return None
    
    
class Monitors(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField(max_length=10)
    pieces = models.IntegerField()
    promotion = models.FloatField(blank=True, null=True)
    color = models.CharField(max_length=40)
    resolution = models.CharField(max_length=20)
    refresh_rate = models.CharField(max_length=10)
    Power_consumption = models.CharField(max_length=10)
    describe = models.CharField(max_length=30000, null=True)
    main_photo = models.ImageField(upload_to=f'monitors', null=True, blank=True)
    content_photo1 = models.ImageField(upload_to=f'monitors', null=True, blank=True)
    content_photo2 = models.ImageField(upload_to=f'monitors', null=True, blank=True)
    content_photo3 = models.ImageField(upload_to=f'monitors', null=True, blank=True)
    html_file = models.FileField(upload_to="monitors", default="", null=True, blank=True)
    producent = models.CharField(max_length=100)
    producent_code = models.CharField(max_length=100)
    ean = models.IntegerField(unique=True)
    distibution = models.CharField(max_length=10)
    screen = models.CharField(max_length=30)
    screen_diagonal = models.CharField(max_length=10)
    high = models.CharField(max_length=10)
    width = models.CharField(max_length=10)
    deep = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)
    opinions = models.CharField(max_length=5000, null=True, blank=True)
    
    
    cattegory = models.CharField(choices=CHOICES, max_length=50, default='')
    

    def __str__(self) -> str:
        return self.name
    
    def render_html(self) -> Any:
        path = self.html_file.path
        if os.path.exists(path):
            html_string = codecs.open(path, 'r').read()
            return mark_safe(html_string)
        return None
    

    
class MainProductDatabase(models.Model):
    phones_product_data = models.OneToOneField(Phones, on_delete=models.CASCADE, null=True, blank=True)
    monitors_product_data = models.OneToOneField(Monitors, on_delete=models.CASCADE, default='')
    ean = models.IntegerField(null=True, blank=True, unique=True)
    product_of_the_day = models.BooleanField(default=False)
    cattegory = models.CharField(max_length=50, default='')

    def __str__(self) -> str:
        return f'Product: {self.monitors_product_data.name}'
    
    
class Laptops(models.Model):
    pass
     
class Pc(models.Model):
    pass

class AccesoriesForLaptops(models.Model):
    pass

class Ssd(models.Model):
    pass
     
class Graphs(models.Model):
    pass

class Ram(models.Model):
    pass

class Pendrives(models.Model):
    pass

class Switches(models.Model):
    pass
     
class Motherboard(models.Model):
    pass

class Cpu(models.Model):
    pass

class Tv(models.Model):
    pass

class Headphones(models.Model):
    pass

class Routers(models.Model):
    pass

