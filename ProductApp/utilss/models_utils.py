from typing import Dict
from django.db.models.query import QuerySet


def filter_phones(phones: QuerySet) -> Dict:
    
    system = {}
    for product in phones:
        if product.system in system:
            system[product.system] += 1
        else:
            system[product.system] = 1

    processor = {}
    for product in phones:
        if product.processor in processor:
            processor[product.processor] += 1
        else:
            processor[product.processor] = 1

    cpu_clock = {}
    for product in phones:
        if product.cpu_clock in cpu_clock:
            cpu_clock[product.cpu_clock] += 1
        else:
            cpu_clock[product.cpu_clock] = 1

    ram = {}
    for product in phones:
        if product.ram in ram:
            ram[product.ram] += 1
        else:
            ram[product.ram] = 1

    memory = {}
    for product in phones:
        if product.memory in memory:
            memory[product.memory] += 1
        else:
            memory[product.memory] = 1

    memory_card = {}
    for product in phones:
        if product.memory_card in memory_card:
            memory_card[product.memory_card] += 1
        else:
            memory_card[product.memory_card] = 1

    screen = {}
    for product in phones:
        if product.screen in screen:
            screen[product.screen] += 1
        else:
            screen[product.screen] = 1

    screen_diagonal = {}
    for product in phones:
        if product.screen_diagonal in screen_diagonal:
            screen_diagonal[product.screen_diagonal] += 1
        else:
            screen_diagonal[product.screen_diagonal] = 1

    battery = {}
    for product in phones:
        if product.battery in battery:
            battery[product.battery] += 1
        else:
            battery[product.battery] = 1


    return {'battery': battery,
            'diagonal': screen_diagonal,
            'waterproof': len([product.waterproof for product in phones if product.waterproof == True]),
            'screen': screen,
            'memory_card,': memory_card,
            'memory,': memory,
            'ram,': ram,
            'processor,': processor,
            'system,': system,
            'cpu_clock,': cpu_clock,
        }
    
def filter_monitors(monitors: QuerySet) -> Dict:
    
    resolution = {}
    for product in monitors:

        if product.resolution in resolution:
            resolution[product.resolution] += 1
        else:
            resolution[product.resolution] = 1

    refresh_rate = {}
    for product in monitors:

        if product.refresh_rate in refresh_rate:
            refresh_rate[product.refresh_rate] += 1
        else:
            refresh_rate[product.refresh_rate] = 1

    format = {}
    for product in monitors:

        if product.format in format:
            format[product.format] += 1
        else:
            format[product.format] = 1

    matrix_type = {}
    for product in monitors:

        if product.matrix_type in matrix_type:
            matrix_type[product.matrix_type] += 1
        else:
            matrix_type[product.matrix_type] = 1

    screen = {}
    for product in monitors:

        if product.screen in screen:
            screen[product.screen] += 1
        else:
            screen[product.screen] = 1

    diagonal = {}
    for product in monitors:

        if product.diagonal in diagonal:
            diagonal[product.diagonal] += 1
        else:
            diagonal[product.diagonal] = 1

    return {'resolution': resolution,
            'diagonal': diagonal,
            'curved': len([product.curved for product in monitors if product.curved == True]),
            'screen': screen,
            'matrix_type,': matrix_type,
            'format,': format,
            'refresh_rate,': refresh_rate,
            }

