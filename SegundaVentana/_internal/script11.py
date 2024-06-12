import socket
from datetime import datetime

# Define las subredes que deben estar separadas
subred_a = '192.168.1.254'
subred_b = '192.168.1.110'

# Función para verificar si dos direcciones IP pertenecen a la misma subred
def are_in_same_subnet(ip1, ip2, subnet):
    return ip1[:len(subnet)] == ip2[:len(subnet)]

# Obtiene las direcciones IP de las interfaces de red activas
def get_active_ip_addresses():
    ip_addresses = []
    for interface, addrs in socket.if_nameindex():
        for addr_info in socket.getaddrinfo(socket.gethostname(), None):
            ip = addr_info[4][0]
            ip_addresses.append(ip)
    return ip_addresses

# Comprueba si las direcciones IP pertenecen a subredes diferentes
def check_network_separation(ip_addresses, subnet_a, subnet_b):
    for ip1 in ip_addresses:
        for ip2 in ip_addresses:
            if ip1 != ip2:
                if are_in_same_subnet(ip1, ip2, subnet_a) or are_in_same_subnet(ip1, ip2, subnet_b):
                    return False
    return True

# Función para imprimir la información adicional al inicio
def imprimir_informacion_adicional():

    # Mensaje adicional
    
    
    # Nombre del equipo
    nombre_equipo = socket.gethostname()
    
    # Fecha y hora actual
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Se ejecutó  la prueba 13.1.3 Separación en las redes")
    print(f"Nombre del equipo: {nombre_equipo}")
    print(f"Fecha y hora: {fecha_actual}\n")

# Llamar a la función para imprimir la información adicional al inicio
imprimir_informacion_adicional()

# Ejecuta la comprobación
active_ip_addresses = get_active_ip_addresses()
if check_network_separation(active_ip_addresses, subred_a, subred_b):
    print("La separación en las redes cumple con la norma ISO 27001-2013 13.1.3")
else:
    print("La separación en las redes no cumple con la norma ISO 27001-2013 13.1.3")
