import psutil
import socket
from datetime import datetime

def obtener_usuarios_conectados():
    usuarios_conectados = set()
    
    for usuario in psutil.users():
        usuarios_conectados.add(usuario.name)
    
    return usuarios_conectados

if __name__ == "__main__":
    # Nombre del equipo
    nombre_equipo = socket.gethostname()
    
    # Hora y fecha
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    usuarios = obtener_usuarios_conectados()
    cantidad_usuarios = len(usuarios)
    
    # Mostrar nombre del equipo y hora/fecha
    print("Se ejecutó  la prueba 9.2.1 Registro y cancelación de registro  de usuarios")
    print(f"Nombre del equipo: {nombre_equipo}")
    print(f"Fecha y hora: {fecha_actual}\n")

    if cantidad_usuarios > 0:
        print(f"Hay {cantidad_usuarios} usuario(s) conectado(s):")
        for usuario in usuarios:
            print(f"- {usuario}")
    else:
        print("No hay usuarios conectados en este momento.")


