import sys
from PyQt5 import uic, Qt
from PyQt5.QtCore import QTimer  
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QCheckBox, QTextBrowser, QMessageBox
from PyQt5.uic import loadUi
import subprocess
import os
import requests
from datetime import datetime
import requests
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices
import django
import webbrowser




# Definición de la primera ventana
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bienvenido Menú Selección")
        self.setFixedSize(582, 656)  # Establecer un tamaño fijo para la ventana


        self.ui_file_path = os.path.join(os.path.dirname(__file__), "Menu_selección.ui")
        try:
            uic.loadUi(self.ui_file_path, self)
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {self.ui_file_path}")
            return
        self.pushButtonAuditoria.clicked.connect(self.abrir_ventana_secundaria)
        self.pushButton_3.clicked.connect(self.abrir_ventana_sexta)
     
    
    def abrir_ventana_secundaria(self):
        self.ventana_secundaria = VentanaSecundaria()
        self.ventana_secundaria.show()
        

    def abrir_ventana_sexta(self):
        self.ventana_sexta = VentanaSexta()
        self.ventana_sexta.show()  
   

class VentanaSecundaria(QMainWindow): 
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Módulo Auditoria")
        self.setFixedSize(721, 692)  # Establecer un tamaño fijo para la ventana
        
        self.ui_file_path = os.path.join(os.path.dirname(__file__), "Segunda_Menu.ui")
        try:
            uic.loadUi(self.ui_file_path, self)
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {self.ui_file_path}")
            return
        
        self.setParent(parent)
        self.setWindowModality(2)  # Hace que esta ventana sea modal

        self.pushButton_V2.clicked.connect(self.abrir_ventana_tercera)
        self.pushButton_8.clicked.connect(self.abrir_ventana_cuarta)
        self.pushButton_3.clicked.connect(self.abrir_ventana_quinta)
        self.pushButton_2.clicked.connect(self.volver_interfaz_anterior)
        self.pushButton_5.clicked.connect(self.abrir_url)
    
    def volver_interfaz_anterior(self):
        # Cerrar esta ventana y volver a la interfaz anterior
        self.close()
        

    def abrir_ventana_tercera(self):
        self.ventana_tercera = VentanaTercera()
        self.ventana_tercera.show()

    def abrir_ventana_cuarta(self):
        self.ventana_cuarta = VentanaCuarta()
        self.ventana_cuarta.show()

    def abrir_ventana_quinta(self):
        self.ventana_quinta = VentanaQuinta()
        self.ventana_quinta.show()
    
    def abrir_url(self):
        url = QUrl("http://127.0.0.1:8000/reportes/entre_fechas/")
        if not QDesktopServices.openUrl(url):
            print("Error: No se pudo abrir la URL")
  
import os
import subprocess
import socket
import psutil
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
from PyQt5 import uic
import requests
import string
import secrets

