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
        product_model = product.routers_product_model.model
        return models.MainProductDatabase.objects.filter(routers_product_model__model=product_model)
    
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
                
    
            
            

        
       
    
    # elif cattegory == 'Laptops':
    #     pass
    
    # elif cattegory == 'PC':
    #     pass
    
    # elif cattegory == 'Monitor':
    #     pass
    
    # elif cattegory == 'Accesories for laptops':
    #     pass
    
    # elif cattegory == 'SSD':
    #     pass
    
    # elif cattegory == 'Graphs':
    #     pass
    
    # elif cattegory == 'Ram':
    #     pass
    
    # elif cattegory == 'Pendrives':
    #     pass
    
    # elif cattegory == 'Routers':
    #     pass
    
    # elif cattegory == 'Switches':
    #     pass
    
    # elif cattegory == 'Motherboard':
    #     pass
    
    # elif cattegory == 'CPU':
    #     pass
    
    # elif cattegory == 'TV':
    #     pass
    
    # elif cattegory == 'Headphones':
    #     pass