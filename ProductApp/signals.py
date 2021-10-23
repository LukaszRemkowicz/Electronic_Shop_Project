from functools import wraps

from django.db.models.signals import post_save
from django.dispatch import receiver

from . import models, utils


skip_signals = False

def skip_signal():
    def _skip_signal(signal_func):
        @wraps(signal_func)
        def _decorator(sender, instance, **kwargs):
            if skip_signals == True:
                return None
            return signal_func(sender, instance, **kwargs)
        return _decorator
    return _skip_signal


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

    global skip_signals

    if created:
        """ check if ean code is already in the DB """

        product_ean = models.MainProductDatabase.objects.filter(ean=instance.ean).exists()

        if product_ean:
            pass

        else:

            skip_signals = True
            product = utils.choose_model(instance.__class__.__name__, instance)
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
                product.img = instance.main_photo
                product.second_img = instance.second_photo
                product.third_img = instance.third_photo
            except Exception as e:
                print('Oops, something went wrong: ', e)
                pass

            skip_signals = False
    else:
        """ update product if not created"""

        product = models.MainProductDatabase.objects.get(ean=instance.ean)

        print(product.img)
        print(utils.get_product(instance.__class__.__name__, instance).main_photo)

        try:

            if product.name != utils.get_product(instance.__class__.__name__, instance).name:
                product.name = instance.name
                product.save()
            elif product.price != utils.get_product(instance.__class__.__name__, instance).price:
                product.price = instance.price
                product.save()
            elif product.pieces != utils.get_product(instance.__class__.__name__, instance).pieces:
                product.pieces = instance.pieces
                product.save()
            elif product.ean != utils.get_product(instance.__class__.__name__, instance).ean:
                product.ean = instance.ean
                product.save()
            elif product.product_of_the_day != utils.get_product(instance.__class__.__name__, instance).product_of_the_day:
                product.product_of_the_day = instance.product_of_the_day
                product.save()
            elif product.cattegory != utils.get_product(instance.__class__.__name__, instance).cattegory:
                product.cattegory = instance.cattegory
                product.save()
            elif product.color != utils.get_product(instance.__class__.__name__, instance).color:
                product.color = instance.color
                product.save()
            elif product.img != utils.get_product(instance.__class__.__name__, instance).main_photo:
                product.img = instance.main_photo
                product.save()
            elif product.second_img != utils.get_product(instance.__class__.__name__, instance).second_photo:
                product.second_img = instance.second_photo
                product.save()
            elif product.third_img != utils.get_product(instance.__class__.__name__, instance).third_photo:
                product.third_img = instance.third_photo
                product.save()

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
    """ save main product if created """

    global skip_signals

    product_ean = models.MainProductDatabase.objects.filter(ean=instance.ean).exists()
    if product_ean:
        pass
    else:
        print(instance)

        skip_signals = True
        instance.mainproductdatabase.save()
        skip_signals = False


@receiver(post_save, sender=models.MainProductDatabase)
@skip_signal()
def update_product(sender, instance, created, **kwargs):
    """ Update product if main product changed """

    global skip_signals

    if not created:

        product = models.MainProductDatabase.objects.get(ean=instance.ean)

        skip_signals = True
        instance_obj = utils.try_to_get_product(product, instance)

        if product.name != instance_obj.name:
            instance_obj.name = product.name
            instance_obj.save()
        elif product.price != instance_obj.price:
            instance_obj.price = product.price
            instance_obj.save()
        elif product.pieces != instance_obj.pieces:
            instance_obj.pieces = product.pieces
            instance_obj.save()
        elif product.ean != instance_obj.ean:
            instance_obj.ean = product.ean
            instance_obj.save()
        elif product.cattegory != instance_obj.cattegory:
            instance_obj.cattegory = product.cattegory
            instance_obj.save()
        elif product.color != instance_obj.color:
            instance_obj.color = product.color
            instance_obj.save()

        skip_signals = False