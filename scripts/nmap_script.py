#!/usr/bin/python

# Network status device

nm.scan(hosts='192.168.1.0/24', arguments='-n -sP -PE -PA21,23,80,22')
hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
for host, status in hosts_list:
	print('{0}:{1}'.host)