def filter_laptops(laptops: QuerySet) -> Dict:

    resolution = {}
    for product in laptops:

        if product.resolution in resolution:
            resolution[product.resolution] += 1
        else:
            resolution[product.resolution] = 1

    screen = {}
    for product in laptops:

        if product.screen in screen:
            screen[product.screen] += 1
        else:
            screen[product.screen] = 1

    system = {}
    for product in laptops:

        if product.system in system:
            system[product.system] += 1
        else:
            system[product.system] = 1

    screen_diagonal = {}
    for product in laptops:

        if product.screen_diagonal in screen_diagonal:
            screen_diagonal[product.screen_diagonal] += 1
        else:
            screen_diagonal[product.screen_diagonal] = 1

    graph = {}
    for product in laptops:

        if product.graph in graph:
            graph[product.graph] += 1
        else:
            graph[product.graph] = 1

    ram = {}
    for product in laptops:

        if product.ram in ram:
            ram[product.ram] += 1
        else:
            ram[product.ram] = 1

    ram_model = {}
    for product in laptops:

        if product.ram_model in ram_model:
            ram_model[product.ram_model] += 1
        else:
            ram_model[product.ram_model] = 1

    ram_freq = {}
    for product in laptops:

        if product.ram_freq in ram_freq:
            ram_freq[product.ram_freq] += 1
        else:
            ram_freq[product.ram_freq] = 1

    p_c_i_e = {}
    for product in laptops:

        if product.p_c_i_e in p_c_i_e:
            p_c_i_e[product.p_c_i_e] += 1
        else:
            p_c_i_e[product.p_c_i_e] = 1
            
    processor = {}
    for product in laptops:

        if product.processor in processor:
            processor[product.processor] += 1
        else:
            processor[product.processor] = 1
    
    processor_clock = {}
    for product in laptops:

        if product.processor_clock in processor_clock:
            processor_clock[product.processor_clock] += 1
        else:
            processor_clock[product.processor_clock] = 1
            
    processor_cores_threads = {}
    for product in laptops:

        if product.processor_cores_threads in processor_cores_threads:
            processor_cores_threads[product.processor_cores_threads] += 1
        else:
            processor_cores_threads[product.processor_cores_threads] = 1

    return {'resolution': resolution,
            'diagonal': screen_diagonal,
            'bluetooth': len([product.bluetooth for product in laptops if product.bluetooth == True]),
            'screen': screen,
            'system,': system,
            'graph,': graph,
            'ram,': ram,
            'ram_model,': ram_model,
            'ram_freq,': ram_freq,
            'pcie,': p_c_i_e,
            'processor,': processor,
            'processor_clock,': processor_clock,
            'cores_threads,': processor_cores_threads,
            }

def filter_tvs(tvs: QuerySet) -> Dict:

    refresh = {}
    for product in tvs:
        if product.refresh_rate in refresh:
            refresh[product.refresh_rate] += 1
        else:
            refresh[product.refresh_rate] = 1

    diagonal = {
        "20-29'": 0,
        "30-39'": 0,
        "40-49'": 0,
        "50-59'": 0,
        "60-69'": 0,
        "70' and more": 0,
    }

    for product in tvs:
        splited = product.diagonal.split('\'')[0]
        if 20 <= int(splited) < 30:
            diagonal["20-29'"] += 1
        elif 30 <= int(splited) < 39:
            diagonal["30-39'"] += 1
        elif 40 <= int(splited) < 49:
            diagonal["40-49'"] += 1
        elif 50 <= int(splited) < 59:
            diagonal["50-59'"] += 1
        elif 60 <= int(splited) < 69:
            diagonal["60-69'"] += 1
        elif 70 <= int(splited):
            diagonal["70' and more"] += 1

    resolution = {}
    for product in tvs:
        if product.resolution in resolution:
            resolution[product.resolution] += 1
        else:
            resolution[product.resolution] = 1

    matrix_type = {}
    for product in tvs:
        if product.matrix_type in matrix_type:
            matrix_type[product.matrix_type] += 1
        else:
            matrix_type[product.matrix_type] = 1

    return {'refresh_rate': refresh,
            'diagonal': diagonal,
            'curved': len([product.curved for product in tvs if product.curved == 'Yes']),
            'smart_tv': len([product.smart_tv for product in tvs if product.smart_tv == 'Yes']),
            'resolution': resolution,
            'matrix_type': matrix_type
        }