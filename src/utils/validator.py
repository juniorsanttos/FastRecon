from ipaddress import ip_address #importa a função para validar endereços IP


def is_valid_ip(host):
    try:
        ip_address(host) #tenta validar o host como um endereço IP
        return True

    except ValueError:
        return False

def is_hostname_valid(hostname):
    import socket #importa a biblioteca socket para validar hostnames

    try:
        socket.gethostbyname(hostname) #tenta resolver o hostname para um endereço IP
        return True
    except socket.gaierror:
        return False

def is_valid_port(start_port, end_port):
    if 0 < start_port <= 65535 and 0 < end_port <= 65535 and start_port <= end_port:
        return True
    else:
        return False