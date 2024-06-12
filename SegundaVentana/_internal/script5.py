import os
import socket
from datetime import datetime

def buscar_copias_de_seguridad_windows():
    # Ruta a la carpeta de copias de seguridad de Windows
    carpeta_copias = os.path.join(os.getenv('SystemDrive'), 'Users', 'TuUsuario', 'AppData', 'Local', 'Packages', 'Microsoft.Windows.SecHealthUI_cw5n1h2txyewy', 'LocalState', 'Files')

    copias_de_seguridad = []

    for raiz, _, archivos in os.walk(carpeta_copias):
        for archivo in archivos:
            if archivo.lower().endswith('.vhd') or archivo.lower().endswith('.vhdx'):
                ruta_completa = os.path.join(raiz, archivo)
                copias_de_seguridad.append(ruta_completa)

    return copias_de_seguridad

if __name__ == "__main__":
    # Nombre del equipo
    nombre_equipo = socket.gethostname()
    
    # Fecha actual
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Se ejecutó  la prueba 12.3 Copias de respaldo ")
    print(f"Nombre del equipo: {nombre_equipo}")
    print(f"Fecha y hora: {fecha_actual}\n")

    copias_encontradas = buscar_copias_de_seguridad_windows()

    if copias_encontradas:
        print("Se encontraron las siguientes copias de seguridad de Windows:")
        for copia in copias_encontradas:
            print(copia)
    else:
        print("No se encontraron copias de seguridad de Windows.")
