import ipaddress
import random
class IPv4RandomNetwork(ipaddress.IPv4Network):
    def __init__(self):
        net = random.randint(0x0b000000, 0xdf000000)
        mask = random.randint(8,24)
        ipaddress.IPv4Network.__init__()




