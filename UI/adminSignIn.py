# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminSignIn.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from adminLogIn import *
import psycopg2
from config import config

class Ui_adminSignIn(object):
    def setupUi(self, adminSignIn):
        adminSignIn.setObjectName("adminSignIn")
        adminSignIn.resize(261, 268)
        adminSignIn.setStyleSheet("background-color: rgb(85, 85, 255);\n"
"color: rgb(236, 236, 236);")
        adminSignIn.setWindowIcon(QIcon('icono.png'))
        self.nombreLabel = QtWidgets.QLabel(adminSignIn)
        self.nombreLabel.setGeometry(QtCore.QRect(20, 40, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.nombreLabel.setFont(font)
        self.nombreLabel.setObjectName("nombreLabel")
        self.apellidoLabel = QtWidgets.QLabel(adminSignIn)
        self.apellidoLabel.setGeometry(QtCore.QRect(20, 80, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.apellidoLabel.setFont(font)
        self.apellidoLabel.setObjectName("apellidoLabel")
        self.emailLabel = QtWidgets.QLabel(adminSignIn)
        self.emailLabel.setGeometry(QtCore.QRect(20, 120, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.emailLabel.setFont(font)
        self.emailLabel.setObjectName("emailLabel")
        self.passwordLabel = QtWidgets.QLabel(adminSignIn)
        self.passwordLabel.setGeometry(QtCore.QRect(20, 160, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.passwordLabel.setFont(font)
        self.passwordLabel.setObjectName("passwordLabel")
        self.nombreInput = QtWidgets.QLineEdit(adminSignIn)
        self.nombreInput.setGeometry(QtCore.QRect(110, 40, 113, 20))
        self.nombreInput.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(72, 72, 72);")
        self.nombreInput.setObjectName("nombreInput")
        self.apellidoInput = QtWidgets.QLineEdit(adminSignIn)
        self.apellidoInput.setGeometry(QtCore.QRect(110, 80, 113, 20))
        self.apellidoInput.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(72, 72, 72);")
        self.apellidoInput.setObjectName("apellidoInput")
        self.emailInput = QtWidgets.QLineEdit(adminSignIn)
        self.emailInput.setGeometry(QtCore.QRect(110, 120, 113, 20))
        self.emailInput.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(72, 72, 72);")
        self.emailInput.setObjectName("emailInput")
        self.passwordInput = QtWidgets.QLineEdit(adminSignIn)
        self.passwordInput.setGeometry(QtCore.QRect(110, 160, 113, 20))
        self.passwordInput.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(72, 72, 72);")
        self.passwordInput.setObjectName("passwordInput")
        self.sigInButton = QtWidgets.QPushButton(adminSignIn)
        self.sigInButton.setGeometry(QtCore.QRect(70, 200, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.sigInButton.setFont(font)
        self.sigInButton.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(72, 72, 72);")
        self.sigInButton.setObjectName("sigInButton")
        self.sigInButton.clicked.connect(self.validateInfo)
        self.retranslateUi(adminSignIn)
        QtCore.QMetaObject.connectSlotsByName(adminSignIn)

    def retranslateUi(self, adminSignIn):
        _translate = QtCore.QCoreApplication.translate
        adminSignIn.setWindowTitle(_translate("adminSignIn", "Sign In"))
        self.nombreLabel.setText(_translate("adminSignIn", "Nombre:"))
        self.apellidoLabel.setText(_translate("adminSignIn", "Apellido:"))
        self.emailLabel.setText(_translate("adminSignIn", "Email:"))
        self.passwordLabel.setText(_translate("adminSignIn", "Contraseña:"))
        self.sigInButton.setText(_translate("adminSignIn", "Sign In"))

    def validateInfo(self):
        #Aqui iria verificar el user y password en BD
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
            nombre=self.nombreInput.text()
            apellido=self.apellidoInput.text()
            email=self.emailInput.text()
            contrasena=self.passwordInput.text()
            """user=self.userInput.text()
            password=self.passwordInput.text()"""

            if (nombre != '' and apellido != '' and email != '' and contrasena != '') :
                cur.execute( "SELECT firstname FROM employee WHERE employee.email=%s",(email,) )
                correo_existente=cur.fetchall()
                if (len(correo_existente)!=0):
                    blank=QMessageBox()
                    blank.setIcon(QMessageBox.Information)
                    blank.setWindowTitle("ERROR")
                    blank.setText("Ese correo ya esta registrado como Administrador")
                    blank.exec()
                else:
                    cur.execute( "SELECT MAX(employee.employeeid) FROM employee" )
                    IDUsuario=cur.fetchall()
                    IDoficial=(IDUsuario[0][0])
                    IDoficial += 1
                    print(IDoficial)
                    cur.execute("INSERT INTO employee (employeeid, firstname, lastname, email)VALUES (%s, %s,%s, %s)", (IDoficial, nombre, apellido, email,))
                    
                    cur.execute("INSERT INTO permisos_admin (permisoid, contraseña, employeeid)VALUES (%s, %s,%s)", (IDoficial, contrasena, IDoficial,))
                    print("estoy aqui")
                    conexion.commit()
                    """self.window = QtWidgets.QWidget()
                    self.ui = Ui_SignInWidget()
                    self.ui.setupUi(self.window)
                    #LogIn.hide()
                    self.window.show()"""
                    #LogIn.hide()
                    self.window = QtWidgets.QWidget()
                    self.ui = Ui_adminLogIn()
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
    adminSignIn = QtWidgets.QWidget()
    ui = Ui_adminSignIn()
    ui.setupUi(adminSignIn)
    adminSignIn.show()
    sys.exit(app.exec_())
