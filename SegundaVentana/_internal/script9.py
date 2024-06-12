import subprocess
import socket
from datetime import datetime

# Función para imprimir la información adicional al inicio
def imprimir_informacion_adicional():
    # Nombre del equipo
    nombre_equipo = socket.gethostname()
    
    # Fecha y hora actual
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Se ejecutó  la prueba 13.1.1 Controles de redes")
    print(f"Nombre del equipo: {nombre_equipo}")
    print(f"Fecha y hora: {fecha_actual}\n")

# Llamar a la función para imprimir la información adicional al inicio
imprimir_informacion_adicional()

# Define la lista de puertos que se deben comprobar
puertos_a_comprobar = [80, 443, 22]  # Puedes personalizar esta lista según tus necesidades

# Comprueba si el firewall de Windows está habilitado
def firewall_habilitado():
    try:
        subprocess.check_output(["netsh", "advfirewall", "show", "allprofiles"])
        return True
    except subprocess.CalledProcessError:
        return False

# Comprueba si un puerto específico está abierto
def puerto_abierto(puerto):
    try:
        subprocess.check_output(["netsh", "advfirewall", "firewall", "show", "rule", f"name=port={puerto}"])
        return True
    except subprocess.CalledProcessError:
        return False

# Comprueba el cumplimiento de los controles de redes
def verificar_controles_de_red():
    if firewall_habilitado():
        print("El firewall de Windows está habilitado.")
        for puerto in puertos_a_comprobar:
            if puerto_abierto(puerto):
                print(f"El puerto {puerto} está abierto y permitido.")
            else:
                print(f"El puerto {puerto} está cerrado o denegado.")
    else:
        print("El firewall de Windows no está habilitado. Asegúrate de configurarlo adecuadamente.")

# Ejecuta la comprobación
verificar_controles_de_red()
