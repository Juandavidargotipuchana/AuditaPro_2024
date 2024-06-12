import subprocess
import re
import socket
from datetime import datetime




# Ejecutar un comando de CMD
comando = 'wmic os get lastbootuptime'
resultado = subprocess.run(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

def imprimir_informacion_adicional():

    # Mensaje adicional
    
    
    # Nombre del equipo
    nombre_equipo = socket.gethostname()
    
    # Fecha y hora actual
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Se ejecutó  la prueba Fecha Última Vez Que Se Inició El Sistema ")
    print(f"Nombre del equipo: {nombre_equipo}")
    print(f"Fecha y hora: {fecha_actual}\n")

# Llamar a la función para imprimir la información adicional al inicio
imprimir_informacion_adicional()



# Verificar el código de retorno
if resultado.returncode == 0:
    # Extraer la fecha y hora de la salida
    fecha_hora_inicio = re.search(r'(\d{14})', resultado.stdout)
    if fecha_hora_inicio:
        fecha_hora_inicio = fecha_hora_inicio.group(1)
        # Convertir la cadena a formato de fecha y hora
        fecha_hora_inicio = datetime.strptime(fecha_hora_inicio, '%Y%m%d%H%M%S')
        # Imprimir la fecha y hora de inicio formateadas
        print("Fecha y hora de inicio del sistema:", fecha_hora_inicio.strftime('%Y-%m-%d %H:%M:%S'))
    else:
        print("No se pudo obtener la fecha y hora de inicio del sistema.")
else:
    print(f"El comando retornó un código de error {resultado.returncode}.")