# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SignIn.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from logIn import *

class Ui_LogIn(object):
    def setupUi(self, LogIn):
        LogIn.setObjectName("LogIn")
        LogIn.resize(261, 353)
        LogIn.setStyleSheet("background-color: rgb(85, 85, 255);\n"
"color: rgb(236, 236, 236);")
        LogIn.setWindowIcon(QIcon('icono.png'))
        self.nombreLabel = QtWidgets.QLabel(LogIn)
        self.nombreLabel.setGeometry(QtCore.QRect(20, 40, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.nombreLabel.setFont(font)
        self.nombreLabel.setObjectName("nombreLabel")
        self.apellidoLabel = QtWidgets.QLabel(LogIn)
        self.apellidoLabel.setGeometry(QtCore.QRect(20, 80, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.apellidoLabel.setFont(font)
        self.apellidoLabel.setObjectName("apellidoLabel")
        self.paisLabel = QtWidgets.QLabel(LogIn)
        self.paisLabel.setGeometry(QtCore.QRect(20, 120, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.paisLabel.setFont(font)
        self.paisLabel.setObjectName("paisLabel")
        self.emailLabel = QtWidgets.QLabel(LogIn)
        self.emailLabel.setGeometry(QtCore.QRect(20, 160, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.emailLabel.setFont(font)
        self.emailLabel.setObjectName("emailLabel")
        self.userLabel = QtWidgets.QLabel(LogIn)
        self.userLabel.setGeometry(QtCore.QRect(20, 200, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.userLabel.setFont(font)
        self.userLabel.setObjectName("userLabel")
        self.passwordLabel = QtWidgets.QLabel(LogIn)
        self.passwordLabel.setGeometry(QtCore.QRect(20, 240, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.passwordLabel.setFont(font)
        self.passwordLabel.setObjectName("passwordLabel")
        self.nombreInput = QtWidgets.QLineEdit(LogIn)
        self.nombreInput.setGeometry(QtCore.QRect(110, 40, 113, 20))
        self.nombreInput.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(72, 72, 72);")
        self.nombreInput.setObjectName("nombreInput")
        self.apellidoInput = QtWidgets.QLineEdit(LogIn)
        self.apellidoInput.setGeometry(QtCore.QRect(110, 80, 113, 20))
        self.apellidoInput.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(72, 72, 72);")
        self.apellidoInput.setObjectName("apellidoInput")
        self.paisInput = QtWidgets.QLineEdit(LogIn)
        self.paisInput.setGeometry(QtCore.QRect(110, 120, 113, 20))
        self.paisInput.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(72, 72, 72);")
        self.paisInput.setObjectName("paisInput")
        self.emailInput = QtWidgets.QLineEdit(LogIn)
        self.emailInput.setGeometry(QtCore.QRect(110, 160, 113, 20))
        self.emailInput.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(72, 72, 72);")
        self.emailInput.setObjectName("emailInput")
        self.userInput = QtWidgets.QLineEdit(LogIn)
        self.userInput.setGeometry(QtCore.QRect(110, 200, 113, 20))
        self.userInput.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(72, 72, 72);")
        self.userInput.setObjectName("userInput")
        self.passwordInput = QtWidgets.QLineEdit(LogIn)
        self.passwordInput.setGeometry(QtCore.QRect(110, 240, 113, 20))
        self.passwordInput.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(72, 72, 72);")
        self.passwordInput.setObjectName("passwordInput")
        self.sigInButton = QtWidgets.QPushButton(LogIn)
        self.sigInButton.setGeometry(QtCore.QRect(70, 290, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.sigInButton.setFont(font)
        self.sigInButton.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(72, 72, 72);")
        self.sigInButton.setObjectName("sigInButton")

        self.retranslateUi(LogIn)
        QtCore.QMetaObject.connectSlotsByName(LogIn)

    def retranslateUi(self, LogIn):
        _translate = QtCore.QCoreApplication.translate
        LogIn.setWindowTitle(_translate("LogIn", "Form"))
        self.nombreLabel.setText(_translate("LogIn", "Nombre:"))
        self.apellidoLabel.setText(_translate("LogIn", "Apellido:"))
        self.paisLabel.setText(_translate("LogIn", "País:"))
        self.emailLabel.setText(_translate("LogIn", "Email:"))
        self.userLabel.setText(_translate("LogIn", "Usuario:"))
        self.passwordLabel.setText(_translate("LogIn", "Contraseña:"))
        self.sigInButton.setText(_translate("LogIn", "Sign In"))

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
                        self.ui = Ui_SignInWidget()
                        self.ui.setupUi(self.window)
                        LoginIn.hide()
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




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LogIn = QtWidgets.QWidget()
    ui = Ui_LogIn()
    ui.setupUi(LogIn)
    LogIn.show()
    LogIn.setWindowTitle("Sign In")
    sys.exit(app.exec_())
