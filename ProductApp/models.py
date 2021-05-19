from django.db import models
from django.db.models.base import Model


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
    

    def __str__(self) -> str:
        return self.name
    

    
class MainProductDatabase(models.Model):
    main_product_data = models.OneToOneField(Phones, on_delete=models.CASCADE)
    ean = models.IntegerField(null=True, blank=True)

    
    def __str__(self) -> str:
        return f'Product: {self.main_product_data.name}'