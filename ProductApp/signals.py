from django.db.models.signals import post_save
from django.dispatch import receiver

from . import models

def choose_model(model, instance):
    """ create objects for specific model """
    
    if model == "Phones":
        return models.MainProductDatabase.objects.create(phones_product_data=instance)
    elif model == "Monitors":
        return models.MainProductDatabase.objects.create(monitors_product_data=instance)
    elif model == 'Laptops':
        return models.MainProductDatabase.objects.create(laptops_product_data=instance)
    elif model == 'Pc':
        return models.MainProductDatabase.objects.create(pc_product_data=instance)
    elif model == 'AccesoriesForLaptops':
        return models.MainProductDatabase.objects.create(AccesoriesForLaptops_data=instance)
    elif model == 'Ssd':
        return models.MainProductDatabase.objects.create(ssd_product_data=instance)
    elif model == 'Graphs':
        return models.MainProductDatabase.objects.create(graphs_product_data=instance)
    elif model == 'Ram':
        return models.MainProductDatabase.objects.create(ram_product_data=instance)
    elif model == 'Pendrives':
        return models.MainProductDatabase.objects.create(pendrive_product_data=instance)
    elif model == 'Switches':
        return models.MainProductDatabase.objects.create(stwitch_product_data=instance)
    elif model == 'Motherboard':
        return models.MainProductDatabase.objects.create(motherboard_product_data=instance)
    elif model == 'Cpu':
        return models.MainProductDatabase.objects.create(cpu_product_data=instance)
    elif model == 'Tv':
        return models.MainProductDatabase.objects.create(tv_product_data=instance)
    elif model == 'Headphones':
        return models.MainProductDatabase.objects.create(headphones_product_data=instance)
    elif model == 'Routers':
        return models.MainProductDatabase.objects.create(routers_product_data=instance)
    

@receiver(post_save, sender=models.Phones)
@receiver(post_save, sender=models.Monitors)
@receiver(post_save, sender=models.Laptops)
@receiver(post_save, sender=models.Pc)
@receiver(post_save, sender=models.AccesoriesForLaptops)
@receiver(post_save, sender=models.Ssd)
@receiver(post_save, sender=models.Graphs)
@receiver(post_save, sender=models.Ram)
@receiver(post_save, sender=models.Pendrives)
@receiver(post_save, sender=models.Routers)
@receiver(post_save, sender=models.Switches)
@receiver(post_save, sender=models.Motherboard)
@receiver(post_save, sender=models.Cpu)
@receiver(post_save, sender=models.Tv)
@receiver(post_save, sender=models.Headphones)
def create_product(sender, instance, created, **kwargs):
    if created:
        
        """ check if ean code is already in the base """
        
        product_ean = models.MainProductDatabase.objects.filter(ean=instance.ean).exists()
        
        if product_ean:
            pass
        else:
            # SENDERS = {'Phones': lambda: MainProductDatabase.objects.create(phones_product_data=instance), 
            #            'Monitors': lambda: MainProductDatabase.objects.create(monitors_product_data=instance)}
            # product = SENDERS[instance.__class__.__name__]()
            product = choose_model(instance.__class__.__name__, instance)
            product.ean = instance.ean
            product.cattegory = instance.cattegory
            product.name = instance.name
            product.price = instance.price
            product.pieces = instance.pieces
            product.color = instance.color
            try:
                product.promotion = instance.promotion
            except:
                pass
            try:
                product.main_photo = instance.img
            except:
                pass
            
            
    
        
        
@receiver(post_save, sender=models.Phones)
@receiver(post_save, sender=models.Monitors)
@receiver(post_save, sender=models.Laptops)
@receiver(post_save, sender=models.Pc)
@receiver(post_save, sender=models.AccesoriesForLaptops)
@receiver(post_save, sender=models.Ssd)
@receiver(post_save, sender=models.Graphs)
@receiver(post_save, sender=models.Ram)
@receiver(post_save, sender=models.Pendrives)
@receiver(post_save, sender=models.Routers)
@receiver(post_save, sender=models.Switches)
@receiver(post_save, sender=models.Motherboard)
@receiver(post_save, sender=models.Cpu)
@receiver(post_save, sender=models.Tv)
@receiver(post_save, sender=models.Headphones)
def save_product(sender, instance, **kwargs):
    product_ean = models.MainProductDatabase.objects.filter(ean=instance.ean).exists()
    if product_ean:
        pass
    else:
        instance.mainproductdatabase.save()