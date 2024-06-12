import socket
from datetime import datetime

def check_server(host, port):
    try:
        # Intentar crear un objeto socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)  # Establecer un tiempo de espera en segundos
            s.connect((host, port))
            return True
    except (socket.timeout, ConnectionRefusedError):
        return False

# Función para imprimir la información adicional al inicio
def imprimir_informacion_adicional():
    # Nombre del equipo
    nombre_equipo = socket.gethostname()
    
    # Fecha y hora actual
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Se ejecutó  la prueba 13.1.2 Seguridad de los servicios de red ")
    print(f"Nombre del equipo: {nombre_equipo}")
    print(f"Fecha y hora: {fecha_actual}\n")

# Llamar a la función para imprimir la información adicional al inicio
imprimir_informacion_adicional()

# Dirección IP o nombre de dominio del servidor que deseas verificar
host = "192.168.1.254"

# Puerto que deseas verificar (por ejemplo, el puerto 80 para HTTP)
port = 80

if check_server(host, port):
    print(f"El servidor {host}:{port} está en línea y accesible.")
else:
    print(f"No se pudo conectar al servidor {host}:{port}.")

