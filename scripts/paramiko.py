# install paramiko debian

# dpkg -l | grep libssl
# apt-get remove --purge libssl
# apt-get autoremove
# apt-get install libssl libssl-dev
# pip install paramiko
# apt-get install python-dev libmysqlclient-dev
# pip install mysql-python

import paramiko
ip = '192.168.100.10'
username = 'admin'
password = 'cisco'
ssh_conn = paramiko.SSHClient()
ssh_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_conn.connect(ip, username=username, password=password, look_for_keys=False)

ssh_shell = ssh_conn.invoke_shell()

ssh_shell

dir(ssh_shell)

output = ssh_shell.recv(65535)

ssh_shell.send("show ip int brief\n")

ssh_shell.send("show int status\n")

print output