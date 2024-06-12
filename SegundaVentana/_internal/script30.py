import socket
from datetime import datetime



def imprimir_informacion_adicional():

    # Mensaje adicional
    
    
    # Nombre del equipo
    nombre_equipo = socket.gethostname()
    
    # Fecha y hora actual
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Se ejecutó  la prueba Verificar Restricciones En El Host ")
    print(f"Nombre del equipo: {nombre_equipo}")
    print(f"Fecha y hora: {fecha_actual}\n")

# Llamar a la función para imprimir la información adicional al inicio
imprimir_informacion_adicional()

def check_restrictions():
    try:
        # Creamos un objeto de socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Intentamos conectar a una dirección y puerto conocidos
        s.connect(('www.google.com', 80))
        
        # Si la conexión es exitosa, no hay restricciones
        print("No hay restricciones en el host de tu PC.")
        
    except socket.error as e:
        # Si hay un error al conectar, puede haber una restricción
        print("Puede haber una restricción en el host de tu PC:", e)

check_restrictions()
