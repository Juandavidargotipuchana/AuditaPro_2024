import subprocess
import socket
from datetime import datetime

def imprimir_informacion_adicional():

    # Mensaje adicional
    
    
    # Nombre del equipo
    nombre_equipo = socket.gethostname()
    
    # Fecha y hora actual
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Se ejecutó  la prueba Mostrar Información De Red  ")
    print(f"Nombre del equipo: {nombre_equipo}")
    print(f"Fecha y hora: {fecha_actual}\n")

# Llamar a la función para imprimir la información adicional al inicio
imprimir_informacion_adicional()


# Ejecutar un comando de CMD
comando = 'netstat'
with subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as proceso:
    # Leer y mostrar la salida estándar línea por línea en tiempo real
    print("Salida estándar:")
    for linea in proceso.stdout:
        print(linea, end='')
    
    # Leer y mostrar la salida de error si la hay
    print("Salida de error:")
    for linea_error in proceso.stderr:
        print(linea_error, end='')

# Verificar el código de retorno
if proceso.returncode == 0:
    print("El comando se ejecutó correctamente.")
else:
    print(f"El comando retornó un código de error {proceso.returncode}.")
