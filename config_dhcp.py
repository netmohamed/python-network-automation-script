import paramiko
import getpass
from time import sleep


d='''
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░s░c░r░i░p░t░░░f░o░r░░░c░o░n░f░i░g░░░d░h░c░░p░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
'''
print(d)


username = input("set username ssh :")
password = getpass.getpass(prompt="set password ssh :", stream=None)
hostname = input("set hostname  ssh :")


#===========================================================================================


#=========================== chose ================================================================
chose='''
============================================================================================|
1 --------------------------------------> configure   dhcp                                  |  
2 --------------------------------------> configure  agent de relie                         | 
============================================================================================|
'''
print(chose)
def config_dhcp():
    print('=====================config dhcp ===============================================================')
    ipaddr=input('ip distribute of dhcp :')
    defgw=input('set default getway of dhcp :')
    loop=input('name of pool :')
    ipaddr2=input('ip distribute of dhcp 2:')
    defgw2=input('set default getway of dhcp 2 :')
    loop2=input('name of pool 2 :')
    #command2=['enable\n','cisco\n', 'conf t\n',f'ip dhcp pool {loop}\n network {ipaddr}  255.255.255.0 \ndefault-router {defgw}','do wr']
    #command3=['exit\n','ip dhcp pool {0}\n network {1} 255.255.255.0\n default-router {2}'.format(loop2,ipaddr2,defgw2),'do wr']
    session = paramiko.SSHClient()
    session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    session.connect(hostname, port=22, username=username, password=password)
    connection = session.invoke_shell()
    while connection.recv_ready():
        connection.recv(6000)
    connection.send('enable\n')
    connection.send('cisco\n')
    connection.send('conf t\n')
    sleep(0.5)
    connection.send(f'ip dhcp pool {loop}\n ')
    sleep(0.5)
    connection.send(f'network {ipaddr}  255.255.255.0 \n')
    sleep(0.5)
    connection.send(f'default-router {defgw}\n')
    sleep(0.5)
    connection.send('exit\n')
    sleep(0.5)

    connection.send(f'ip dhcp pool {loop2}\n ')
    sleep(0.5)
    connection.send(f'network {ipaddr2}  255.255.255.0 \n')
    sleep(0.5)
    connection.send(f'default-router {defgw2}\n')
    sleep(0.5)
    connection.send('exit\n')
    sleep(0.5)
    connection.send('do wr\n')
   

    
    session.close()
def config_agent_relie():
    print('=====================config agent de relie ===============================================================')
    interface=input('set int : ')
    helper_address=input('write the helper address : ')
    command2=['enable\n','cisco\n', 'conf t\n','int {0}\nip helper-address {1}'.format(interface,helper_address),'do wr']
    
    session = paramiko.SSHClient()
    session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    session.connect(hostname, port=22, username=username, password=password)
    connection = session.invoke_shell()
    while connection.recv_ready():
        connection.recv(6000)
        sleep(1)
    for cmd2 in command2:
            connection.send(cmd2)
            sleep(0.5)
    
    session.close()
choose=input('choose number :')

if choose == '1' :
     config_dhcp()
elif choose == '2' :
     config_agent_relie()

    


