from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import (MainProductDatabase, Phones, 
                     Monitors, Laptops, Pc, AccesoriesForLaptops, 
                     Ssd, Graphs,Ram, Pendrives, Routers, Switches,
                     Motherboard, Cpu, Tv, Headphones)


def choose_model(model, instance):
    """ help function for difference models """
    if model == "Phones":
        return MainProductDatabase.objects.create(phones_product_data=instance)
    elif model == "Monitors":
        return MainProductDatabase.objects.create(monitors_product_data=instance)

@receiver(post_save, sender=Phones)
@receiver(post_save, sender=Monitors)
@receiver(post_save, sender=Laptops)
@receiver(post_save, sender=Pc)
@receiver(post_save, sender=AccesoriesForLaptops)
@receiver(post_save, sender=Ssd)
@receiver(post_save, sender=Graphs)
@receiver(post_save, sender=Ram)
@receiver(post_save, sender=Pendrives)
@receiver(post_save, sender=Routers)
@receiver(post_save, sender=Switches)
@receiver(post_save, sender=Motherboard)
@receiver(post_save, sender=Cpu)
@receiver(post_save, sender=Tv)
@receiver(post_save, sender=Headphones)
def create_product(sender, instance, created, **kwargs):
    if created:
        
        """ check if ean code is already in the base """
        
        product_ean = MainProductDatabase.objects.filter(ean=instance.ean).exists()
        
        if product_ean:
            pass
        else:
            # SENDERS = {'Phones': lambda: MainProductDatabase.objects.create(phones_product_data=instance), 
            #            'Monitors': lambda: MainProductDatabase.objects.create(monitors_product_data=instance)}
            # product = SENDERS[instance.__class__.__name__]()
            product = choose_model(instance.__class__.__name__, instance)
            product.ean = instance.ean
            product.cattegory = instance.cattegory
            
    
        
        
@receiver(post_save, sender=Phones)
@receiver(post_save, sender=Monitors)
@receiver(post_save, sender=Laptops)
@receiver(post_save, sender=Pc)
@receiver(post_save, sender=AccesoriesForLaptops)
@receiver(post_save, sender=Ssd)
@receiver(post_save, sender=Graphs)
@receiver(post_save, sender=Ram)
@receiver(post_save, sender=Pendrives)
@receiver(post_save, sender=Routers)
@receiver(post_save, sender=Switches)
@receiver(post_save, sender=Motherboard)
@receiver(post_save, sender=Cpu)
@receiver(post_save, sender=Tv)
@receiver(post_save, sender=Headphones)
def save_product(sender, instance, **kwargs):
    product_ean = MainProductDatabase.objects.filter(ean=instance.ean).exists()
    if product_ean:
        pass
    else:
        instance.mainproductdatabase.save()