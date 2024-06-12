import urllib.request
import socket
from datetime import datetime

def imprimir_informacion_adicional():

    # Mensaje adicional
    
    
    # Nombre del equipo
    nombre_equipo = socket.gethostname()
    
    # Fecha y hora actual
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Se ejecutó  la prueba Verificar Conectividad a Internet")
    print(f"Nombre del equipo: {nombre_equipo}")
    print(f"Fecha y hora: {fecha_actual}\n")

# Llamar a la función para imprimir la información adicional al inicio
imprimir_informacion_adicional()

def test_internet_connection():
    try:
        # Intentar abrir una conexión a un sitio web conocido (en este caso, google.com)
        urllib.request.urlopen("http://www.google.com", timeout=5)
        print("Conexión a Internet establecida: ¡La prueba fue exitosa!")
    except urllib.error.URLError as e:
        print("No se pudo establecer conexión a Internet: ", e.reason)

if __name__ == "__main__":
    # Realizar la prueba de conectividad a Internet
    test_internet_connection()
