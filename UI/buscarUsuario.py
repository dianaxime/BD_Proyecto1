# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'buscarUsuario.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from permisosUsuario import *
from PyQt5.QtWidgets import QMessageBox
import psycopg2
from config import config


class Ui_buscarUsuario(object):
    def conectar(self,Form):
        nombre=self.nombreInput.text()
        apellido=self.apellidoInput.text()
        """ Conexión al servidor de pases de datos PostgreSQL """
        conexion = None
        if nombre != '' and apellido != '':
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
                cur.execute("SELECT customer.customerid, customer.firstname, customer.lastname FROM customer WHERE customer.firstname = '{0}'".format(nombre))
                #Insertamos los datos devueltos por la consulta en la tabla
                data=cur.fetchall()
                if len(data)>0:
                    if data[0][1] == nombre and data[0][2] == apellido:
                        self.window = QtWidgets.QWidget()
                        self.message = data
                        self.ui = Ui_permisosUsuario(self.message)
                        self.ui.setupUi(self.window)
                        Form.hide()
                        self.window.show()
                    else:
                        blank=QMessageBox()
                        blank.setIcon(QMessageBox.Information)
                        blank.setWindowTitle("ERROR")
                        blank.setText("La informacion no coincide")
                        blank.exec()
                else:
                    blank=QMessageBox()
                    blank.setIcon(QMessageBox.Information)
                    blank.setWindowTitle("ERROR")
                    blank.setText("Por favor ingrese un usuario válido")
                    blank.exec()        
                # Cerremos el cursor
                cur.close()
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
            finally:
                if conexion is not None:
                    conexion.close()
        else:
            blank=QMessageBox()
            blank.setIcon(QMessageBox.Information)
            blank.setWindowTitle("ERROR")
            blank.setText("Llene los recuadros")
            blank.exec()
        

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(324, 251)
        Form.setStyleSheet("background-color: rgb(85, 85, 255);\n"
"color: rgb(236, 236, 236);")
        Form.setWindowIcon(QIcon('icono.png'))
        self.continuarButton = QtWidgets.QPushButton(Form)
        self.continuarButton.setGeometry(QtCore.QRect(100, 180, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.continuarButton.setFont(font)
        self.continuarButton.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(72, 72, 72);")
        self.continuarButton.setObjectName("continuarButton")
        self.buscarLabel = QtWidgets.QLabel(Form)
        self.buscarLabel.setGeometry(QtCore.QRect(40, 20, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.buscarLabel.setFont(font)
        self.buscarLabel.setObjectName("buscarLabel")
        self.nombreInput = QtWidgets.QLineEdit(Form)
        self.nombreInput.setGeometry(QtCore.QRect(130, 90, 161, 20))
        self.nombreInput.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(72, 72, 72);")
        self.nombreInput.setObjectName("nombreInput")
        self.nombreLabel = QtWidgets.QLabel(Form)
        self.nombreLabel.setGeometry(QtCore.QRect(40, 90, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nombreLabel.setFont(font)
        self.nombreLabel.setObjectName("nombreLabel")
        self.apellidoInput = QtWidgets.QLineEdit(Form)
        self.apellidoInput.setGeometry(QtCore.QRect(130, 134, 161, 20))
        self.apellidoInput.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(72, 72, 72);")
        self.apellidoInput.setObjectName("apellidoInput")
        self.apellidoLabel = QtWidgets.QLabel(Form)
        self.apellidoLabel.setGeometry(QtCore.QRect(40, 130, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.apellidoLabel.setFont(font)
        self.apellidoLabel.setObjectName("apellidoLabel")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Buscar usuario"))
        self.continuarButton.setText(_translate("Form", "Continuar"))
        self.buscarLabel.setText(_translate("Form", "Ingrese usuario a modificar:"))
        self.nombreLabel.setText(_translate("Form", "Nombre:"))
        self.apellidoLabel.setText(_translate("Form", "Apellido:"))
        self.continuarButton.clicked.connect(lambda:self.conectar(Form))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_buscarUsuario()
    ui.setupUi(Form)
    Form.show()
    Form.setWindowTitle("Buscar Usuario")
    sys.exit(app.exec_())