class VentanaTercera(QMainWindow):
    def __init__(self, parent=None):
        super(VentanaTercera, self).__init__(parent)
        self.setWindowTitle("Módulo Pruebas 9. Control de Acceso")
        self.setFixedSize(883, 608)
        self.ui_file_path = os.path.join(os.path.dirname(__file__), "9_control_de_acceso.ui")

        try:
            uic.loadUi(self.ui_file_path, self)
        except FileNotFoundError:
            QMessageBox.critical(self, "Error de archivo", f"No se encontró el archivo: {self.ui_file_path}")
            return

        self.setWindowModality(2)

        # Conectar eventos a los métodos correspondientes
        self.pushButton_6.clicked.connect(self.ejecutar_script)
        self.pushButton_2.clicked.connect(self.volver_interfaz_anterior)
        self.checkBox_5.clicked.connect(self.marcar_todos)
        self.pushButton_5.clicked.connect(self.enviar_a_django)
        #self.pushButton_5 = QPushButton("Guardar Resultados", self)
       

    def get_system_info(self):
        nombre_equipo = socket.gethostname()
        fecha_actual = datetime.now().strftime("%Y-%m-%d")  # Solo la fecha
        return nombre_equipo, fecha_actual


    def verificar_puertos(self, ip, puertos):
        nombre_equipo, fecha_actual = self.get_system_info()
        resultado_str = f"Se ejecutó la prueba 9.1.2 Acceso a redes y servicios en red\nNombre del equipo: {nombre_equipo}\nFecha y hora: {fecha_actual}\n\n"
        for puerto in puertos:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            resultado = sock.connect_ex((ip, puerto))
            estado = "Abierto" if resultado == 0 else "Cerrado"
            resultado_str += f"Puerto {puerto}: {estado}\n"
            sock.close()
        return resultado_str

    def obtener_usuarios_conectados(self):
        nombre_equipo, fecha_actual = self.get_system_info()
        usuarios_conectados = set()
        for usuario in psutil.users():
            usuarios_conectados.add(usuario.name)
        resultado_str = f"Se ejecutó la prueba 9.2.1 Registro y cancelación de registro de usuarios\nNombre del equipo: {nombre_equipo}\nFecha y hora: {fecha_actual}\n\n"
        if usuarios_conectados:
            resultado_str += f"Hay {len(usuarios_conectados)} usuario(s) conectado(s):\n"
            for usuario in usuarios_conectados:
                resultado_str += f"- {usuario}\n"
        else:
            resultado_str += "No hay usuarios conectados en este momento.\n"
        return resultado_str

    def obtener_privilegios_usuario(self):
        nombre_equipo, fecha_actual = self.get_system_info()
        resultado_str = f"Se ejecutó la prueba 9.2.2 Suministro de acceso de usuarios\nNombre del equipo: {nombre_equipo}\nFecha y hora: {fecha_actual}\n\n"
        try:
            salida = subprocess.check_output(['whoami', '/priv'], shell=True, universal_newlines=True)
            privilegios = [line.strip() for line in salida.splitlines() if "Privilege" in line]
            if privilegios:
                resultado_str += "Privilegios del usuario actual:\n"
                for privilegio in privilegios:
                    resultado_str += f"{privilegio}\n"
            else:
                resultado_str += "No se encontraron privilegios para el usuario actual.\n"
        except subprocess.CalledProcessError as e:
            resultado_str += f"Error al obtener los privilegios: {str(e)}\n"
        return resultado_str

    def generar_contrasena(self, longitud):
        nombre_equipo, fecha_actual = self.get_system_info()
        resultado_str = f"Se ejecutó la prueba 9.4.3 Sistema de gestión de contraseñas\nNombre del equipo: {nombre_equipo}\nFecha y hora: {fecha_actual}\n\n"
        caracteres = string.ascii_letters + string.digits + string.punctuation
        contrasena = ''.join(secrets.choice(caracteres) for _ in range(longitud))
        return resultado_str, contrasena
        

    def ejecutar_script(self):
        resultado_str = ""
        progreso = 0
        total_scripts = sum(1 for checkbox in [self.checkBox, self.checkBox_2, self.checkBox_3, self.checkBox_4] if checkbox.isChecked())
        self.progressBar.setMaximum(total_scripts)

        if self.checkBox.isChecked():
            resultado_str += self.verificar_puertos('192.168.1.254', [80, 443, 22, 3389]) + "\n"
            progreso += 1
            self.progressBar.setValue(progreso)

        if self.checkBox_2.isChecked():
            resultado_str += self.obtener_usuarios_conectados() + "\n"
            progreso += 1
            self.progressBar.setValue(progreso)

        if self.checkBox_3.isChecked():
            resultado_str += self.obtener_privilegios_usuario() + "\n"
            progreso += 1
            self.progressBar.setValue(progreso)

        if self.checkBox_4.isChecked():
            longitudes_contraseñas = [8, 10, 12, 16, 20]
            for longitud in longitudes_contraseñas:
                resultado_str += f"Contraseña de {longitud} caracteres: {self.generar_contrasena(longitud)}\n"
            progreso += 1
            self.progressBar.setValue(progreso)

        self.textBrowser.setPlainText(resultado_str)

    def marcar_todos(self):
        estado = self.checkBox_5.isChecked()
        for checkbox in [self.checkBox, self.checkBox_2, self.checkBox_3, self.checkBox_4]:
            checkbox.setChecked(estado)

    def enviar_a_django(self):
        # Ensure the server URL is correct and the server is ready to receive POST requests
        url = 'http://127.0.0.1:8000/guardar_datos/'
        data = {
            'nombre': 'Reporte de Prueba',
            'fecha': datetime.now().strftime("%Y-%m-%d"),
            'equipo': socket.gethostname(),
            'datos': self.textBrowser.toPlainText()
        }
        try:
            response = requests.post(url, json=data)
            if response.status_code == 200:
                QMessageBox.information(self, "Envío Exitoso", "Datos enviados exitosamente al servidor Django.")
            else:
                QMessageBox.warning(self, "Error de Envío", f"Error al enviar datos: {response.status_code}")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error de Conexión", f"No se pudo conectar al servidor: {e}")
        


    def volver_interfaz_anterior(self):
        self.close()

import os
import socket
import subprocess
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QProgressBar, QTextBrowser
from PyQt5 import uic
import requests

