import subprocess
import socket
from datetime import datetime


def imprimir_informacion_adicional():

    # Mensaje adicional
        
    # Nombre del equipo
    nombre_equipo = socket.gethostname()
    
    # Fecha y hora actual
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Se ejecutó  la prueba Ver Actualizaciones Instaladas ")
    print(f"Nombre del equipo: {nombre_equipo}")
    print(f"Fecha y hora: {fecha_actual}\n")

# Llamar a la función para imprimir la información adicional al inicio
imprimir_informacion_adicional()
# Ejecutar un comando de CMD
comando = 'wmic qfe list'
resultado = subprocess.run(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Imprimir la salida estándar y la salida de error
print("Salida estándar:")
print(resultado.stdout)
print("Salida de error:")
print(resultado.stderr)

# Verificar el código de retorno
if resultado.returncode == 0:
    print("El comando se ejecutó correctamente.")
else:
    print(f"El comando retornó un código de error {resultado.returncode}.")
