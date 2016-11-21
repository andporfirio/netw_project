#!/usr/bin/python
# Criado um docstring com os ips dos devices e utilizando o 
# strip() para retirar os espacos e o splitlines() para dividir em linhas 

from __future__ import absolute_import, division, print_function
import netmiko
import json

devices = '''
192.168.100.10 
192.168.100.11
192.168.100.12
192.168.100.13
192.168.100.14
'''.strip().splitlines()

device_type = 'cisco_ios' 
username = 'admin' 
password = 'cisco'

netmiko_exceptions = (netmiko.ssh_exception.NetMikoAuthenticationException,
                      netmiko.ssh_exception.NetMikoTimeoutException)

for device in devices:
    try:
        print('#'*79)
        print('Connecting to device %s:' %device)
        connection = netmiko.ConnectHandler(ip=device, device_type=device_type,
                                        username=username, password=password) 
        print(connection.send_command('show clock'))
        connection.disconnect()
    except netmiko_exceptions as excep:
        print('Failed to: ' ,device ,excep)

