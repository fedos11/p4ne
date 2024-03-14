import ipaddress
import random

class IPv4RandomNetwork(ipaddress.IPv4Network):
    def __init__(self):
        net = random.randint(0x0b000000, 0xdf000000)
        mask = random.randint(8, 24)
        ipaddress.IPv4Network.__init__(self, (net, mask), strict=False)

random_networks = []
for _ in range(50):
    random_network = IPv4RandomNetwork()
    random_networks.append(random_network)

random_networks.sort(key=lambda x: (x.prefixlen, x.network_address))

for network in random_networks:
    print(network)