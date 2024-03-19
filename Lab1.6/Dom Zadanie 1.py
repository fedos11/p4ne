import os
import re
import ipaddress
from openpyxl import Workbook

folder_path = 'C:\\Users\\fa.petrov\\Desktop\\config_files'

ip_regex = r'ip address (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'

network_dict = {}

for filename in os.listdir(folder_path):
    if filename.endswith('.log'):
        with open(os.path.join(folder_path, filename), 'r') as file:
            for line in file:
                match = re.search(ip_regex, line)
                if match:
                    ip_interface = ipaddress.IPv4Interface(f"{match.group(1)}/{match.group(2)}")
                    network_dict[str(ip_interface.network)] = str(ip_interface.netmask)

wb = Workbook()
ws = wb.active

ws.append(["Сеть", "Маска"])

for network, mask in network_dict.items():
    ws.append([network, mask])

wb.save("C:\\Users\\fa.petrov\\Desktop\\address_plan.xlsx")

for network, mask in network_dict.items():
    print(f"Сеть: {network}, Маска: {mask}")