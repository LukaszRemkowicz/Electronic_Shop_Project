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

    screen_diagonal = {
        "5 - 5.49'": 0,
        "5.5 - 5.99'": 0,
        "6 - 6.49'": 0,
        "6.5 - 6.99'": 0,
        "7 - 7.49'": 0,
    }

    for product in phones:
        if 5 <= float(product.screen_diagonal) <= 5.49:
            screen_diagonal["5 - 5.49'"] += 1
        elif 5.5 <= float(product.screen_diagonal) <= 5.99:
            screen_diagonal["5.5 - 5.99'"] += 1
        elif 6 <= float(product.screen_diagonal) <= 6.49:
            screen_diagonal["6 - 6.49'"] += 1
        elif 6.5 <= float(product.screen_diagonal) <= 6.99:
            screen_diagonal["6.5 - 6.99'"] += 1
        elif 7 <= float(product.screen_diagonal) <= 7.49:
            screen_diagonal["7 - 7.49''"] += 1

    battery = {}
    for product in phones:
        if product.battery in battery:
            battery[product.battery] += 1
        else:
            battery[product.battery] = 1

    waterproof = {
        "Yes": len([product.waterproof for product in phones if product.waterproof]),
        "No": len([product.waterproof for product in phones if not product.waterproof]),
    }

    return {
        "battery": battery,
        "diagonal": screen_diagonal,
        "waterproof": waterproof,
        "screen": screen,
        "memory_card": memory_card,
        "memory": memory,
        "ram": ram,
        "processor": processor,
        "system": system,
        "cpu_clock": cpu_clock,
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

    curved = {}
    for product in monitors:

        if product.curved in curved:
            curved[product.curved] += 1
        else:
            curved[product.curved] = 1

    if "No" not in curved:
        curved["No"] = 0
    if "Yes" not in curved:
        curved["Yes"] = 0

    diagonal = {
        "10-19'": 0,
        "20-29'": 0,
        "30-39'": 0,
        "40-49'": 0,
        "50-59'": 0,
        "60-69'": 0,
        "70' and more": 0,
    }

    for product in monitors:
        splited = product.diagonal.replace('"', "").replace("'", "")

        if 10 <= float(splited) <= 19:
            diagonal["10-19'"] += 1
        elif 20 <= float(splited) <= 30:
            diagonal["20-29'"] += 1
        elif 30 <= float(splited) <= 39:
            diagonal["30-39'"] += 1
        elif 40 <= float(splited) <= 49:
            diagonal["40-49'"] += 1
        elif 50 <= float(splited) <= 59:
            diagonal["50-59'"] += 1
        elif 60 <= float(splited) <= 69:
            diagonal["60-69'"] += 1
        elif 70 <= float(splited):
            diagonal["70' and more"] += 1

    return {
        "resolution": resolution,
        "diagonal": diagonal,
        "curved": curved,
        "screen": screen,
        "matrix_type": matrix_type,
        "format": format,
        "refresh_rate": refresh_rate,
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

    return {
        "resolution": resolution,
        "diagonal": screen_diagonal,
        "bluetooth": len(
            [product.bluetooth for product in laptops if product.bluetooth]
        ),
        "screen": screen,
        "system": system,
        "graph": graph,
        "ram": ram,
        "ram_model": ram_model,
        "ram_freq": ram_freq,
        "pcie": p_c_i_e,
        "processor": processor,
        "processor_clock": processor_clock,
        "processor_cores_threads": processor_cores_threads,
    }


def filter_pcs(pcs: QuerySet) -> Dict:
    processor = {}
    for product in pcs:
        if product.processor in processor:
            processor[product.processor] += 1
        else:
            processor[product.processor] = 1

    socket = {}
    for product in pcs:
        if product.socket in socket:
            socket[product.socket] += 1
        else:
            socket[product.socket] = 1

    system = {}
    for product in pcs:
        if product.system in system:
            system[product.system] += 1
        else:
            system[product.system] = 1

    motherboard_chipset = {}
    for product in pcs:
        if product.motherboard_chipset in motherboard_chipset:
            motherboard_chipset[product.motherboard_chipset] += 1
        else:
            motherboard_chipset[product.motherboard_chipset] = 1

    disc = {}
    for product in pcs:
        if product.disc in disc:
            disc[product.disc] += 1
        else:
            disc[product.disc] = 1

    ram = {}
    for product in pcs:
        if product.ram in ram:
            ram[product.ram] += 1
        else:
            ram[product.ram] = 1

    ram_type = {}
    for product in pcs:
        if product.ram_type in ram_type:
            ram_type[product.ram_type] += 1
        else:
            ram_type[product.ram_type] = 1

    p_c_i_e = {}
    for product in pcs:
        if product.p_c_i_e in p_c_i_e:
            p_c_i_e[product.p_c_i_e] += 1
        else:
            p_c_i_e[product.p_c_i_e] = 1

    bluetooth = {}
    for product in pcs:
        if product.bluetooth in bluetooth:
            bluetooth[product.bluetooth] += 1
        else:
            bluetooth[product.bluetooth] = 1

    if "No" not in bluetooth:
        bluetooth["No"] = 0
    if "Yes" not in bluetooth:
        bluetooth["Yes"] = 0

    return {
        "processor": processor,
        "socket": socket,
        "system": system,
        "motherboard_chipset": motherboard_chipset,
        "disc": disc,
        "ram": ram,
        "ram_type": ram_type,
        "p_c_i_e": p_c_i_e,
        "bluetooth": bluetooth,
    }


def filter_ssd(ssds: QuerySet) -> Dict:
    format = {}
    for product in ssds:
        if product.format in format:
            format[product.format] += 1
        else:
            format[product.format] = 1

    capacity = {}
    for product in ssds:
        if product.capacity in capacity:
            capacity[product.capacity] += 1
        else:
            capacity[product.capacity] = 1

    reading_speed = {}
    for product in ssds:
        if product.reading_speed in reading_speed:
            reading_speed[product.reading_speed] += 1
        else:
            reading_speed[product.reading_speed] = 1

    writing_speed = {}
    for product in ssds:
        if product.writing_speed in writing_speed:
            writing_speed[product.writing_speed] += 1
        else:
            writing_speed[product.writing_speed] = 1

    life_time = {}
    for product in ssds:
        if product.life_time in life_time:
            life_time[product.life_time] += 1
        else:
            life_time[product.life_time] = 1

    return {
        "format": format,
        "capacity": capacity,
        "reading_speed": reading_speed,
        "writing_speed": writing_speed,
        "life_time": life_time,
    }


def filter_graphs(graphs: QuerySet) -> Dict:
    chipset = {}
    for product in graphs:
        if product.chipset in chipset:
            chipset[product.chipset] += 1
        else:
            chipset[product.chipset] = 1

    chipset_producent = {}
    for product in graphs:
        if product.chipset_producent in chipset_producent:
            chipset_producent[product.chipset_producent] += 1
        else:
            chipset_producent[product.chipset_producent] = 1

    ram = {}
    for product in graphs:
        if product.ram in ram:
            ram[product.ram] += 1
        else:
            ram[product.ram] = 1

    ram_type = {}
    for product in graphs:
        if product.ram_type in ram_type:
            ram_type[product.ram_type] += 1
        else:
            ram_type[product.ram_type] = 1

    connector_type = {}
    for product in graphs:
        if product.connector_type in connector_type:
            connector_type[product.connector_type] += 1
        else:
            connector_type[product.connector_type] = 1

    return {
        "chipset": chipset,
        "chipset_producent": chipset_producent,
        "ram": ram,
        "ram_type": ram_type,
        "connector_type": connector_type,
    }


def filter_rams(rams: QuerySet) -> Dict:
    capacity = {}
    for product in rams:
        if product.capacity in capacity:
            capacity[product.capacity] += 1
        else:
            capacity[product.capacity] = 1

    frequency = {}
    for product in rams:
        if product.frequency in frequency:
            frequency[product.frequency] += 1
        else:
            frequency[product.frequency] = 1

    modules_number = {}
    for product in rams:
        if product.modules_number in modules_number:
            modules_number[product.modules_number] += 1
        else:
            modules_number[product.modules_number] = 1

    delay = {}
    for product in rams:
        if product.delay in delay:
            delay[product.delay] += 1
        else:
            delay[product.delay] = 1

    voltage = {}
    for product in rams:
        if product.voltage in voltage:
            voltage[product.voltage] += 1
        else:
            voltage[product.voltage] = 1

    typee = {}
    for product in rams:
        if product.type in typee:
            typee[product.type] += 1
        else:
            typee[product.type] = 1

    return {
        "capacity": capacity,
        "frequency": frequency,
        "modules_number": modules_number,
        "delay": delay,
        "voltage": voltage,
        "type": typee,
    }


def filter_pendrives(pendrives: QuerySet) -> Dict:
    capacity = {}
    for product in pendrives:
        if product.capacity in capacity:
            capacity[product.capacity] += 1
        else:
            capacity[product.capacity] = 1

    return {"capacity": capacity}


def filter_switches(switches: QuerySet) -> Dict:
    num_of_poe = {}
    for product in switches:
        if product.num_of_poe in num_of_poe:
            num_of_poe[product.num_of_poe] += 1
        else:
            num_of_poe[product.num_of_poe] = 1

    case_kind = {}
    for product in switches:
        if product.case_kind in case_kind:
            case_kind[product.case_kind] += 1
        else:
            case_kind[product.case_kind] = 1

    manageable = {}
    for product in switches:
        if product.manageable in manageable:
            manageable[product.manageable] += 1
        else:
            manageable[product.manageable] = 1

    return {
        "num_of_poe": num_of_poe,
        "case_kind": case_kind,
        "manageable": manageable,
    }


def filter_motherboards(motherboards: QuerySet) -> Dict:
    chipset = {}
    for product in motherboards:
        if product.chipset in chipset:
            chipset[product.chipset] += 1
        else:
            chipset[product.chipset] = 1

    processor_socket = {}
    for product in motherboards:
        if product.processor_socket in processor_socket:
            processor_socket[product.processor_socket] += 1
        else:
            processor_socket[product.processor_socket] = 1

    ram_slots = {}
    for product in motherboards:
        if product.ram_slots in ram_slots:
            ram_slots[product.ram_slots] += 1
        else:
            ram_slots[product.ram_slots] = 1

    card_standard = {}
    for product in motherboards:
        if product.card_standard in card_standard:
            card_standard[product.card_standard] += 1
        else:
            card_standard[product.card_standard] = 1

    raid_controler = {}
    for product in motherboards:
        reaplce_str = product.raid_controler.replace("\n RAID ", ", ").replace(
            "RAID ", ""
        )
        if reaplce_str != "No raid":
            new_string = f"Raids: {reaplce_str}"
        else:
            new_string = reaplce_str

        if new_string in raid_controler:
            raid_controler[new_string] += 1
        else:
            raid_controler[new_string] = 1

    ram = {}
    for product in motherboards:
        if product.ram in ram:
            ram[product.ram] += 1
        else:
            ram[product.ram] = 1

    wifi = {}
    for product in motherboards:
        if product.wifi in wifi:
            wifi[product.wifi] += 1
        else:
            wifi[product.wifi] = 1

    return {
        "chipset": chipset,
        "processor_socket": processor_socket,
        "ram_slots": ram_slots,
        "card_standard": card_standard,
        "raid_controler": raid_controler,
        "ram": ram,
        "wifi": wifi,
    }


def filter_cpus(cpus: QuerySet) -> Dict:
    cooler = {}
    for product in cpus:
        if product.cooler in cooler:
            cooler[product.cooler] += 1
        else:
            cooler[product.cooler] = 1

    socket = {}
    for product in cpus:
        if product.socket in socket:
            socket[product.socket] += 1
        else:
            socket[product.socket] = 1

    cores_num = {}
    for product in cpus:
        if product.cores_num in cores_num:
            cores_num[product.cores_num] += 1
        else:
            cores_num[product.cores_num] = 1

    threat_num = {}
    for product in cpus:
        if product.threat_num in threat_num:
            threat_num[product.threat_num] += 1
        else:
            threat_num[product.threat_num] = 1

    clock_frequency = {}
    for product in cpus:
        if product.clock_frequency in clock_frequency:
            clock_frequency[product.clock_frequency] += 1
        else:
            clock_frequency[product.clock_frequency] = 1

    supported_memory = {}
    for product in cpus:
        if product.supported_memory in supported_memory:
            supported_memory[product.supported_memory] += 1
        else:
            supported_memory[product.supported_memory] = 1

    return {
        "cooler": cooler,
        "socket": socket,
        "cores_num": cores_num,
        "threat_num": threat_num,
        "clock_frequency": clock_frequency,
        "supported_memory": supported_memory,
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
        splited = product.diagonal.split("'")[0]
        if 20 <= int(splited) <= 30:
            diagonal["20-29'"] += 1
        elif 30 <= int(splited) <= 39:
            diagonal["30-39'"] += 1
        elif 40 <= int(splited) <= 49:
            diagonal["40-49'"] += 1
        elif 50 <= int(splited) <= 59:
            diagonal["50-59'"] += 1
        elif 60 <= int(splited) <= 69:
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

    curved = {}
    for product in tvs:
        if product.curved in curved:
            curved[product.curved] += 1
        else:
            curved[product.curved] = 1

    if "No" not in curved:
        curved["No"] = 0
    if "Yes" not in curved:
        curved["Yes"] = 0

    smart_tv = {}
    for product in tvs:
        if product.smart_tv in smart_tv:
            smart_tv[product.smart_tv] += 1
        else:
            smart_tv[product.smart_tv] = 1

    if "No" not in smart_tv:
        smart_tv["No"] = 0
    if "Yes" not in smart_tv:
        smart_tv["Yes"] = 0

    return {
        "refresh_rate": refresh,
        "diagonal": diagonal,
        "curved": curved,
        "smart_tv": smart_tv,
        "resolution": resolution,
        "matrix_type": matrix_type,
    }


def filter_headphones(heaphones: QuerySet) -> Dict:
    connection = {}
    for product in heaphones:
        if product.connection in connection:
            connection[product.connection] += 1
        else:
            connection[product.connection] = 1

    return {"connection": connection}


def filter_routers(routers: QuerySet) -> Dict:
    wifi = {}
    for product in routers:
        new_str = product.wifi
        if product.wifi == "":
            new_str = "No WiFi"
        if new_str in wifi:
            wifi[new_str] += 1
        else:
            wifi[new_str] = 1

    case = {}
    for product in routers:
        if product.case in case:
            case[product.case] += 1
        else:
            case[product.case] = 1

    wan_ports = {}
    for product in routers:
        new_str = product.wan_ports
        if product.wan_ports == "":
            new_str = "No WAN ports"
        if new_str in wan_ports:
            wan_ports[new_str] += 1
        else:
            wan_ports[new_str] = 1

    lan_ports = {}
    for product in routers:
        new_str = product.lan_ports
        if product.lan_ports == "":
            new_str = "No LAN ports"
        if new_str in lan_ports:
            lan_ports[new_str] += 1
        else:
            lan_ports[new_str] = 1

    usb_ports = {}
    for product in routers:
        if product.usb_ports in usb_ports:
            usb_ports[product.usb_ports] += 1
        else:
            usb_ports[product.usb_ports] = 1

    sim = {}
    for product in routers:
        if product.sim in sim:
            sim[product.sim] += 1
        else:
            sim[product.sim] = 1

    return {
        "wifi": wifi,
        "lan_ports": lan_ports,
        "wan_ports": wan_ports,
        "case": case,
        "usb_ports": usb_ports,
        "sim": sim,
    }
