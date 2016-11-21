#!/usr/bin/python
#Utilizando uma lista com todos os dicionarios dos devices 

from __future__ import absolute_import, division, print_function
import netmiko
import json

netmiko_exceptions = (netmiko.ssh_exception.NetMikoAuthenticationException,
                      netmiko.ssh_exception.NetMikoTimeoutException)

with open('devices.json') as devices_files:
    devices = json.load(devices_files)

for device in devices:
    try:
        print('#'*79)
        print('Connecting to device %s:' %device['ip'])
        connection = netmiko.ConnectHandler(**device) 
        print(connection.send_command('show clock'))
        connection.disconnect()
    except netmiko_exceptions as excep:
        print('Failed to: ' ,device['ip'] ,excep)

