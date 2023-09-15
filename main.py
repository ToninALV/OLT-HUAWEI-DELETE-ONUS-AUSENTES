import os
import paramiko
import time


path01 = "olts.txt"
path02 = "onus.txt"
path03 = "service_profile_all.txt"

try:
    os.remove(path03)
except:
    pass

# Acessar Arquivo com as OLTS para pegar o IP or Input com IP | Usuário | Senha

host = "10.144.9.3"
port = "22"
username = "antonio.silva"
password = "An@13606973659"

# Conectar na OLT e dar os comandos

def connect_equipament():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port=port, username=username, password=password)
    print("-----CONEXÃO ESTABELECIDA-----")

    command = ssh.invoke_shell()
    return command


def send_command():
    
    file = open(path03, 'w')
    ssh = connect_equipament()
    time.sleep(.5)
    ssh.send('enable\n')
    ssh.send('config\n')
    ssh.send('mmi-mode original-output\n')
    ssh.send('display service-port all\n\n')
    time.sleep(30)
    

    terminal = ssh.recv(131070)
    terminal = terminal.decode('utf-8')
    ssh.close()


    file.write(terminal)





# Pegar time da OLT como tempo de base

# Pegar ONU's com tempo maior que 45 dias offline

# Deletar as Onu's

# Gerar um log para as onus desautorizadas

send_command()