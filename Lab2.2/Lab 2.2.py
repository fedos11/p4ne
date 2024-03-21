import glob
import re
import ipaddress
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/config')
def config():
    return render_template('config.html', hostnames=hostnames_dict)


@app.route('/config/<hostname>')
def hostname_config(hostname):
    return render_template('hostname.html', hostname=hostname, interfaces=hostnames_dict[hostname])


def find_interface(target_line: str) -> ipaddress.IPv4Interface:
    if m := re.match(
            r' ip address (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',
            target_line):
        return ipaddress.IPv4Interface((m.group(1), m.group(2)))


if __name__ == '__main__':
    hostnames_dict = {}

    dir_name = 'config_files'
    file_list = glob.glob(f'{dir_name}\\*.log')

    for file_path in file_list:
        with open(file_path) as file:

            hostname = ''
            interfaces_list = []

            file_lines = file.readlines()
            for line in file_lines:
                if m := re.match(r'hostname (.*)\n', line):
                    hostname = m.group(1)

            if hostname:
                for line in file_lines:
                    if interface := find_interface(line):
                        interfaces_list.append(interface)
                hostnames_dict[hostname] = interfaces_list

    app.run(debug=True, port=80)
