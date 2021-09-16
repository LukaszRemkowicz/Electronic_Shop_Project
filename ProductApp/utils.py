from django.core.exceptions import ObjectDoesNotExist

from ProductApp import models

def filter_products(cattegory, product):
    if cattegory == 'Phones':
        product_model = product.phones_product_data.model
        
        same_products = models.MainProductDatabase.objects.filter(phones_product_data__model=product_model)
        same_products_data = {
            'items' : same_products, 
            'colors' : set([element.phones_product_data.color for element in same_products]),
            'memory' : set([element.phones_product_data.memory for element in same_products]),
            'ram' : set([element.phones_product_data.ram for element in same_products]),
            'battery' : set([element.phones_product_data.battery for element in same_products]),
            'items_id' : [element.id for element in same_products]
        }
                
        return same_products_data
    
    elif cattegory == 'Laptops':
        product_model = product.laptops_product_data.model
        return models.MainProductDatabase.objects.filter(laptops_product_data__model=product_model)
    
    elif cattegory == 'PC':
        product_model = product.pc_product_data.model
        return models.MainProductDatabase.objects.filter(pc_product_data__model=product_model)
    
    elif cattegory == 'Monitor':
        product_model = product.monitors_product_data.model
        return models.MainProductDatabase.objects.filter(monitors_product_data__model=product_model)
    
    elif cattegory == 'Accesories for laptops':
        product_model = product.laptop_accesories_data.model
        return models.MainProductDatabase.objects.filter(laptop_accesories_data__model=product_model)
    
    elif cattegory == 'SSD':
        product_model = product.ssd_product_model.model
        return models.MainProductDatabase.objects.filter(ssd_product_model__model=product_model)
    
    elif cattegory == 'Graphs':
        product_model = product.graphs_product_data.model
        return models.MainProductDatabase.objects.filter(graphs_product_data__model=product_model)
    
    elif cattegory == 'Ram':
        product_model = product.ram_product_data.model
        return models.MainProductDatabase.objects.filter(ram_product_data__model=product_model)
    
    elif cattegory == 'Pendrives':
        product_model = product.pendrives_product_model.model
        return models.MainProductDatabase.objects.filter(pendrives_product_model__model=product_model)
    
    elif cattegory == 'Routers':
        product_model = product.router_product_data.model
        return models.MainProductDatabase.objects.filter(router_product_data__model=product_model)
    
    elif cattegory == 'Switches':
        product_model = product.switches_product_model.model
        return models.MainProductDatabase.objects.filter(switches_product_model__model=product_model)
    
    elif cattegory == 'Motherboard':
        product_model = product.motherboards_product_model.model
        return models.MainProductDatabase.objects.filter(motherboards_product_model__model=product_model)
    
    elif cattegory == 'CPU':
        product_model = product.cpu_product_model.model
        return models.MainProductDatabase.objects.filter(cpu_product_model__model=product_model)
    
    elif cattegory == 'TV':
        product_model = product.tv_product_model.model
        return models.MainProductDatabase.objects.filter(tv_product_model__model=product_model)
    
    elif cattegory == 'Headphones':
        product_model = product.headphones_product_model.model
        return models.MainProductDatabase.objects.filter(headphones_product_model__model=product_model)
    
    
def find_new_product(product_items_list, product_data, product_parametr, main_product):
        
    for id in product_items_list:
        
        if main_product.cattegory == "Phones":
            if product_parametr == 'color':
            
                try:
                    product = models.MainProductDatabase.objects.get(id=int(id), color=product_data)
                    return product                          
                except:
                    pass
                                
            elif product_parametr == 'memory':
                                
                try:
                    product = models.MainProductDatabase.objects.get(id=int(id), phones_product_data__memory=product_data)       
                    return product                
                except:
                    pass
                
            
            elif product_parametr == 'ram':
                
                try:
                    product = models.MainProductDatabase.objects.get(id=int(id), phones_product_data__ram=product_data)     
                    return product                     
                except:
                    pass
                
            
            elif product_parametr == 'battery':
                
                try:
                    product = models.MainProductDatabase.objects.get(id=int(id), phones_product_data__battery=product_data) 
                    return product                         
                except:
                    pass
                
    
