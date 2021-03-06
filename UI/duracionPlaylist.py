# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'duracionPlaylist.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem
import psycopg2
from config import config
from Reportes import *
import csv

class Ui_duracionPlaylist(object):
    def conectar(self):
        """ Conexión al servidor de pases de datos PostgreSQL """
        conexion = None
        try:
            # Lectura de los parámetros de conexion
            params = config()
            # Conexion al servidor de PostgreSQL
            conexion = psycopg2.connect(**params)
            # creación del cursor
            cur = conexion.cursor()
            # Ejecución la consulta para obtener la conexión
            cur.execute('SELECT version()')
            # Se obtienen los resultados
            db_version = cur.fetchone()
            # Ejecutamos una consulta
            cur.execute( "SELECT DISTINCT playlist.name, SUM(track.milliseconds) FROM playlisttrack JOIN track ON track.trackid=playlisttrack.trackid JOIN playlist ON playlist.playlistid=playlisttrack.playlistid GROUP BY playlist.playlistid ORDER BY SUM(track.milliseconds) DESC" )
            #Insertamos los datos devueltos por la consulta en la tabla
            row = 0
            
            #print (cur.fetchall())
            for a,b in cur.fetchall():
                self.tableWidget.setRowCount(row + 1)
                self.tableWidget.setItem(row, 0, QTableWidgetItem(a))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(str(b)))
                #csv_writer.writerow([a, str(b)])
                row += 1

            # Cerremos el cursor
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conexion is not None:
                conexion.close()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(560, 449)
        Form.setStyleSheet("background-color: rgb(85, 85, 255);")
        Form.setWindowIcon(QIcon('icono.png'))
        self.volverButton = QtWidgets.QPushButton(Form)
        self.volverButton.setGeometry(QtCore.QRect(20, 410, 75, 23))
        self.volverButton.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(72, 72, 72);")
        self.volverButton.setObjectName("volverButton")
        self.titutloLabel = QtWidgets.QLabel(Form)
        self.titutloLabel.setGeometry(QtCore.QRect(20, 10, 521, 41))
        self.titutloLabel.setStyleSheet("color: rgb(236, 236, 236);")
        self.titutloLabel.setObjectName("titutloLabel")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(20, 60, 521, 331))
        self.tableWidget.setStyleSheet("background-color: rgb(234, 234, 234);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        nombreColumnas = ("Playlist","Duracion (ms)")
        # Establecer las etiquetas de encabezado horizontal usando etiquetas
        self.tableWidget.setHorizontalHeaderLabels(nombreColumnas)
        self.tableWidget.setColumnWidth(0, 240)
        self.tableWidget.setColumnWidth(1, 240)
        #boton de generar reporte
        self.reporteButton = QtWidgets.QPushButton(Form)
        self.reporteButton.setGeometry(QtCore.QRect(400, 410, 75, 23))
        self.reporteButton.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(72, 72, 72);")
        self.reporteButton.setObjectName("reporteButton")
        self.reporteButton.clicked.connect(self.generarCsv)
        self.conectar()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def openReportes(self, Form):
        #self.window = QtWidgets.QWidget()
        #self.ui = Ui_Reportes()
        #self.ui.setupUi(self.window)
        Form.hide()
        #self.window.show()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.volverButton.setText(_translate("Form", "Volver"))
        self.reporteButton.setText(_translate("Form", "CSV"))
        self.titutloLabel.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Duración de playlist</span></p></body></html>"))
        self.volverButton.clicked.connect(lambda:self.openReportes(Form))

    def generarCsv(self):
        conexion = None
        try:
            # Lectura de los parámetros de conexion
            params = config()
            # Conexion al servidor de PostgreSQL
            conexion = psycopg2.connect(**params)
            # creación del cursor
            cur = conexion.cursor()
            # Ejecución la consulta para obtener la conexión
            cur.execute('SELECT version()')
            # Se obtienen los resultados
            db_version = cur.fetchone()
            ##escritura a .csv
            with open('duracionPlaylistConsult.csv', mode='w', newline='') as cvs_file:
                csv_writer = csv.writer(cvs_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                csv_writer.writerow(['Playlist', 'Duracion (ms)'])
                cur.execute( "SELECT DISTINCT playlist.name, SUM(track.milliseconds) FROM playlisttrack JOIN track ON track.trackid=playlisttrack.trackid JOIN playlist ON playlist.playlistid=playlisttrack.playlistid GROUP BY playlist.playlistid ORDER BY SUM(track.milliseconds) DESC" )
                row = 0
                #print (cur.fetchall())
                for a,b in cur.fetchall():
                    csv_writer.writerow([a, str(b)])
                    row += 1
            # Cerremos el cursor
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conexion is not None:
                conexion.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_duracionPlaylist()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
