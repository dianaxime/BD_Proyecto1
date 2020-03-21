# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logIn.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QMessageBox
from Actions import Ui_bienvenidaLabel
#from SignIn import Ui_LogIn
from SignIn import *
import psycopg2
from config import config


class Ui_SignInWidget(object):
    def setupUi(self, SignInWidget):
        SignInWidget.setObjectName("SignInWidget")
        SignInWidget.resize(322, 341)
        SignInWidget.setStyleSheet("background-color: rgb(85, 85, 255);\n"
"color: rgb(236, 236, 236);")
        SignInWidget.setWindowIcon(QIcon('icono.png'))
        self.userLabel = QtWidgets.QLabel(SignInWidget)
        self.userLabel.setGeometry(QtCore.QRect(30, 60, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.userLabel.setFont(font)
        self.userLabel.setObjectName("userLabel")
        self.passwordLabel = QtWidgets.QLabel(SignInWidget)
        self.passwordLabel.setGeometry(QtCore.QRect(30, 110, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.passwordLabel.setFont(font)
        self.passwordLabel.setObjectName("passwordLabel")
        self.userInput = QtWidgets.QLineEdit(SignInWidget)
        self.userInput.setGeometry(QtCore.QRect(130, 60, 151, 21))
        self.userInput.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(72, 72, 72);")
        self.userInput.setObjectName("userInput")
        self.passwordInput = QtWidgets.QLineEdit(SignInWidget)
        self.passwordInput.setEchoMode(QLineEdit.Password)
        self.passwordInput.setGeometry(QtCore.QRect(130, 110, 151, 20))
        self.passwordInput.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(72, 72, 72);")
        self.passwordInput.setObjectName("passwordInput")
        self.signIn = QtWidgets.QPushButton(SignInWidget)
        self.signIn.setGeometry(QtCore.QRect(90, 250, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.signIn.setFont(font)
        self.signIn.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(72, 72, 72);")
        self.signIn.setObjectName("signIn")
        self.signIn.clicked.connect(self.openSignIn)
        self.logIn = QtWidgets.QPushButton(SignInWidget)
        self.logIn.setGeometry(QtCore.QRect(90, 180, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.logIn.setFont(font)
        self.logIn.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(72, 72, 72);")
        self.logIn.setObjectName("logIn")
        #aqui en vez de openActions seria validate para validar la data ingresada
        self.logIn.clicked.connect(self.openActions)
        self.retranslateUi(SignInWidget)
        QtCore.QMetaObject.connectSlotsByName(SignInWidget)

    def retranslateUi(self, SignInWidget):
        _translate = QtCore.QCoreApplication.translate
        SignInWidget.setWindowTitle(_translate("SignInWidget", "Form"))
        self.userLabel.setText(_translate("SignInWidget", "Correo:"))
        self.passwordLabel.setText(_translate("SignInWidget", "Contraseña:"))
        self.signIn.setText(_translate("SignInWidget", "Sign In"))
        self.logIn.setText(_translate("SignInWidget", "Log In"))

    def openActions(self):
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
                cur.execute("SELECT contraseña FROM permisos_usuario JOIN customer ON customer.customerid=permisos_usuario.customerid  WHERE customer.email=%s",(user,))
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
                        self.window = QtWidgets.QWidget()
                        self.ui = Ui_bienvenidaLabel()
                        self.ui.setupUi(self.window)
                        SignInWidget.hide()
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


    def openSignIn(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_LogIn()
        self.ui.setupUi(self.window)
        SignInWidget.hide()
        self.window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SignInWidget = QtWidgets.QWidget()
    ui = Ui_SignInWidget()
    ui.setupUi(SignInWidget)
    SignInWidget.show()
    SignInWidget.setWindowTitle("Log In")
    sys.exit(app.exec_())
