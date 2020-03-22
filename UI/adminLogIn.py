# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminLogIn.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QMessageBox
import psycopg2
from config import config
from adminActions import *
from adminSignIn import *

class Ui_adminLogIn(object):
    def setupUi(self, adminLogIn):
        adminLogIn.setObjectName("adminLogIn")
        adminLogIn.resize(322, 276)
        adminLogIn.setStyleSheet("background-color: rgb(85, 85, 255);\n"
"color: rgb(236, 236, 236);")
        adminLogIn.setWindowIcon(QIcon('icono.png'))
        self.userLabel = QtWidgets.QLabel(adminLogIn)
        self.userLabel.setGeometry(QtCore.QRect(30, 60, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.userLabel.setFont(font)
        self.userLabel.setObjectName("userLabel")
        self.passwordLabel = QtWidgets.QLabel(adminLogIn)
        self.passwordLabel.setGeometry(QtCore.QRect(30, 110, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.passwordLabel.setFont(font)
        self.passwordLabel.setObjectName("passwordLabel")
        self.userInput = QtWidgets.QLineEdit(adminLogIn)
        self.userInput.setGeometry(QtCore.QRect(130, 60, 151, 21))
        self.userInput.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(72, 72, 72);")
        self.userInput.setObjectName("userInput")
        self.passwordInput = QtWidgets.QLineEdit(adminLogIn)
        self.passwordInput.setEchoMode(QLineEdit.Password)
        self.passwordInput.setGeometry(QtCore.QRect(130, 110, 151, 20))
        self.passwordInput.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(72, 72, 72);")
        self.passwordInput.setObjectName("passwordInput")
        self.signIn = QtWidgets.QPushButton(adminLogIn)
        self.signIn.setGeometry(QtCore.QRect(90, 210, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.signIn.setFont(font)
        self.signIn.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(72, 72, 72);")
        self.signIn.setObjectName("signIn")
        #self.signIn.clicked.connect(self.openSignIn)
        self.logIn = QtWidgets.QPushButton(adminLogIn)
        self.logIn.setGeometry(QtCore.QRect(90, 150, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.logIn.setFont(font)
        self.logIn.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(72, 72, 72);")
        self.logIn.setObjectName("logIn")
        #self.logIn.clicked.connect(self.openActions)
        self.retranslateUi(adminLogIn)
        QtCore.QMetaObject.connectSlotsByName(adminLogIn)

    def retranslateUi(self, adminLogIn):
        _translate = QtCore.QCoreApplication.translate
        adminLogIn.setWindowTitle(_translate("adminLogIn", "Log In"))
        self.userLabel.setText(_translate("adminLogIn", "Usuario:"))
        self.passwordLabel.setText(_translate("adminLogIn", "Contraseña:"))
        self.signIn.setText(_translate("adminLogIn", "Sign In"))
        self.logIn.setText(_translate("adminLogIn", "Log In"))
        self.logIn.clicked.connect(lambda:self.openActions(adminLogIn))
        self.signIn.clicked.connect(lambda:self.openSignIn(adminLogIn))

    def openActions(self, adminLogIn):
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
            user=self.userInput.text()
            password=self.passwordInput.text()

            if user != '' and password != '':
                cur.execute("SELECT contraseña FROM permisos_admin JOIN employee ON employee.employeeid=permisos_admin.employeeid  WHERE employee.email=%s",(user,))
                contrasenaUsuario=cur.fetchall()
                print(password)
                if (len(contrasenaUsuario)==0):
                    invalid=QMessageBox()
                    invalid.setIcon(QMessageBox.Information)
                    invalid.setWindowTitle("INVALIDO")
                    invalid.setText("Correo no registrado")
                    invalid.exec()
                else:
                    if contrasenaUsuario[0][0] == password:
                        #SignInWidget.hide()
                        self.window = QtWidgets.QWidget()
                        self.ui = Ui_adminActions()
                        self.ui.setupUi(self.window)
                        adminLogIn.hide()
                        self.window.show()
                    else: 
                        invalid=QMessageBox()
                        invalid.setIcon(QMessageBox.Information)
                        invalid.setWindowTitle("INVALIDO")
                        invalid.setText("Contraseña incorrectos")
                        invalid.exec()
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


    def openSignIn(self, adminLogIn):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_adminSignIn()
        self.ui.setupUi(self.window)
        #adminLogIn.hide()
        self.window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    adminLogIn = QtWidgets.QWidget()
    ui = Ui_adminLogIn()
    ui.setupUi(adminLogIn)
    adminLogIn.show()
    sys.exit(app.exec_())
