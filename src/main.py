import sys
from utils import validator
from module import dns,portscan

#Coletando Entrada Do Usuário
try:
    host = sys.argv[1] #coleta entrada do usuário via linha de comando
    start_port =  int(sys.argv[2]) #coleta a porta inicial para varredura
    end_port = int(sys.argv[3]) #coleta a porta final para varred

except IndexError: #Caso o usuário não forneça um host
    print("Usage: python main.py <host>")
    sys.exit(1)

#Validando Entrada Do Usuário
ip_valid = validator.is_valid_ip(host) #valida o host usando a função do módulo validator
hostname_valid = validator.is_hostname_valid(host) #valida o host usando a função do módulo validator

valid_port = validator.is_valid_port(start_port, end_port) #valida as portas usando a função do módulo validator

#Programa Principal
if not valid_port: #se as portas não forem válidas, exibe uma mensagem de erro e encerra o programa
    print("[-] Por favor, forneça um intervalo de portas válido (1-65535).")
    sys.exit(1)

if ip_valid:
    print(f"[+] IPv4 Detectado: {host}")

elif hostname_valid:
    print(f"[+] Hostname Detectado: {host}")
    
    ip_address = dns.resolver_dns(host) #tenta resolver o hostname para um endereço IP usando a função do módulo dns
    
    if ip_address: #se a resolução for bem-sucedida, exibe o endereço IP resolvido
        print(f"[+] Endereço IP Resolvido: {ip_address}")
    
    else: 
        print("[-] Falha ao resolver o hostname.")

else:
    print("[-] Por favor, forneça um endereço IP ou hostname válido.")
    sys.exit(1)

#Scaneando Portas
open_ports = portscan.port_scan(host, start_port, end_port) #realiza a varredura de portas usando a função do módulo portscan

for port in open_ports: #exibe as portas abertas encontradas
    print(f"[+] Porta Aberta: {port}")