import subprocess
import socket
from datetime import datetime

# Función para imprimir la información adicional al inicio
def imprimir_informacion_adicional():
    # Nombre del equipo
    nombre_equipo = socket.gethostname()
    
    # Fecha y hora actual
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Se ejecutó  la prueba 12.4 Registro  y seguimiento ")
    print(f"Nombre del equipo: {nombre_equipo}")
    print(f"Fecha y hora: {fecha_actual}\n")

# Llamar a la función para imprimir la información adicional al inicio
imprimir_informacion_adicional()

# Función para verificar si la auditoría de eventos de seguridad está habilitada
def is_security_auditing_enabled():
    try:
        # Ejecutar el comando "auditpol /get /category:*"
        result = subprocess.check_output(["auditpol", "/get", "/category:*"], stderr=subprocess.STDOUT, text=True)
        
        # Buscar si "Audit Policy Configuration" aparece en la salida
        return "Audit Policy Configuration" in result
    except subprocess.CalledProcessError:
        return False

# Verificar si la auditoría de seguridad está habilitada
if is_security_auditing_enabled():
    print("La auditoría de eventos de seguridad está habilitada en Windows.")
else:
    print("La auditoría de eventos de seguridad no está habilitada en Windows.")