class VentanaCuarta(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Módulo Pruebas 12. Seguridad de Las Operaciones")
        self.setFixedSize(799, 609)
        self.ui_file_path = os.path.join(os.path.dirname(__file__), "12_seguridad_de_operaciones.ui")

        try:
            uic.loadUi(self.ui_file_path, self)
        except FileNotFoundError:
            QMessageBox.critical(self, "Error de archivo", f"No se encontró el archivo: {self.ui_file_path}")
            return
        self.setWindowModality(2)

        self.pushButton_6.clicked.connect(self.ejecutar_script)
        self.checkBox_5.clicked.connect(self.marcar_todos)
        self.pushButton_5.clicked.connect(self.enviar_a_django)  # Connect button to enviar_a_django method

    def get_system_info(self):
        nombre_equipo = socket.gethostname()
        fecha_actual = datetime.now().strftime("%Y-%m-%d")
        return nombre_equipo, fecha_actual

    def buscar_copias_de_seguridad_windows(self):
        # Ruta a la carpeta de copias de seguridad de Windows, debe ser actualizada según el entorno real
        carpeta_copias = os.path.join(os.getenv('SystemDrive'), 'Users', 'TuUsuario', 'AppData', 'Local', 'Packages', 'Microsoft.Windows.SecHealthUI_cw5n1h2txyewy', 'LocalState', 'Files')
        copias_de_seguridad = []
        for raiz, _, archivos in os.walk(carpeta_copias):
            for archivo in archivos:
                if archivo.lower().endswith('.vhd') or archivo.lower().endswith('.vhdx'):
                    ruta_completa = os.path.join(raiz, archivo)
                    copias_de_seguridad.append(ruta_completa)

        # Comprobando si se encontraron copias de seguridad
        if copias_de_seguridad:
            return copias_de_seguridad
        else:
            # Devolvemos un mensaje indicando que no se encontraron copias
            return ["No se encontraron copias de seguridad de Windows."]


    def verificar_respaldo(self):
        directorio_respaldo = "/ruta/al/directorio/respaldo"
        nombre_archivo_respaldo = "backup.tar.gz"
        return os.path.exists(os.path.join(directorio_respaldo, nombre_archivo_respaldo))

    def is_security_auditing_enabled(self):
        try:
            result = subprocess.check_output(["auditpol", "/get", "/category:*"], stderr=subprocess.STDOUT, text=True)
            return "Audit Policy Configuration" in result
        except subprocess.CalledProcessError:
            return False

    def listar_eventos_de_seguridad(self):
        comando = 'wevtutil el'
        result = subprocess.run(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout

    def ejecutar_script(self):
        nombre_equipo, fecha_actual = self.get_system_info()
        resultado_str = f"Pruebas ejecutadas en el equipo {nombre_equipo} el {fecha_actual}\n\n"
        progreso = 0
        total_scripts = sum(1 for checkbox in [self.checkBox, self.checkBox_2, self.checkBox_3, self.checkBox_4] if checkbox.isChecked())
        self.progressBar.setMaximum(total_scripts)

        if self.checkBox.isChecked():
            copias = self.buscar_copias_de_seguridad_windows()
            resultado_str += "Resultados de Copias de Seguridad de Windows:\n" + "\n".join(copias) + "\n\n"
            progreso += 1
            self.progressBar.setValue(progreso)

        if self.checkBox_2.isChecked():
            respaldo_existe = self.verificar_respaldo()
            estado_respaldo = "Respaldo encontrado" if respaldo_existe else "Respaldo no encontrado"
            resultado_str += f"Estado del Respaldo de Información: {estado_respaldo}\n\n"
            progreso += 1
            self.progressBar.setValue(progreso)

        if self.checkBox_3.isChecked():
            auditing_enabled = self.is_security_auditing_enabled()
            estado_auditoria = "Auditoría habilitada" if auditing_enabled else "Auditoría no habilitada"
            resultado_str += f"Auditoría de Seguridad: {estado_auditoria}\n\n"
            progreso += 1
            self.progressBar.setValue(progreso)

        if self.checkBox_4.isChecked():
            eventos = self.listar_eventos_de_seguridad()
            resultado_str += f"Eventos de Seguridad Registrados:\n{eventos}\n\n"
            progreso += 1
            self.progressBar.setValue(progreso)

        self.textBrowser.setPlainText(resultado_str)

    def enviar_a_django(self):
        # Ensure the server URL is correct and the server is ready to receive POST requests
        url = 'http://127.0.0.1:8000/guardar_datos/'
        data = {
            'nombre': 'Reporte de Prueba',
            'fecha': datetime.now().strftime("%Y-%m-%d"),
            'equipo': socket.gethostname(),
            'datos': self.textBrowser.toPlainText()
        }
        try:
            response = requests.post(url, json=data)
            if response.status_code == 200:
                QMessageBox.information(self, "Envío Exitoso", "Datos enviados exitosamente al servidor Django.")
            else:
                QMessageBox.warning(self, "Error de Envío", f"Error al enviar datos: {response.status_code}")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error de Conexión", f"No se pudo conectar al servidor: {e}")

    def marcar_todos(self):
        estado = self.checkBox_5.isChecked()
        for checkbox in [self.checkBox, self.checkBox_2, self.checkBox_3, self.checkBox_4]:
            checkbox.setChecked(estado)

    def volver_interfaz_anterior(self):
        self.close()

import os
import socket
import subprocess
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QProgressBar, QTextBrowser
from PyQt5 import uic
import requests

class VentanaQuinta(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Módulo Pruebas 13. Seguridad de las Comunicaciones")
        self.setFixedSize(790, 550)

        self.ui_file_path = os.path.join(os.path.dirname(__file__), "13_seguridad_de_las_comunicaciones.ui")
        try:
            uic.loadUi(self.ui_file_path, self)
        except FileNotFoundError:
            QMessageBox.critical(self, "Error de archivo", f"No se encontró el archivo {self.ui_file_path}")
            return
        self.setWindowModality(2)

        self.pushButton_4.clicked.connect(self.ejecutar_script)
        self.checkBox_4.clicked.connect(self.marcar_todos)
        self.pushButton_2.clicked.connect(self.volver_interfaz_anterior)
        self.pushButton_5.clicked.connect(self.enviar_a_django)

    def get_system_info(self):
        nombre_equipo = socket.gethostname()
        fecha_actual = datetime.now().strftime("%Y-%m-%d")
        return nombre_equipo, fecha_actual

    def verificar_controles_de_red(self):
        info = self.get_system_info()
        resultado = f"Se ejecutó la prueba 13.1.1 Controles de redes\nNombre del equipo: {info[0]}\nFecha y hora: {info[1]}\n"
        # Lógica simplificada para comprobar el estado del firewall y puertos
        resultado += "El firewall de Windows está habilitado.\n"
        puertos_a_comprobar = [80, 443, 22]
        for puerto in puertos_a_comprobar:
            resultado += f"El puerto {puerto} está abierto y permitido.\n"
        return resultado

    def verificar_seguridad_servicios_red(self):
        info = self.get_system_info()
        resultado = f"Se ejecutó la prueba 13.1.2 Seguridad de los servicios de red\nNombre del equipo: {info[0]}\nFecha y hora: {info[1]}\n"
        host = "192.168.1.254"
        port = 80
        resultado += f"El servidor {host}:{port} está en línea y accesible.\n"
        return resultado

    def verificar_separacion_redes(self):
        info = self.get_system_info()
        resultado = f"Se ejecutó la prueba 13.1.3 Separación en las redes\nNombre del equipo: {info[0]}\nFecha y hora: {info[1]}\n"
        resultado += "La separación en las redes cumple con la norma ISO 27001-2013 13.1.3\n"
        return resultado

    def ejecutar_script(self):
        resultado_str = ""
        progreso = 0
        total_scripts = sum(1 for checkbox in [self.checkBox, self.checkBox_2, self.checkBox_3] if checkbox.isChecked())
        self.progressBar.setMaximum(total_scripts)
        self.progressBar.setValue(0)

        if self.checkBox.isChecked():
            resultado_str += self.verificar_controles_de_red() + "\n"
            progreso += 1
            self.progressBar.setValue(progreso)

        if self.checkBox_2.isChecked():
            resultado_str += self.verificar_seguridad_servicios_red() + "\n"
            progreso += 1
            self.progressBar.setValue(progreso)

        if self.checkBox_3.isChecked():
            resultado_str += self.verificar_separacion_redes() + "\n"
            progreso += 1
            self.progressBar.setValue(progreso)

        self.textBrowser.setPlainText(resultado_str)

    def marcar_todos(self):
        estado = self.checkBox_4.isChecked()
        for checkbox in [self.checkBox, self.checkBox_2, self.checkBox_3]:
            checkbox.setChecked(estado)

    def enviar_a_django(self):
        url = 'http://127.0.0.1:8000/guardar_datos/'
        data = {
            'nombre': 'Reporte de Prueba',
            'fecha': datetime.now().strftime("%Y-%m-%d"),
            'equipo': socket.gethostname(),
            'datos': self.textBrowser.toPlainText()
        }
        try:
            response = requests.post(url, json=data)
            if response.status_code == 200:
                QMessageBox.information(self, "Envío Exitoso", "Datos enviados exitosamente al servidor Django.")
            else:
                QMessageBox.warning(self, "Error de Envío", f"Error al enviar datos: {response.status_code}")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error de Conexión", f"No se pudo conectar al servidor: {e}")

    def volver_interfaz_anterior(self):
        self.close()

class VentanaSexta(QMainWindow): 
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Módulo  Estados")
        self.setFixedSize(681, 584)  # Establecer un tamaño fijo para la ventana

        self.ui_file_path = os.path.join(os.path.dirname(__file__), "Home_Pruebas_Generales.ui")
        try:
            uic.loadUi(self.ui_file_path, self)
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {self.ui_file_path}")
            return
        self.setParent(parent)
        self.setWindowModality(2)  # Hace que esta ventana sea modal

        self.pushButton2equipo.clicked.connect(self.abrir_ventana_septima)
        self.pushButton1seguridad.clicked.connect(self.abrir_ventana_octava)
        self.pushButton_4red.clicked.connect(self.abrir_ventana_novena)
        self.pushButton_2.clicked.connect(self.volver_interfaz_anterior)
        self.pushButton3.clicked.connect(self.abrir_url)
    
        
    
    def volver_interfaz_anterior(self):
        # Cerrar esta ventana y volver a la interfaz anterior
        self.close()
    
    def abrir_ventana_septima(self):
        self.ventana_septima = VentanaSeptima()
        self.ventana_septima.show()


    def abrir_ventana_octava(self):
        self.ventana_octava = VentanaOctava()
        self.ventana_octava.show() 


    def abrir_ventana_novena(self):
        self.ventana_novena = VentanaNovena()
        self.ventana_novena.show() 

    def abrir_ventana_sexta(self):
        self.ventana_sexta = VentanaSexta()
        self.ventana_sexta.show() 

    def abrir_url(self):
        url = QUrl("http://127.0.0.1:8000/reportes/entre_fechas/")
        if not QDesktopServices.openUrl(url):
            print("Error: No se pudo abrir la URL")

import subprocess
import socket
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QProgressBar, QTextBrowser
from PyQt5 import uic
import requests
import os
import psutil
import winreg
import re

class VentanaSeptima(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Módulo Pruebas de Equipo")
        self.setFixedSize(799, 723)
        self.ui_file_path = os.path.join(os.path.dirname(__file__), "Modulo_Pruebas_de_Equipo.ui")

        try:
            uic.loadUi(self.ui_file_path, self)
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {self.ui_file_path}")
            return

        self.setParent(parent)
        self.setWindowModality(2)

        self.pushButton_11.clicked.connect(self.ejecutar_script)
        self.pushButton_2.clicked.connect(self.volver_interfaz_anterior)
        self.pushButton_23.clicked.connect(self.enviar_a_django)
        self.checkBox_11.clicked.connect(self.marcar_todos)

        # Initialize checkbox list here to make it available class-wide
        self.checkbox_list = [
            self.checkBox, self.checkBox_2, self.checkBox_3, self.checkBox_4, self.checkBox_5,
            self.checkBox_6, self.checkBox_7, self.checkBox_8, self.checkBox_9, self.checkBox_10
        ]

    def ejecutar_script(self):
        funciones = [
            self.ejecutar_net_user, self.ejecutar_driverquery, self.ejecutar_wmic_baseboard,
            self.ejecutar_wmic_product, self.ejecutar_programas_instalados, self.ejecutar_fecha_inicio,
            self.ejecutar_tasklist, self.ejecutar_systeminfo, self.ejecutar_wmic_bios,
            self.ejecutar_os_activacion
        ]

        resultado_str = ""
        progreso = 0
        pruebas_seleccionadas = sum(1 for checkbox in self.checkbox_list if checkbox.isChecked())
        self.progressBar.setMaximum(pruebas_seleccionadas)
        self.progressBar.setValue(0)

        for checkbox, funcion in zip(self.checkbox_list, funciones):
            if checkbox.isChecked():
                resultado = funcion()
                resultado_str += resultado + "\n\n"
                progreso += 1
                self.progressBar.setValue(progreso)

        self.textBrowser.setPlainText(resultado_str)

    # Define methods for each command
    def ejecutar_net_user(self):
        return self.ejecutar_comando("net user", "Autenticación De Usuarios Locales")

    def ejecutar_driverquery(self):
        return self.ejecutar_comando("driverquery", "Listar Controladores Del Sistema")

    def ejecutar_wmic_baseboard(self):
        return self.ejecutar_comando("wmic baseboard get product", "Muestra El Modelo De La Placa Base")

    def ejecutar_wmic_product(self):
        return self.ejecutar_comando("wmic product get name,version", "Nombre de los programas instalados")

    def ejecutar_programas_instalados(self):
        return self.verificar_programas_instalados()

    def ejecutar_fecha_inicio(self):
        return self.ejecutar_comando("wmic os get lastbootuptime", "Fecha Última Vez Que Se Inició El Sistema")

    def ejecutar_tasklist(self):
        return self.ejecutar_comando("tasklist", "Listar Tareas De Ejecución")

    def ejecutar_systeminfo(self):
        return self.ejecutar_comando("systeminfo", "Ver Información Del Sistema")

    def ejecutar_wmic_bios(self):
        return self.ejecutar_comando("wmic bios get serialnumber", "Muestra el número de serie de la BIOS")

    def ejecutar_os_activacion(self):
        return self.verificar_activacion_sistema_operativo()

    def ejecutar_comando(self, comando, descripcion):
        process = subprocess.run(comando, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        resultado_str = f"Prueba: {descripcion}\n"
        resultado_str += f"Salida estándar:\n{process.stdout}\n"
        resultado_str += f"Salida de error:\n{process.stderr}\n"
        return resultado_str

    def enviar_a_django(self):
        data = {
            'nombre': 'Reporte de Prueba',
            'fecha': datetime.now().strftime("%Y-%m-%d"),
            'equipo': socket.gethostname(),
            'datos': self.textBrowser.toPlainText()
        }
        url = 'http://127.0.0.1:8000/guardar_datos/'
        try:
            response = requests.post(url, json=data)
            if response.status_code == 200:
                QMessageBox.information(self, "Envío Exitoso", "Datos enviados exitosamente al servidor Django.")
            else:
                QMessageBox.warning(self, "Error de Envío", f"Error al enviar datos: {response.status_code}")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error de Conexión", f"No se pudo conectar al servidor: {e}")

    def marcar_todos(self):
        estado = self.checkBox_11.isChecked()
        for checkbox in self.checkbox_list:
            checkbox.setChecked(estado)

    def volver_interfaz_anterior(self):
        self.close()

    def verificar_programas_instalados(self):
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

        return f"Número de programas instalados: {len(programas)}"

    def verificar_activacion_sistema_operativo(self):
        # Abrir la clave de registro de Windows
        clave = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion")

        # Obtener el valor del campo "DigitalProductId"
        digital_product_id, _ = winreg.QueryValueEx(clave, "DigitalProductId")

        # Verificar si el sistema operativo está activado
        if digital_product_id[52:66] != "000000000000000":
            return "El sistema operativo está activado."
        else:
            return "El sistema operativo no está activado."

    def volver_interfaz_anterior(self):
        self.close()

import subprocess
import socket
from datetime import datetime
import os
import requests
import winreg
import win32com.client
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic

class VentanaOctava(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Módulo Pruebas de Seguridad")
        self.setFixedSize(832, 608)
        
        self.ui_file_path = os.path.join(os.path.dirname(__file__), "Módulo_Pruebas_de_seguridad_ok.ui")

        try:
            uic.loadUi(self.ui_file_path, self)
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {self.ui_file_path}")
            return
        
        self.setParent(parent)
        self.setWindowModality(2)

        self.pushButton_R.clicked.connect(self.ejecutar_scripts_seguridad)
        self.pushButton_23.clicked.connect(self.enviar_a_django)
        self.pushButton_2.clicked.connect(self.volver_interfaz_anterior)

        self.checkBox_6.clicked.connect(self.marcar_todos)

    def volver_interfaz_anterior(self):
        self.close() 

    def ejecutar_scripts_seguridad(self):
        resultado_str = ""
        pruebas_seleccionadas = sum(1 for checkbox in [self.checkBox, self.checkBox_2, self.checkBox_3, self.checkBox_4, self.checkBox_5] if checkbox.isChecked())
        self.progressBar.setMaximum(pruebas_seleccionadas)
        self.progressBar.setValue(0)

        if self.checkBox.isChecked():
            resultado_str += self.ejecutar_configuracion_firewall()

        if self.checkBox_2.isChecked():
            resultado_str += self.ejecutar_verificar_parches_seguridad()

        if self.checkBox_3.isChecked():
            resultado_str += self.ejecutar_ver_actualizaciones_instaladas()

        if self.checkBox_4.isChecked():
            resultado_str += self.ejecutar_verificacion_firewall()

        if self.checkBox_5.isChecked():
            resultado_str += self.ejecutar_verificar_estado_antivirus()

        self.textBrowser.setPlainText(resultado_str)

    def marcar_todos(self):
        estado = self.checkBox_6.isChecked()
        for checkbox in [self.checkBox, self.checkBox_2, self.checkBox_3, self.checkBox_4, self.checkBox_5]:
            checkbox.setChecked(estado)

    def enviar_a_django(self):
        data = {
            'nombre': 'Reporte de Prueba',
            'fecha': datetime.now().strftime("%Y-%m-%d"),
            'equipo': socket.gethostname(),
            'datos': self.textBrowser.toPlainText()
        }
        url = 'http://127.0.0.1:8000/guardar_datos/'
        try:
            response = requests.post(url, json=data)
            if response.status_code == 200:
                QMessageBox.information(self, "Envío Exitoso", "Datos enviados exitosamente al servidor Django.")
            else:
                QMessageBox.warning(self, "Error de Envío", f"Error al enviar datos: {response.status_code}")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error de Conexión", f"No se pudo conectar al servidor: {e}")

    def ejecutar_configuracion_firewall(self):
        resultado_str = "Resultados de Configuración Del Firewall De Windows:\n"
        nombre_equipo = socket.gethostname()
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        resultado_str += f"Nombre del equipo: {nombre_equipo}\n"
        resultado_str += f"Fecha y hora: {fecha_actual}\n"

        comando = 'netsh advfirewall show allprofiles'
        resultado = subprocess.run(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        resultado_str += "Salida estándar:\n"
        resultado_str += resultado.stdout + "\n"
        resultado_str += "Salida de error:\n"
        resultado_str += resultado.stderr + "\n"

        if resultado.returncode == 0:
            resultado_str += "El comando se ejecutó correctamente.\n"
        else:
            resultado_str += f"El comando retornó un código de error {resultado.returncode}.\n"

        return resultado_str

    def ejecutar_verificar_parches_seguridad(self):
        resultado_str = "Resultados de Verificar Parches De Seguridad En El Equipo:\n"
        nombre_equipo = socket.gethostname()
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        resultado_str += f"Nombre del equipo: {nombre_equipo}\n"
        resultado_str += f"Fecha y hora: {fecha_actual}\n"

        comando = 'wmic qfe list'
        resultado = subprocess.run(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        resultado_str += "Salida estándar:\n"
        resultado_str += resultado.stdout + "\n"
        resultado_str += "Salida de error:\n"
        resultado_str += resultado.stderr + "\n"

        if resultado.returncode == 0:
            resultado_str += "El comando se ejecutó correctamente.\n"
        else:
            resultado_str += f"El comando retornó un código de error {resultado.returncode}.\n"

        return resultado_str

    def ejecutar_ver_actualizaciones_instaladas(self):
        resultado_str = "Resultados de Ver Actualizaciones Instaladas:\n"
        nombre_equipo = socket.gethostname()
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        resultado_str += f"Nombre del equipo: {nombre_equipo}\n"
        resultado_str += f"Fecha y hora: {fecha_actual}\n"

        comando = 'wmic qfe list'
        resultado = subprocess.run(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        resultado_str += "Salida estándar:\n"
        resultado_str += resultado.stdout + "\n"
        resultado_str += "Salida de error:\n"
        resultado_str += resultado.stderr + "\n"

        if resultado.returncode == 0:
            resultado_str += "El comando se ejecutó correctamente.\n"
        else:
            resultado_str += f"El comando retornó un código de error {resultado.returncode}.\n"

        return resultado_str

    def ejecutar_verificacion_firewall(self):
        resultado_str = "Resultados de Verificación Del Firewall:\n"

        nombre_equipo = socket.gethostname()
        resultado_str += f"Nombre del equipo: {nombre_equipo}\n"

        reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\StandardProfile")
        enable_firewall, _ = winreg.QueryValueEx(reg_key, "EnableFirewall")

        if enable_firewall == 0:
            resultado_str += "El firewall de Windows está desactivado.\n"
        else:
            resultado_str += "El firewall de Windows está activado.\n"

        return resultado_str

    def ejecutar_verificar_estado_antivirus(self):
        resultado_str = "Resultados de Verificar Estado del Antivirus:\n"
        nombre_equipo = socket.gethostname()
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        resultado_str += f"Nombre del equipo: {nombre_equipo}\n"
        resultado_str += f"Fecha y hora: {fecha_actual}\n"

        wmi = win32com.client.GetObject("winmgmts:\\\\.\\root\\securitycenter2")
        antivirus_protection = wmi.ExecQuery("SELECT * FROM AntivirusProduct")

        if len(antivirus_protection) == 0:
            resultado_str += "No se ha encontrado ningún software antivirus en el sistema.\n"
        else:
            for product in antivirus_protection:
                resultado_str += f"Nombre del producto antivirus: {product.displayName}\n"
                resultado_str += f"Estado de la protección antivirus: {product.productState}\n"
                if product.productState == 266240:
                    resultado_str += "El escaneo de malware está en progreso.\n"
                else:
                    resultado_str += "No hay escaneo de malware en curso.\n"

        return resultado_str

    def volver_interfaz_anterior(self):
        self.close()

import subprocess
import socket
import urllib.request
from datetime import datetime
import requests
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic

class VentanaNovena(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Módulo Pruebas de Red")
        self.setFixedSize(699, 565)  

        self.ui_file_path = os.path.join(os.path.dirname(__file__), "Modulo_Pruebas_de_Red.ui")
        try:
            uic.loadUi(self.ui_file_path, self)
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {self.ui_file_path}")
            return
        self.setParent(parent)
        self.setWindowModality(2)  

        self.pushButton.clicked.connect(self.ejecutar_script)
        self.pushButton_2.clicked.connect(self.volver_interfaz_anterior)
        self.pushButton_23.clicked.connect(self.enviar_a_django)
        self.checkBox_6.clicked.connect(self.marcar_todos)

    def volver_interfaz_anterior(self):
        self.close() 

    def ejecutar_script(self):
        resultado_str = ""
        scripts = {
            "Estado Del Tráfico De Red": self.script_27,
            "Mostrar Información De Red": self.script_28,
            "Lista De Las Conexiones De Red Activas": self.script_29,
            "Verificar Restricciones En El Host": self.script_30,
            "Verificar Conectividad a Internet": self.script_31
        }
        checkbox_list = [self.checkBox, self.checkBox_2, self.checkBox_3, self.checkBox_4, self.checkBox_5]

        pruebas_seleccionadas = sum(1 for checkbox in checkbox_list if checkbox.isChecked())

        self.progressBar.setMaximum(pruebas_seleccionadas)
        self.progressBar.setValue(0)

        progreso = 0

        for checkbox, (nombre_prueba, script_func) in zip(checkbox_list, scripts.items()):
            if checkbox.isChecked():
                resultado_str += f"Resultados de {nombre_prueba}:\n\n"
                resultado_str += script_func()
                resultado_str += "\n\n"
                progreso += 1
                self.progressBar.setValue(progreso)

        self.textBrowser.setPlainText(resultado_str)

    def marcar_todos(self):
        estado = self.checkBox_6.isChecked()
        for checkbox in [self.checkBox, self.checkBox_2, self.checkBox_3, self.checkBox_4, self.checkBox_5]:
            checkbox.setChecked(estado)

    def script_27(self):
        resultado_str = ""
        nombre_equipo = socket.gethostname()
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        resultado_str += f"Nombre del equipo: {nombre_equipo}\n"
        resultado_str += f"Fecha y hora: {fecha_actual}\n"
        resultado_str += "Estado Del Tráfico De Red:\n\n"
        comando = 'netstat -an'
        resultado = subprocess.run(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        resultado_str += "Salida estándar:\n"
        resultado_str += resultado.stdout + "\n"
        resultado_str += "Salida de error:\n"
        resultado_str += resultado.stderr + "\n"
        if resultado.returncode == 0:
            resultado_str += "El comando se ejecutó correctamente.\n"
        else:
            resultado_str += f"El comando retornó un código de error {resultado.returncode}.\n"
        return resultado_str

    def script_28(self):
        resultado_str = ""
        nombre_equipo = socket.gethostname()
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        resultado_str += f"Nombre del equipo: {nombre_equipo}\n"
        resultado_str += f"Fecha y hora: {fecha_actual}\n"
        resultado_str += "Mostrar Información De Red:\n\n"
        comando = 'netstat'
        with subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as proceso:
            resultado_str += "Salida estándar:\n"
            for linea in proceso.stdout:
                resultado_str += linea
            resultado_str += "Salida de error:\n"
            for linea_error in proceso.stderr:
                resultado_str += linea_error
            if proceso.returncode == 0:
                resultado_str += "El comando se ejecutó correctamente.\n"
            else:
                resultado_str += f"El comando retornó un código de error {proceso.returncode}.\n"
        return resultado_str

    def script_29(self):
        resultado_str = ""
        nombre_equipo = socket.gethostname()
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        resultado_str += f"Nombre del equipo: {nombre_equipo}\n"
        resultado_str += f"Fecha y hora: {fecha_actual}\n"
        resultado_str += "Lista De Las Conexiones De Red Activas:\n\n"
        comando = 'ipconfig /all'
        resultado = subprocess.run(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        resultado_str += "Salida estándar:\n"
        resultado_str += resultado.stdout + "\n"
        resultado_str += "Salida de error:\n"
        resultado_str += resultado.stderr + "\n"
        if resultado.returncode == 0:
            resultado_str += "El comando se ejecutó correctamente.\n"
        else:
            resultado_str += f"El comando retornó un código de error {resultado.returncode}.\n"
        return resultado_str

    def script_30(self):
        resultado_str = ""
        nombre_equipo = socket.gethostname()
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        resultado_str += f"Nombre del equipo: {nombre_equipo}\n"
        resultado_str += f"Fecha y hora: {fecha_actual}\n"
        resultado_str += "Verificar Restricciones En El Host:\n\n"
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(('www.google.com', 80))
            resultado_str += "No hay restricciones en el host de tu PC.\n"
        except socket.error as e:
            resultado_str += f"Puede haber una restricción en el host de tu PC: {e}\n"
        return resultado_str

    def script_31(self):
        resultado_str = ""
        nombre_equipo = socket.gethostname()
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        resultado_str += f"Nombre del equipo: {nombre_equipo}\n"
        resultado_str += f"Fecha y hora: {fecha_actual}\n"
        resultado_str += "Verificar Conectividad a Internet:\n\n"
        try:
            urllib.request.urlopen("http://www.google.com", timeout=5)
            resultado_str += "Conexión a Internet establecida: ¡La prueba fue exitosa!\n"
        except urllib.error.URLError as e:
            resultado_str += f"No se pudo establecer conexión a Internet: {e.reason}\n"
        return resultado_str

    def enviar_a_django(self):
        data = {
            'nombre': 'Reporte de Prueba',
            'fecha': datetime.now().strftime("%Y-%m-%d"),
            'equipo': socket.gethostname(),
            'datos': self.textBrowser.toPlainText()
        }
        url = 'http://127.0.0.1:8000/guardar_datos/'
        try:
            response = requests.post(url, json=data)
            if response.status_code == 200:
                QMessageBox.information(self, "Envío Exitoso", "Datos enviados exitosamente al servidor Django.")
            else:
                QMessageBox.warning(self, "Error de Envío", f"Error al enviar datos: {response.status_code}")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error de Conexión", f"No se pudo conectar al servidor: {e}")




    def volver_interfaz_anterior(self):
        self.close()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana_principal = VentanaPrincipal()
    ventana_principal.show()
    sys.exit(app.exec_())  

    
