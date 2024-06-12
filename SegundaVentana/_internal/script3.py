import subprocess
import socket
from datetime import datetime

def obtener_privilegios_usuario():
    try:
        # Ejecuta la herramienta whoami para obtener información sobre los privilegios
        salida = subprocess.check_output(['whoami', '/priv'], universal_newlines=True)
        lineas = salida.splitlines()
        
        # Filtra las líneas que contienen información de privilegios
        privilegios = [linea.strip() for linea in lineas if "Privilege" in linea]
        
        # Nombre del equipo
        nombre_equipo = socket.gethostname()
        
        # Hora y fecha
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print("Se ejecutó  la prueba 9.2.2 Suministro de acceso de usuarios")
        print(f"Nombre del equipo: {nombre_equipo}")
        print(f"Fecha y hora: {fecha_actual}\n")

        if privilegios:
            print("Privilegios del usuario actual:")
            for privilegio in privilegios:
                print(privilegio)
        else:
            print("No se encontraron privilegios para el usuario actual.")
    except Exception as e:
        print(f"Error al obtener los privilegios: {str(e)}")

if __name__ == "__main__":
    obtener_privilegios_usuario()


