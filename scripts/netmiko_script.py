#!/usr/bin/python
# -*- coding: utf-8 -*-

def connect():
	import getpass
	from netmiko import ConnectHandler
	from datetime import datetime
	cisco_device = {
		'device_type':'cisco_ios',
		'ip':'',
		'username':'',
		'password':'',		
		}
	while True:
		print("Show interfaces device Cisco")
		print("...........")
		print("Precione 'q' para sair")
		cisco_device['ip'] = raw_input("Digite o IP do equipamento: ")
		if cisco_device['ip'] == 'q':
			cisco_device.clear()
			break
		else:
			cisco_device['username'] = raw_input("Digite o usuário: ")
		if cisco_device['username'] == 'q':
			cisco_device.clear()
			break
		else:
			cisco_device['password'] = getpass.getpass("Digite a senha: ")
		if cisco_device['password'] == 'q':
			cisco_device.clear()
			break
		else:
			print(".............")
			print("..Iniciando a conexão..")
		net_connect = ConnectHandler(**cisco_device)
		print(net_connect.find_prompt())
		output = net_connect.send_command("show ip int brief")
		print(output)
		break

connect()