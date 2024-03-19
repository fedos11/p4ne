import ipaddress

def classify_string(input_string):
    if input_string.startswith("ip address"):
        parts = input_string.split()
        if len(parts) == 4:
            try:
                ip_interface = ipaddress.IPv4Interface(parts[2] + "/" + parts[3])
                return ip_interface
            except ValueError:
                pass
    return None
import os

folder_path = 'C:\\Users\\fa.petrov\\Desktop\\config_files'

ip_addresses = []

for filename in os.listdir(folder_path):
    if filename.endswith('.log'):
        with open(os.path.join(folder_path, filename), 'r') as file:
            # Перебор всех строк в файле
            for line in file:
                # Классификация каждой строки
                ip_interface = classify_string(line)
                if ip_interface is not None:
                    ip_addresses.append(str(ip_interface.ip))

for ip in ip_addresses:
    print(ip)