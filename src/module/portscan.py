import socket #importa a biblioteca socket para criar conexões de rede
from concurrent.futures import ThreadPoolExecutor #importa a classe ThreadPoolExecutor para gerenciar threads
from concurrent.futures import as_completed #importa a função as_completed para lidar com os resultados das threads conforme elas terminam

def port_scan(host, port):

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock: #cria um socket TCP/IP

        sock.settimeout(1) #define um tempo limite para a conexão

        result = sock.connect_ex((host, port)) #tenta conectar ao host e porta especificados

        if result == 0: #se a conexão for bem-sucedida, a porta está aberta
            return port #retorna a porta aberta encontrada

def port_scan_range(host, start_port, end_port):

    open_ports = [] #lista para armazenar as portas abertas encontradas

    with ThreadPoolExecutor(max_workers=150) as ex:
        
        futures = [] #lista para armazenar os objetos Future retornados pela execução das threads

        for port in range(start_port, end_port + 1): #itera sobre o intervalo de portas fornecido
            
            futures.append(ex.submit(port_scan, host, port)) #envia a função de varredura de porta para execução em uma thread
        

        for f in as_completed(futures): #lida com os resultados das threads conforme elas terminam
            
            result = f.result() #obtém o resultado da thread

            if result:
                open_ports.append(result) #se a porta estiver aberta, adiciona à lista de portas abertas

    return open_ports.sort() #retorna a lista de portas abertas encontradas