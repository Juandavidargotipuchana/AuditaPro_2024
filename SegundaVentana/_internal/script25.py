import winreg
import socket
from datetime import datetime

def imprimir_informacion_adicional():

    # Mensaje adicional
    
    
    # Nombre del equipo
    nombre_equipo = socket.gethostname()
    
    # Fecha y hora actual
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Se ejecutó  la prueba Verificación Del  Firewall ")
    print(f"Nombre del equipo: {nombre_equipo}")
    print(f"Fecha y hora: {fecha_actual}\n")

# Llamar a la función para imprimir la información adicional al inicio
imprimir_informacion_adicional()


# Abre la clave del registro que contiene la configuración del firewall de Windows
reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\StandardProfile")

# Lee el valor de la clave "EnableFirewall"
enable_firewall, _ = winreg.QueryValueEx(reg_key, "EnableFirewall")

# Comprueba si el firewall está activado o no
if enable_firewall == 0:
    print("El firewall de Windows está desactivado.")
else:
    print("El firewall de Windows está activado.")