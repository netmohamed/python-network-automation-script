import paramiko
import getpass
from time import sleep

d='''
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░˜”*°•.˜”*°• script for config vlan •°*”˜.•°*”˜░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
'''
print(d)



hostname =input('set ip address :')
username = input('set username :')
password =getpass.getpass(prompt="set password :", stream=None)

def configure_vlan(hostname, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, username=username, password=password)
    connection=client.invoke_shell()
    connection.send('enable\n')
    connection.send('cisco\n')
    connection.send('conf t\n')


    

    try:
        num_vlans = int(input("Enter the number of VLANs to configure: "))

        for i in range(1, num_vlans + 1):
            

            
            command = f"vlan {i}\nname VLAN{i}\n"
            connection.send(command)
            print('config vlan ======================== {}'.format(i))
            sleep(0.5)
            
            

    finally:
        client.close()


def configure_switch_port(hostname, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, username=username, password=password)
    connection=client.invoke_shell()
    connection.send('enable\n')
    connection.send('cisco\n')
    connection.send('conf t\n')
    try:
        inter = str(input("set interface : "))
        vlan_id=int(input('set vlan id : '))
        command =[f'int {inter}\n','switchport mode access\n ',f'switchport access vlan {vlan_id}\n','do wr']
        for i in command:
            print(f'start confgure ========================== {i}')
            connection.send(i)
            sleep(0.5)
    finally:
        client.close()
        print("Switch port configuration completed.")

def remove_vlan(hostname,username,password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, username=username, password=password)
    connection=client.invoke_shell()
    connection.send('enable\n')
    connection.send('cisco\n')
    connection.send('conf t\n')


    

    try:
        num_vlans = int(input("Enter the number of VLANs to remove : "))

        for i in range(1, num_vlans + 1):
            

            
            command = f"no vlan {i}\nno name VLAN{i}\n"
            connection.send(command)
            print('remove vlan ======================== {}'.format(i))
            sleep(0.5)
            
            

    finally:
        client.close() 

d='''
1  ===> config vlan
2  ===> config switch port mode access
3  ===> remove vlan 
'''
print(d)
choose=int(input('set wath do you want : '))
if choose == int(1) :
    configure_vlan(hostname, username, password)
elif choose == int(2):
    configure_switch_port(hostname, username, password)
elif choose == 3 :
    remove_vlan(hostname,username,password)
