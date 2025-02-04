# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Módulo_Pruebas_de_seguridad_ok.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(832, 608)
        MainWindow.setStyleSheet("background-color: rgb(9, 154, 194);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(420, 170, 371, 361))
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"Arial\";")
        self.textBrowser.setObjectName("textBrowser")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 110, 441, 41))
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 10, 321, 101))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Imagenes/Pruebas Generales.jpg"))
        self.label.setObjectName("label")
        self.pushButton_23 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_23.setGeometry(QtCore.QRect(60, 500, 191, 51))
        self.pushButton_23.setStyleSheet("QPushButton {\n"
"    background-color: rgb(180, 87, 98);\n"
"    font: 12pt \"Arial\";\n"
"    color: rgb(255, 255, 255);\n"
"    border: 2px solid black;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(200, 107, 118); /* Color cuando el cursor está sobre el botón */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(150, 67, 78); /* Color cuando el botón está presionado */\n"
"}\n"
"")
        self.pushButton_23.setObjectName("pushButton_23")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(30, 210, 381, 51))
        self.checkBox.setStyleSheet("font: 12pt \"Arial\";")
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(30, 260, 381, 21))
        self.checkBox_2.setStyleSheet("font: 12pt \"Arial\";")
        self.checkBox_2.setObjectName("checkBox_2")
        self.pushButton_R = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_R.setGeometry(QtCore.QRect(60, 430, 191, 51))
        self.pushButton_R.setStyleSheet("QPushButton {\n"
"    background-color: rgb(203, 246, 255);\n"
"    font: 12pt \"Arial\";\n"
"    border: 2px solid black;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(180, 230, 255); /* Color cuando el cursor está sobre el botón */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(150, 220, 255); /* Color cuando el botón está presionado */\n"
"}\n"
"\n"
"\n"
"")
        self.pushButton_R.setObjectName("pushButton_R")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(30, 300, 281, 21))
        self.checkBox_3.setStyleSheet("font: 12pt \"Arial\";")
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(30, 340, 271, 17))
        self.checkBox_4.setStyleSheet("font: 12pt \"Arial\";")
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(30, 380, 251, 17))
        self.checkBox_5.setStyleSheet("font: 12pt \"Arial\";")
        self.checkBox_5.setObjectName("checkBox_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(710, 540, 75, 23))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color: rgb(192, 192, 192);\n"
"    font: 11pt \"Arial\";\n"
"    color: rgb(0, 0, 0); /* Color del texto negro por defecto */\n"
"    border: 2px solid black;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(212, 212, 212); /* Color cuando el cursor está sobre el botón */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(172, 172, 172); /* Color cuando el botón está presionado */\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.checkBox_6 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_6.setGeometry(QtCore.QRect(30, 190, 171, 17))
        self.checkBox_6.setStyleSheet("font: 12pt \"Arial\";\n"
"color: rgb(255, 255, 255); /* Blanco */\n"
"")
        self.checkBox_6.setObjectName("checkBox_6")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(420, 540, 281, 23))
        self.progressBar.setStyleSheet("font: 12pt \"Arial\";")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Módulo Pruebas de Seguridad"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; color:#ffffff;\">Pruebas de Seguridad </span></p></body></html>"))
        self.pushButton_23.setText(_translate("MainWindow", "Guardar Reporte "))
        self.checkBox.setText(_translate("MainWindow", "Muestra La Configuración Del Firewall De Windows "))
        self.checkBox_2.setText(_translate("MainWindow", "Verificar Parches De Seguridad En El Equipo "))
        self.pushButton_R.setText(_translate("MainWindow", "Ejecutar Prueba"))
        self.checkBox_3.setText(_translate("MainWindow", "Ver Actualizaciones Instaladas"))
        self.checkBox_4.setText(_translate("MainWindow", "Verificación Del  Firewall "))
        self.checkBox_5.setText(_translate("MainWindow", "Verificar Estado del Antivirus "))
        self.pushButton_2.setText(_translate("MainWindow", "Regresar"))
        self.checkBox_6.setText(_translate("MainWindow", "Seleccionar Todos"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
