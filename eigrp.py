import paramiko
import getpass
from time import sleep

d='''
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░s░c░r░i░p░t░░░f░o░r░░░c░o░n░f░i░g░░░e░i░g░r░p░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
'''
print(d)

hostname = input('ip ssh address : ')  
username = input('username ssh :')        
password = getpass.getpass(prompt='set password ssh : ',stream=None) 

def configure_eigrp(hostname, username, password):
    auto=int(input('set autonome system :'))
    net1=input('set network 1 :')
    net2=input('set set network 2:')
    net3=input('set set network 3 :')
   
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, username=username, password=password)

    try:
       
        
        shell = client.invoke_shell()

        
        shell.send("enable\n")
        shell.send( "cisco\n")
        shell.send("configure terminal\n")
        print(f'config autonome system  {auto}')
        shell.send(f"router eigrp {auto} \n")
        print(f'config {net1}')
        sleep(0.5)
        shell.send(f"network {net1} 0.0.0.255 \n")
        print(f'config {net2}')
        sleep(0.5)
        shell.send(f"network {net2} 0.0.0.255 \n")
        print(f'config {net3}')
        sleep(0.5)
        shell.send(f"network {net3} 0.0.0.255\n")
        sleep(0.5)
        shell.send("no auto-summary\n")
        print('exit')
        sleep(0.5)
        shell.send("exit\n")
        sleep(0.5)
        

       
        print(' save config')
        shell.send(" do wr\n")

      
        while not shell.recv_ready():
            pass

        
        output = shell.recv(65535).decode('utf-8')
        print(output)

    finally:
        
        client.close()

  


configure_eigrp(hostname, username, password)