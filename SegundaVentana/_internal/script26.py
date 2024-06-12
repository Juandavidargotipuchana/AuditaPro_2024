import win32com.client
import socket
from datetime import datetime



def imprimir_informacion_adicional():

    # Mensaje adicional
    
    
    # Nombre del equipo
    nombre_equipo = socket.gethostname()
    
    # Fecha y hora actual
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Se ejecutó  la prueba Verificar Estado del Antivirus ")
    print(f"Nombre del equipo: {nombre_equipo}")
    print(f"Fecha y hora: {fecha_actual}\n")

# Llamar a la función para imprimir la información adicional al inicio
imprimir_informacion_adicional()


def check_malware_scan():
    wmi = win32com.client.GetObject("winmgmts:\\\\.\\root\\securitycenter2")

    # Obtener información sobre la protección antivirus
    antivirus_protection = wmi.ExecQuery("SELECT * FROM AntivirusProduct")

    if len(antivirus_protection) == 0:
        print("No se ha encontrado ningún software antivirus en el sistema.")
    else:
        for product in antivirus_protection:
            print("Nombre del producto antivirus:", product.displayName)
            print("Estado de la protección antivirus:", product.productState)
            if product.productState == 266240:
                print("El escaneo de malware está en progreso.")
            else:
                print("No hay escaneo de malware en curso.")

if __name__ == '__main__':
    check_malware_scan()
