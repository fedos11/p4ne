import ipaddress
ip1 = ipaddress.IPv4Address('192.168.1.1')

net1 = ipaddress.IPv4Network('192.168.1.0/24')
net1.network_address

net1.netmask

int(net1.netmask)

ip1.__repr__()
