import psutil
import socket
from datetime import datetime


def imprimir_informacion_adicional():

    # Mensaje adicional
    
    
    # Nombre del equipo
    nombre_equipo = socket.gethostname()
    
    # Fecha y hora actual
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Se ejecutó  la prueba Verificar Cuantos Programas Están Instalados")
    print(f"Nombre del equipo: {nombre_equipo}")
    print(f"Fecha y hora: {fecha_actual}\n")

# Llamar a la función para imprimir la información adicional al inicio
imprimir_informacion_adicional()



def obtener_numero_programas_instalados():
    # Obtener la lista de procesos en ejecución
    procesos = psutil.process_iter()

    # Lista para almacenar los nombres únicos de los programas
    programas = []

    # Recorrer los procesos y obtener el nombre del programa
    for proceso in procesos:
        try:
            nombre = proceso.name()
            if nombre not in programas:
                programas.append(nombre)
        except (psutil.AccessDenied, psutil.NoSuchProcess):
            pass

    return len(programas)

# Obtener el número de programas instalados
numero_programas = obtener_numero_programas_instalados()

print("Número de programas instalados:", numero_programas)
