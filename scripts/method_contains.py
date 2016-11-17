#!/usr/bin/python

list2 = ['Cisco','Juniper','Arista','HP','Nokia']

if list2.__contains__("Cisco") == True:
	i = list2.index("Cisco")
	list2[i] = "Brocade"
	print "Vendor Cisco substituido por Brocade"
else:
	print "Cisco nao foi encontrado"