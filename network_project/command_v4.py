#!/usr/bin/python
#Utilizando uma lista com todos os dicionarios dos devices 

from __future__ import absolute_import, division, print_function
import netmiko
import json


devices = [
{
    'ip':'192.168.100.10',
    'device_type':'cisco_ios',
    'username':'admin',
    'password':'cisco', 
},

{
    'ip':'192.168.100.11',
    'device_type':'cisco_ios',
    'username':'admin',
    'password':'cisco', 
},

{
    'ip':'192.168.100.12',
    'device_type':'cisco_ios',
    'username':'admin',
    'password':'cisco', 
},

{
    'ip':'192.168.100.13',
    'device_type':'cisco_ios',
    'username':'admin',
    'password':'cisco', 
},

{
    'ip':'192.168.100.14',
    'device_type':'cisco_ios',
    'username':'admin',
    'password':'cisco', 
},
]


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

