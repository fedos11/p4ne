import re
import time
import paramiko
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_interface_stats_ssh(host, username, password):
    ssh_connection = paramiko.SSHClient()
    ssh_connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_connection.connect(host, username=username, password=password, look_for_keys=False, allow_agent=False)

    session = ssh_connection.invoke_shell()
    session.send(b'terminal len 0\n')
    time.sleep(0.1)
    session.send(b'show interfaces\n')
    time.sleep(0.1)
    output = session.recv(50000)

    interface_list_ssh = []
    for line in output.decode().split('\n'):
        if m := re.match('(.*) is.*, line protocol is.*', line):
            interface_list_ssh.append(f'Interface: {m.group(1)}')
        if m := re.match('(.*) packets output, (.*) bytes,', line):
            interface_list_ssh.append(f'Packets: {m.group(1).strip()} Bytes: {m.group(2).strip()}')

    ssh_connection.close()
    return interface_list_ssh

def get_interface_stats_rest(host, username, password):
    headers = {
        "accept": "application/yang-data+json",
        "Content-Type": "application/yang-data+json"
    }

    response = requests.get(f'https://{host}/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces',
                            auth=(username, password),
                            headers=headers,
                            verify=False)

    output_list = response.json()['Cisco-IOS-XE-interfaces-oper:interfaces']['interface']

    interface_list_rest = []
    for interface in output_list:
        interface_list_rest.append(
            f"Interface: {interface['name']}\n"
            f"Packets: {interface['v4-protocol-stats']['out-pkts']} "
            f"Bytes: {interface['v4-protocol-stats']['out-octets']}")

    return interface_list_rest

ssh_interface_stats = get_interface_stats_ssh('10.31.70.209', 'restapi', 'j0sg1280-7@')
print("SSH Статистика интерфейсов:")
for item in ssh_interface_stats:
    print(item)

rest_interface_stats = get_interface_stats_rest('10.31.70.209', 'restapi', 'j0sg1280-7@')
print("\nREST API Статистика интерфейсов:")
for item in rest_interface_stats:
    print(item)
