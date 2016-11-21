#!/usr/bin/python
# Conectando aos devices utilizando um dicionario com informacoes
# de cada device

from __future__ import absolute_import, division, print_function
import netmiko
import json

esw1 = {
    'ip':'192.168.100.10',
    'device_type':'cisco_ios',
    'username':'admin',
    'password':'cisco', 
}

esw2 = {
    'ip':'192.168.100.11',
    'device_type':'cisco_ios',
    'username':'admin',
    'password':'cisco', 
}

esw3 = {
    'ip':'192.168.100.12',
    'device_type':'cisco_ios',
    'username':'admin',
    'password':'cisco', 
}

esw4 = {
    'ip':'192.168.100.13',
    'device_type':'cisco_ios',
    'username':'admin',
    'password':'cisco', 
}

esw5 = {
    'ip':'192.168.100.14',
    'device_type':'cisco_ios',
    'username':'admin',
    'password':'cisco', 
}

devices = [esw1, esw2, esw3, esw4, esw5]

netmiko_exceptions = (netmiko.ssh_exception.NetMikoAuthenticationException,
                      netmiko.ssh_exception.NetMikoTimeoutException)

for device in devices:
    try:
        print('#'*79)
        print('Connecting to device %s:' %device['ip'])
        connection = netmiko.ConnectHandler(**device) 
        print(connection.send_command('show clock'))
        connection.disconnect()
    except netmiko_exceptions as excep:
        print('Failed to: ' ,device['ip'] ,excep)

