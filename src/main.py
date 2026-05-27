import sys
from utils import validator
from module import dns,portscan
from module import banner
from datetime import datetime
import time

#Variaveis
target_host = None
max_threads = 150

#Coletando Entrada Do Usuário
try:
    host = sys.argv[1] #coleta entrada do usuário via linha de comando
    
    start_port =  int(sys.argv[2]) #coleta a porta inicial para varredura
    end_port = int(sys.argv[3]) #coleta a porta final para varred

except (IndexError, ValueError): #Caso o usuário não forneça um host ou portas inválidas, exibe uma mensagem de uso e encerra o programa
    print("Usage: python main.py <host> <start_port> <end_port>")
    sys.exit(1)

try:
    max_threads = int(sys.argv[4]) #coleta o número máximo de threads a serem usadas para varredura

    if int(sys.argv[4]) > 400: #Limita o número máximo de threads para evitar sobrecarga do sistema
        print("[-] O número máximo de threads permitido é 400. Usando 400 threads.")
        max_threads = 400

except (IndexError, ValueError): #Caso o usuário não forneça um número válido de threads, exibe uma mensagem de aviso e continua com o valor padrão
    pass


ip_valid = validator.is_valid_ip(host) #valida o host usando a função do módulo validator
hostname_valid = validator.is_hostname_valid(host) #valida o host usando a função do módulo validator

valid_port = validator.is_valid_port(start_port, end_port) #valida as portas usando a função do módulo validator

#Programa Principal
if not valid_port: #se as portas não forem válidas, exibe uma mensagem de erro e encerra o programa
    print("[-] Por favor, forneça um intervalo de portas válido (1-65535).")
    sys.exit(1)

if ip_valid:
    print(f"[+] IPv4 Detectado: {host}")
    target_host = host #define o host alvo como o endereço IP fornecido

elif hostname_valid:
    print(f"[+] Hostname Detectado: {host}")
    
    target_host = dns.resolver_dns(host) #define o host alvo como o endereço IP resolvido

    if target_host: #se a resolução for bem-sucedida, exibe o endereço IP resolvido
        print(f"[+] Endereço IP Resolvido: {target_host}")
    
    else: 
        print("[-] Falha ao resolver o hostname.")

else:
    print("[-] Por favor, forneça um endereço IP ou hostname válido.")
    sys.exit(1)

#Iniciando Registro De Tempo
start_time = datetime.now() #registra o horário de início da varredura
start_timer = time.perf_counter() #inicia o timer de desempenho



#Scaneando Portas Utilizando Threading

ports = portscan.port_scan_range(target_host, start_port, end_port, max_threads) #realiza a varredura de portas usando a função do módulo portscan

print(f"[+] Número de Threads: {max_threads}")

for port in ports: #exibe as portas abertas encontradas
    
    banner_info = banner.banner_grab(target_host,port) #tenta obter o banner do serviço usando a função do módulo banner

    print(f"[+] {port} {banner_info}") 
#Finalizando Registro De Tempo
end_time = datetime.now() #registra o horário de término da varredura
end_timer = time.perf_counter() #finaliza o timer de desempenho

total_time = end_time - start_time #calcula o tempo total decorrido
total_seconds = total_time.total_seconds() #converte o tempo total para segundos

#Printando Resultados
print("=" * 40) #imprime uma linha de separação
print(f"[+] Total de Portas Abertas Encontradas: {len(ports)}") #exibe o número total de portas abertas encontradas
print(f"\n[+] Início: {start_time.strftime('%Y/%m/%d %H:%M:%S')}") #exibe o horário de início da varredura
print(f"[+] Término: {end_time.strftime('%Y/%m/%d %H:%M:%S')}") #exibe o horário de término da varredura
print(f"\n[+] Varredura Concluída em: {total_seconds:.2f} segundos") #exibe o tempo total decorrido para a varredura
print("=" * 40) #imprime uma linha de separação