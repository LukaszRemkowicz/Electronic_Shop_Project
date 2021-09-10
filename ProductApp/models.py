from typing import Any, Dict, List, Tuple
import os
import codecs
import math

from django.db import models, reset_queries
from django.db.models.base import Model
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User


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


class Phones(models.Model):
    
    name = models.CharField(max_length=20, default='')
    model = models.CharField(max_length=20, null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    pieces = models.IntegerField()
    promotion = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
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
    battery = models.IntegerField()
    high = models.CharField(max_length=10)
    width = models.CharField(max_length=10)
    deep = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)
    opinions = models.CharField(max_length=5000, blank=True, null=True)
    reviews = models.CharField(max_length=5000, blank=True, null=True)
    
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
    
    main_photo = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=20, default='')
    model = models.CharField(max_length=20, null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    pieces = models.IntegerField()
    promotion = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    color = models.CharField(max_length=40)
    resolution = models.CharField(max_length=20)
    refresh_rate = models.IntegerField()
    power_consumption = models.IntegerField()
    describe = models.CharField(max_length=30000, null=True)
    main_photo = models.ImageField(upload_to=f'monitors', null=True, blank=True)
    content_photo1 = models.ImageField(upload_to=f'monitors', null=True, blank=True)
    content_photo2 = models.ImageField(upload_to=f'monitors', null=True, blank=True)
    content_photo3 = models.ImageField(upload_to=f'monitors', null=True, blank=True)
    html_file = models.FileField(upload_to="monitors", default="", null=True, blank=True)
    producent = models.CharField(max_length=100)
    producent_code = models.CharField(max_length=100)
    ean = models.IntegerField(unique=True)
    distribution = models.CharField(max_length=10, default='EU')
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
    
    img = models.ImageField(null=True, blank=True, upload_to='products_pic')
    name = models.CharField(max_length=100, default='')
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    pieces = models.IntegerField(default=0)
    promotion = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    
    phones_product_data = models.OneToOneField(Phones, on_delete=models.CASCADE, null=True, blank=True)
    monitors_product_data = models.OneToOneField(Monitors, on_delete=models.CASCADE, default='', null=True, blank=True)
    laptops_product_data = models.OneToOneField('Laptops', on_delete=models.CASCADE, default='', null=True, blank=True)
    
    ean = models.IntegerField(null=True, blank=True, unique=True)
    product_of_the_day = models.BooleanField(default=False)
    cattegory =  models.CharField(choices=CHOICES, max_length=50, default='')
    color = models.CharField(max_length=100, default='')

    def __str__(self) -> str:
        return f'Product: {self.name}'
    
    @property
    def get_img(self) -> str:
        try:
            url = self.img.url
        except:
            url=''
        
        return url
    
    @property
    def get_star_avg(self) -> Tuple[str, List[bool]]:
        """ Method to get product review avarage """
        
        opinions = len(ReviewAndQuestions.objects.filter(product=self.id))
        stars = sum([element.stars for element in ReviewAndQuestions.objects.all()])
        
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
        
        stars = [element.stars for element in ReviewAndQuestions.objects.filter(product=self.id)]
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
        return len(ReviewAndQuestions.objects.filter(product=self.id))
        

    
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


class ReviewAndQuestions(models.Model):
    
    product = models.ForeignKey(MainProductDatabase, on_delete=models.CASCADE)
    review = models.CharField(max_length=5000)
    question = models.CharField(max_length=5000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_created=True)
    stars = models.IntegerField(default=1)
    checked = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f'Review of {self.product.name}'
    
    @property
    def get_time(self) -> str:
        return str(self.date) 
    
    @property
    def get_range_stars(self) -> List[bool]:
        """ return array with representation (True or False) of stars given to a product """
        
        return [True if num in [el for el in range(1, self.stars+1)] else False for num in range(1, 6)]
    
        
    