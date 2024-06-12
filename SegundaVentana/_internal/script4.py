import secrets
import string
import socket
from datetime import datetime

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(secrets.choice(caracteres) for _ in range(longitud))
    return contrasena

if __name__ == "__main__":
    # Nombre del equipo
    nombre_equipo = socket.gethostname()
    
    # Fecha actual
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print("Se ejecutó  la prueba 9.4.3 Sistema de gestión de contraseñas")
    print(f"Nombre del equipo: {nombre_equipo}")
    print(f"Fecha y hora: {fecha_actual}\n")
    
    longitudes_contraseñas = [8, 10, 12, 16, 20]

    for longitud in longitudes_contraseñas:
        contrasena = generar_contrasena(longitud)
        print(f"Contraseña de {longitud} caracteres: {contrasena}")

