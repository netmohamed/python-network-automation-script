import paramiko
import getpass
from time import sleep


d='''
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░s░c░r░i░p░t░░░f░o░r░░░c░o░n░f░i░g░░░i░n░t░e░r░f░a░c░e░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
'''
print(d)


username = input("set username ssh :")
password = getpass.getpass(prompt="set password ssh :", stream=None)
hostname = input("set hostname  ssh :")




interface=input('set int : ')
iface_ip_address=input(' set ip address and mask of interface  :  ')
commands = ['enable\n','cisco\n', 'conf t\n', 'int {0}\n ip address {1}\n no sh\n exit\n'.format(interface,iface_ip_address)]
session = paramiko.SSHClient()
session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
session.connect(hostname, port=22, username=username, password=password)
connection = session.invoke_shell()
outputs = []
while connection.recv_ready():
    connection.recv(6000)
d='''

|       start config interface  .......  
--------------------------                                         |
-----------------------------------------------         |
-------------------------------------------------------------------|

'''
for cmd in commands:
    print(d)
    connection.send(cmd)
    sleep(0.5)
c='''
|====================================================================|
|            int configuration  finished                             |
|====================================================================|
'''    
print(c)
session.close()