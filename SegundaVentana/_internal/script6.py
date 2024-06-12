import os, socket
from datetime import datetime

# Ruta al directorio de respaldo
directorio_respaldo = "/ruta/al/directorio/respaldo"

# Nombre del archivo de respaldo
nombre_archivo_respaldo = "backup.tar.gz"

# Función para imprimir la información adicional al inicio
def imprimir_informacion_adicional():
    # Nombre del equipo
    nombre_equipo = socket.gethostname()
    
    # Fecha actual
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print("Se ejecutó  la prueba 12.3.1 Respaldo  de la información ")
    print(f"\nNombre del equipo: {nombre_equipo}")
    print(f"Fecha y hora: {fecha_actual}\n")

# Llamar a la función para imprimir la información adicional al inicio
imprimir_informacion_adicional()

def verificar_respaldo():
    ruta_completa = os.path.join(directorio_respaldo, nombre_archivo_respaldo)
    if os.path.exists(ruta_completa):
        return True
    else:
        return False

if verificar_respaldo():
    print("El respaldo de la información se ha realizado correctamente.")
else:
    print("El respaldo de la información no se ha realizado o no se encuentra el archivo de respaldo.")
