import winreg
import socket
from datetime import datetime




def imprimir_informacion_adicional():

    # Mensaje adicional
    
    
    # Nombre del equipo
    nombre_equipo = socket.gethostname()
    
    # Fecha y hora actual
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Se ejecutó  la prueba Verificar Si El Sistema Operativo Está Activo ")
    print(f"Nombre del equipo: {nombre_equipo}")
    print(f"Fecha y hora: {fecha_actual}\n")

# Llamar a la función para imprimir la información adicional al inicio
imprimir_informacion_adicional()
# Abrir la clave de registro de Windows
clave = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion")

# Obtener el valor del campo "DigitalProductId"
digital_product_id, _ = winreg.QueryValueEx(clave, "DigitalProductId")

# Verificar si el sistema operativo está activado
if digital_product_id[52:66] != "000000000000000":
    print("El sistema operativo está activado.")
else:
    print("El sistema operativo no está activado.")
