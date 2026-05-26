def port_scan(host, start_port, end_port):
    import socket #importa a biblioteca socket para criar conexões de rede

    open_ports = [] #lista para armazenar as portas abertas

    for port in range(start_port, end_port + 1): #itera sobre o intervalo de portas fornecido

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria um socket TCP/IP         
        sock.settimeout(1) #define um tempo limite para a conexão

        result = sock.connect_ex((host, port)) #tenta conectar ao host e porta especificados

        if result == 0: #se a conexão for bem-sucedida, a porta está aberta
            open_ports.append(port) #adiciona a porta à lista de portas abertas
        
        sock.close() #fecha o socket

    return open_ports #retorna a lista de portas abertas
