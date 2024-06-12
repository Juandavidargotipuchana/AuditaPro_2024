import socket
from datetime import datetime

def verificar_puertos(ip, puertos):
    resultados = {}
    
    for puerto in puertos:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        resultado = sock.connect_ex((ip, puerto))
        
        if resultado == 0:
            resultados[puerto] = "Abierto"
        else:
            resultados[puerto] = "Cerrado"
        sock.close()

    return resultados

# IP del equipo que deseas verificar
equipo = '192.168.1.254'
puertos_a_verificar = [80, 443, 22, 3389]

resultados = verificar_puertos(equipo, puertos_a_verificar)

# Nombre del equipo
nombre_equipo = socket.gethostname()

# Hora y fecha
fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Mostrar resultados
print("Se ejecutó  la prueba 9.1.2 Acceso a redes y servicios en red")
print(f"Nombre del equipo: {nombre_equipo}")
print(f"Fecha y hora: {fecha_actual}\n")

for puerto, estado in resultados.items():
    print(f'Puerto {puerto}: {estado}')

# Mensaje adicional