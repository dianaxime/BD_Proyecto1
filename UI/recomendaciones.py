# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'recomendaciones.ui'
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

class Ui_Recomendaciones(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(515, 514)
        Form.setStyleSheet("background-color: rgb(85, 85, 255);\n"
"color: rgb(236, 236, 236);")
        Form.setWindowIcon(QIcon('icono.png'))
        self.titulo = QtWidgets.QLabel(Form)
        self.titulo.setGeometry(QtCore.QRect(130, 20, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.titulo.setFont(font)
        self.titulo.setObjectName("titulo")
        self.fechaInput = QtWidgets.QLineEdit(Form)
        self.fechaInput.setGeometry(QtCore.QRect(90, 90, 151, 21))
        self.fechaInput.setStyleSheet("color: rgb(72, 72, 72);\n"
"background-color: rgb(243, 243, 243);")
        self.fechaInput.setObjectName("fechaInput")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.agregarButton = QtWidgets.QPushButton(Form)
        self.agregarButton.setGeometry(QtCore.QRect(280, 90, 75, 23))
        self.agregarButton.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(72, 72, 72);")
        self.agregarButton.setObjectName("agregarButton")
        self.agregarButton.clicked.connect(self.agregar)
        self.generarButton = QtWidgets.QPushButton(Form)
        self.generarButton.setGeometry(QtCore.QRect(380, 90, 75, 23))
        self.generarButton.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(72, 72, 72);")
        self.generarButton.setObjectName("generarButton")
        self.generarButton.clicked.connect(self.generar)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(40, 140, 421, 331))
        self.tableWidget.setStyleSheet("background-color: rgb(234, 234, 234);\n"
"color: rgb(72, 72, 72);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnWidth(0, 210)
        self.tableWidget.setColumnWidth(1, 208)
        nombreColumnas = ("Track","Genero")
        # Establecer las etiquetas de encabezado horizontal usando etiquetas
        self.tableWidget.setHorizontalHeaderLabels(nombreColumnas)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Recomendaciones"))
        self.titulo.setText(_translate("Form", "Recomendado para ti"))
        self.label_2.setText(_translate("Form", "Fecha:"))
        self.agregarButton.setText(_translate("Form", "Agregar"))
        self.generarButton.setText(_translate("Form", "Generar"))

    def agregar(self):
        self.tableWidget.setRowCount(0)
        fecha=self.fechaInput.text()
        conexion = None
        try:
            # Lectura de los parámetros de conexion
            params = config()

            #print(params)
            # Conexion al servidor de PostgreSQL
            print('Conectando a la base de datos PostgreSQL...')
            conexion = psycopg2.connect(**params)

            # creación del cursor
            cur = conexion.cursor()

            # Ejecución la consulta para obtener la conexión
            print('La version de PostgreSQL es la:')
            cur.execute('SELECT version()')

            # Se obtienen los resultados
            db_version = cur.fetchone()
            # Se muestra la versión por pantalla
            print(db_version)
    
            if fecha != '' :
                #CAMBIAR QUERY
                cur.execute( "SELECT track.name FROM track WHERE track.name=%s",(nombreTrack,))
                IDtrackO=cur.fetchall()#[0][0]
                if (len(IDtrackO)==0):
                    blank=QMessageBox()
                    blank.setIcon(QMessageBox.Information)
                    blank.setWindowTitle("ERROR")
                    blank.setText("El track no esta registrado")
                    blank.exec()
                else:
                    cur.execute("""
                            SELECT track.name, album.title, artist.name, track.unitprice
                            FROM track  
                                JOIN album ON album.albumid = track.albumid
                                JOIN artist ON artist.artistid = album.artistid
                            WHERE track.name = %s
                            """,(nombreTrack,))

                    row = 0
                    for a,b,c,d in cur.fetchall():
                        self.tableWidget.setRowCount(row + 1)
                        self.tableWidget.setItem(row, 0, QTableWidgetItem(a))
                        self.tableWidget.setItem(row, 1, QTableWidgetItem(b))
                        self.tableWidget.setItem(row, 2, QTableWidgetItem(c))
                        self.tableWidget.setItem(row, 3, QTableWidgetItem(str(d)))
                        row += 1
                    cur.close()                
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
                print('Conexión finalizada.')


    def generar(self):
        print("Hola")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Recomendaciones()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
