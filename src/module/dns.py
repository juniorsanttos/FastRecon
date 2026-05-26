import socket #importa a biblioteca socket para resolver hostnames

def resolver_dns(host):

    try:
        ip_address = socket.gethostbyname(host) #tenta resolver o hostname para um endereço IP
        return ip_address

    except socket.gaierror:
        return None