#!/usr/bin/env python
#Utilizando uma lista com todos os dicionarios dos devices 

from __future__ import absolute_import, division, print_function
import netmiko
import json
from getinput import getinput
from getpass import getpass
import sys
import signal

signal.signal(signal.SIGPIPE, signal.SIG_DFL) #IOError: Broken pine
signal.signal(signal.SIGINT, signal.SIG_DFL) #KeyboardInterrupt: Ctrl+C


if len(sys.argv) < 3:
    print("Usage: command.py commands.txt device.json")
    exit()

netmiko_exceptions = (netmiko.ssh_exception.NetMikoAuthenticationException,
                      netmiko.ssh_exception.NetMikoTimeoutException)

with open(sys.argv[1]) as cmd_file:
    commands = cmd_file.readlines()

with open(sys.argv[2]) as devices_files:
    devices = json.load(devices_files)

for device in devices:
    try:
        print('#'*79)
        print('Connecting to device %s:' %device['ip'])
        connection = netmiko.ConnectHandler(**device)
        filename = connection.base_prompt + '.txt'
        with open(filename, 'w') as out_file:
            for command in commands:
                out_file.write('## Output of: ' + command + '\n\n')
                out_file.write(connection.send_command(command) + '\n\n')
        connection.disconnect()
    except netmiko_exceptions as excep:
        print('Failed to: ' ,device['ip'] ,excep)

