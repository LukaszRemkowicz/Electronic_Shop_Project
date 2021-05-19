from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import MainProductDatabase, Phones


@receiver(post_save, sender=Phones)
def create_product(sender, instance, created, **kwargs):
    print(type(instance))
    print(Phones.ean)
    print(instance.ean)
    print(created)
    if created:
        MainProductDatabase.objects.create(main_product_data=instance)
        
        
@receiver(post_save, sender=Phones)
def save_product(sender, instance, **kwargs):
    print(type(instance))
    instance.mainproductdatabase.save()