from django.db import models
from django.db.models.base import Model
from django.utils.safestring import mark_safe

import os
import codecs


class Phones(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField(max_length=10)
    pieces = models.IntegerField()
    day_product = models.BooleanField(default=False)
    promotion = models.FloatField(blank=True, null=True)
    ram = models.IntegerField()
    memory = models.IntegerField()
    modem = models.IntegerField()
    color = models.CharField(max_length=40)
    describe = models.CharField(max_length=30000, null=True)
    main_photo = models.ImageField(upload_to=f'phones/{name}', null=True, blank=True)
    content_photo1 = models.ImageField(upload_to=f'phones/{name}', null=True, blank=True)
    content_photo2 = models.ImageField(upload_to=f'phones/{name}', null=True, blank=True)
    content_photo3 = models.ImageField(upload_to=f'phones/{name}', null=True, blank=True)
    html_file = models.FileField(upload_to="media", default="")
    producent = models.CharField(max_length=100)
    producent_code = models.CharField(max_length=100)
    ean = models.IntegerField()
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
    opinions = models.CharField(max_length=5000)
    
    CHOICES = [
        ("Laptops", "Laptops"),
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
    
    cattegory = models.CharField(choices=CHOICES, max_length=50, default='')
    

    def __str__(self) -> str:
        return self.name
    
    def render_html(self):
        path = self.html_file.path
        if os.path.exists(path):
            html_string = codecs.open(path, 'r').read()
            return mark_safe(html_string)
        return None
    

    
class MainProductDatabase(models.Model):
    main_product_data = models.OneToOneField(Phones, on_delete=models.CASCADE)
    ean = models.IntegerField(null=True, blank=True)

    
    def __str__(self) -> str:
        return f'Product: {self.main_product_data.name}'