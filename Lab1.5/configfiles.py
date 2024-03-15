import os
import re
from collections import OrderedDict

folder_path = 'C:\\Users\\fa.petrov\\Desktop\\config_files'

ip_regex = r'ip address (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'

ip_dict = OrderedDict()


for filename in os.listdir(folder_path):

    if filename.endswith('.log'):
        with open(os.path.join(folder_path, filename), 'r') as file:
            for line in file:
                match = re.search(ip_regex, line)
                if match:
                    ip_dict[match.group(1)] = None

for ip in ip_dict.keys():
    print(ip)