def get_product(model, instance):
    """ Help function for signals. Get product with specific model """
    
    if model == "Phones":
        return models.MainProductDatabase.objects.get(phones_product_data=instance).phones_product_data
    elif model == "Monitors":
        return models.MainProductDatabase.objects.get(monitors_product_data=instance).monitors_product_data
    elif model == 'Laptops':
        return models.MainProductDatabase.objects.get(laptops_product_data=instance).laptops_product_data
    elif model == 'Pc':
        return models.MainProductDatabase.objects.get(pc_product_data=instance).pc_product_data
    elif model == 'AccesoriesForLaptops':
        return models.MainProductDatabase.objects.get(AccesoriesForLaptops_data=instance).AccesoriesForLaptops_data
    elif model == 'Ssd':
        return models.MainProductDatabase.objects.get(ssd_product_data=instance).ssd_product_data
    elif model == 'Graphs':
        return models.MainProductDatabase.objects.get(graphs_product_data=instance).graphs_product_data
    elif model == 'Ram':
        return models.MainProductDatabase.objects.get(ram_product_data=instance).ram_product_data
    elif model == 'Pendrives':
        return models.MainProductDatabase.objects.get(pendrive_product_data=instance).pendrive_product_data
    elif model == 'Switches':
        return models.MainProductDatabase.objects.get(switch_product_data=instance).switch_product_data
    elif model == 'Motherboard':
        return models.MainProductDatabase.objects.get(motherboard_product_data=instance).motherboard_product_data
    elif model == 'Cpu':
        return models.MainProductDatabase.objects.get(cpu_product_data=instance).cpu_product_data
    elif model == 'Tv':
        return models.MainProductDatabase.objects.get(tv_product_data=instance).tv_product_data
    elif model == 'Headphones':
        return models.MainProductDatabase.objects.get(headphones_product_data=instance).headphones_product_data
    elif model == 'Routers':
        return models.MainProductDatabase.objects.get(router_product_data=instance).router_product_data
    
    
def choose_model(model, instance):
    """ Help function for signals. Create objects for specific model """
    
    
    
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
        return models.MainProductDatabase.objects.create(switch_product_data=instance)
    elif model == 'Motherboard':
        return models.MainProductDatabase.objects.create(motherboard_product_data=instance)
    elif model == 'Cpu':
        return models.MainProductDatabase.objects.create(cpu_product_data=instance)
    elif model == 'Tv':
        return models.MainProductDatabase.objects.create(tv_product_data=instance)
    elif model == 'Headphones':
        return models.MainProductDatabase.objects.create(headphones_product_data=instance)
    elif model == 'Routers':
        return models.MainProductDatabase.objects.create(router_product_data=instance)
    
    
def try_to_get_product(product, instance):
    """ Help function for signals. Try to get specific product from model """
    
    instance_obj = models.MainProductDatabase.objects.get(ean=product.ean)
    try: 
        instance_obj.phones_product_data.name
        return instance_obj.phones_product_data
    except AttributeError:
        instance_obj.monitors_product_data.name
        return instance_obj.monitors_product_data
    except AttributeError:
        instance_obj.laptops_product_data.name
        return instance_obj.laptops_product_data
    except AttributeError:
        instance_obj.pc_product_data.name
        return instance_obj.pc_product_data
    except AttributeError:
        instance_obj.accesories_for_laptop.name
        return instance_obj.accesories_for_laptop
    except AttributeError:
        instance_obj.ssd_product_data.name
        return instance_obj.ssd_product_data
    except AttributeError:
        instance_obj.graphs_product_data.name
        return instance_obj.graphs_product_data
    except AttributeError:
        instance_obj.ram_product_data.name
        return instance_obj.ram_product_data
    except AttributeError:
        instance_obj.pendrive_product_data.name
        return instance_obj.pendrive_product_data
    except AttributeError:
        instance_obj.switch_product_data.name
        return instance_obj.switch_product_data
    except AttributeError:
        instance_obj.motherboard_product_data.name
        return instance_obj.motherboard_product_data
    except AttributeError:
        instance_obj.cpu_product_data.name
        return instance_obj.cpu_product_data
    except AttributeError:
        instance_obj.tv_product_data.name
        return instance_obj.tv_product_data
    except AttributeError:
        instance_obj.headphones_product_data.name
        return instance_obj.headphones_product_data
    except AttributeError:
        instance_obj.router_product_data.name
        return instance_obj.router_product_data
            
