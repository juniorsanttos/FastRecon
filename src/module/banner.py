import socket

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
}

def banner_grab(host, port):
        
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock: #cria um socket TCP/IP

            sock.settimeout(2) #define um tempo limite para a conexão
            sock.connect((host, port)) #tenta conectar ao host e porta especificados


            if port in [80, 8080, 8000]: #para portas HTTP comuns, tenta identificar o servidor web
                
                try:
                    request = (
                        f"HEAD / HTTP/1.1\r\n"
                        f"Host: {host}\r\n"
                    ) #prepara uma requisição HTTP HEAD para tentar obter o banner do servidor web

                    sock.sendall(request.encode()) #envia uma requisição HTTP para tentar obter o banner do servidor web
                    response = sock.recv(1024).decode('utf-8', errors='ignore') #tenta receber a resposta do servidor e decodificar como UTF-8, ignorando erros de decodificação
                    

                    if response: #se a resposta for recebida, procura por uma linha que comece com "Server:" para identificar o servidor web
                        for line in response.splitlines(): #itera sobre as linhas da resposta
                            
                            if line.lower().startswith("server:"): #procura por uma linha que comece com "Server:"
                            
                                return line.split(":", 1)[1].strip() #retorna o valor do campo "Server:", removendo espaços em branco

                except:
                    pass

            #Tenta receber o banner do serviço
            try:
                banner = sock.recv(1024).decode('utf-8', errors='ignore') #tenta receber o banner do serviço e decodificar como UTF-8, ignorando erros de decodificação
                return banner.strip() #retorna o banner recebido, removendo espaços em branco
            
            except:
                pass

            if port in COMMON_PORTS: #se a porta for uma porta comum, retorna o nome do serviço correspondente
                return COMMON_PORTS[port] #retorna o nome do serviço correspondente à porta comum
            
            else:
                pass
            
            return "Unknown Service" #se não for possível obter o banner, retorna "Unknown Service"
            
    except:
        return None #se a conexão falhar, retorna None