# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nReproducionesArtista.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem
import psycopg2
from config import config

class Ui_ReprodArtist(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(471, 401)
        Form.setStyleSheet("background-color: rgb(85, 85, 255);")
        Form.setWindowIcon(QIcon('icono.png'))
        self.titleForm = QtWidgets.QLabel(Form)
        self.titleForm.setGeometry(QtCore.QRect(50, 10, 401, 31))
        self.titleForm.setStyleSheet("color: rgb(236, 236, 236);")
        self.titleForm.setObjectName("titleForm")
        self.inputArtista = QtWidgets.QLineEdit(Form)
        self.inputArtista.setGeometry(QtCore.QRect(110, 60, 191, 21))
        self.inputArtista.setStyleSheet("color: rgb(72, 72, 72);\n"
"background-color: rgb(243, 243, 243);")
        self.inputArtista.setObjectName("inputArtista")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(60, 60, 41, 16))
        self.label_2.setObjectName("label_2")
        self.buscarBoton = QtWidgets.QPushButton(Form)
        self.buscarBoton.setGeometry(QtCore.QRect(360, 60, 51, 23))
        self.buscarBoton.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(72, 72, 72);")
        self.buscarBoton.setObjectName("buscarBoton")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(30, 110, 411, 251))
        self.tableWidget.setStyleSheet("background-color: rgb(234, 234, 234);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnWidth(0, 80)
        self.tableWidget.setColumnWidth(1, 110)
        self.tableWidget.setColumnWidth(2, 104)
        self.tableWidget.setColumnWidth(3, 109)
        nombreColumnas = ("Track Id", "Artista", "Cancion", "Reproducciones")
                # Establecer las etiquetas de encabezado horizontal usando etiquetas
        self.tableWidget.setHorizontalHeaderLabels(nombreColumnas)
        self.buscarBoton.clicked.connect(self.generarDatos)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Reproducciones por artista"))
        self.titleForm.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Canciones más reproducidas por artista</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:9pt; color:#ffffff;\">Artista:</span></p></body></html>"))
        self.buscarBoton.setText(_translate("Form", "Ver"))

    def generarDatos(self):
        conexion=None
        try:
            params = config()
            #print(params)
            # Conexion al servidor de PostgreSQL
            #print('Conectando a la base de datos PostgreSQL...')
            conexion = psycopg2.connect(**params)

            # creación del cursor
            cur = conexion.cursor()

            # Ejecución la consulta para obtener la conexión
            print('La version de PostgreSQL es la:')
            cur.execute('SELECT version()')

            # Se obtienen los resultados
            db_version = cur.fetchone()
            artista=self.inputArtista.text()
           
            if artista != '' :
                cur.execute( """SELECT reproduccion.trackid, artist.name, track.name, COUNT(reproduccion.trackid)
from reproduccion 
join track on track.trackid = reproduccion.trackid 
join album on album.albumid = track.albumid 
join artist on artist.artistid = album.artistid 
where artist.name = %s
group by reproduccion.trackid, artist.name, track.name""",(artista,))
                query=cur.fetchall()#[0][0]
                if (len(query)!=0):
                    row = 0
                    for a,b,c,d in query:
                        self.tableWidget.setRowCount(row + 1)
                        self.tableWidget.setItem(row, 0, QTableWidgetItem(str(a)))
                        self.tableWidget.setItem(row, 1, QTableWidgetItem(str(b)))
                        self.tableWidget.setItem(row, 2, QTableWidgetItem(str(c)))
                        self.tableWidget.setItem(row, 3, QTableWidgetItem(str(d)))
                        row += 1
                    cur.close() 
                    print("no hay mas")
                else:                      
                    blank=QMessageBox()
                    blank.setIcon(QMessageBox.Information)
                    blank.setWindowTitle("ERROR")
                    blank.setText("No se registraron ventas durante esas fechas")
                    blank.exec()                           
            else:
                blank=QMessageBox()
                blank.setIcon(QMessageBox.Information)
                blank.setWindowTitle("INCOMPLETO")
                blank.setText("Por favor llene los campos")
                blank.exec()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conexion is not None:
                conexion.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_ReprodArtist()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
