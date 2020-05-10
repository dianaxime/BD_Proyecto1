# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'buscarcancion.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import psycopg2
from config import config
from modificarCancion import *
from PyQt5.QtWidgets import QMessageBox

class Ui_BuscarCancion(object):
    def __init__(self,id):
        self.id=id
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(339, 221)
        Form.setStyleSheet("background-color: rgb(85, 85, 255);\n"
"color: rgb(236, 236, 236);")
        Form.setWindowIcon(QIcon('icono.png'))
        self.continuarButton = QtWidgets.QPushButton(Form)
        self.continuarButton.setGeometry(QtCore.QRect(100, 150, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.continuarButton.setFont(font)
        self.continuarButton.clicked.connect(self.buscarCancion)
        self.continuarButton.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(72, 72, 72);")
        self.continuarButton.setObjectName("continuarButton")
        self.buscarLabel = QtWidgets.QLabel(Form)
        self.buscarLabel.setGeometry(QtCore.QRect(40, 30, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.buscarLabel.setFont(font)
        self.buscarLabel.setObjectName("buscarLabel")
        self.nombreInput = QtWidgets.QLineEdit(Form)
        self.nombreInput.setGeometry(QtCore.QRect(130, 100, 161, 20))
        self.nombreInput.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(72, 72, 72);")
        self.nombreInput.setObjectName("nombreInput")
        self.nombreLabel = QtWidgets.QLabel(Form)
        self.nombreLabel.setGeometry(QtCore.QRect(40, 100, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nombreLabel.setFont(font)
        self.nombreLabel.setObjectName("nombreLabel")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Buscar cancion"))
        self.continuarButton.setText(_translate("Form", "Continuar"))
        self.buscarLabel.setText(_translate("Form", "Ingrese canción a modificar:"))
        self.nombreLabel.setText(_translate("Form", "Nombre:"))

    def buscarCancion(self):
        conexion=None
        try:
            params = config()

            #print(params)
            # Conexion al servidor de PostgreSQL
            #print('Conectando a la base de datos PostgreSQL...')
            conexion = psycopg2.connect(**params)

            # creación del cursor
            cur = conexion.cursor()
            nombre=self.nombreInput.text()
           
            if nombre != '' :
                cur.execute( "SELECT track.trackid FROM track WHERE track.name=%s",(nombre,))
                IDArtO=cur.fetchall()#[0][0]
                if (len(IDArtO)==0):
                    blank=QMessageBox()
                    blank.setIcon(QMessageBox.Information)
                    blank.setWindowTitle("ERROR")
                    blank.setText("El track que usted desea modificar no esta registrado")
                    blank.exec()
                else:
                    IDArtO=IDArtO[0][0]
                    print(IDArtO)
                    self.window = QtWidgets.QWidget()
                    #self.id=IDArtO
                    self.ui =Ui_ModificarCancion(self.id, IDArtO)
                    self.ui.setupUi(self.window)
                    #LogIn.hide()
                    self.window.show()
                
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
    ui = Ui_BuscarCancion()
    ui.setupUi(Form)
    Form.show()
    Form.setWindowTitle("Buscar Cancion")
    sys.exit(app.exec_())
