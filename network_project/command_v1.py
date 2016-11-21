#!/usr/bin/python
# Conectando em um unico device colocando as informacoes diretamente 
# no ConnectHandler()

from __future__ import absolute_import, division, print_function

import netmiko
import json

connection = netmiko.ConnectHandler(ip='192.168.100.10', 
                device_type='cisco_ios', username='admin', password='cisco')

print(connection.send_command('show clock'))
connection.disconnect()
