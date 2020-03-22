# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inicio.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
#import admin_rc
#import logo_rc
#import user_rc
from adminLogIn import *
from logIn import *

class Ui_Inicio(object):
    def setupUi(self, Inicio):
        Inicio.setObjectName("Inicio")
        Inicio.resize(382, 301)
        Inicio.setStyleSheet("background-color: rgb(85, 85, 255);\n"
"color: rgb(236, 236, 236);")
        Inicio.setWindowIcon(QIcon('icono.png'))
        self.usuariosButton = QtWidgets.QPushButton(Inicio)
        self.usuariosButton.setGeometry(QtCore.QRect(60, 160, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.usuariosButton.setFont(font)
        self.usuariosButton.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"image: url(usuario.png);\n"
"color: rgb(72, 72, 72);")
        self.usuariosButton.setText("")
        self.usuariosButton.setObjectName("usuariosButton")
        self.label = QtWidgets.QLabel(Inicio)
        self.label.setGeometry(QtCore.QRect(20, 0, 341, 281))
        self.label.setAutoFillBackground(False)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.adminButton = QtWidgets.QPushButton(Inicio)
        self.adminButton.setGeometry(QtCore.QRect(220, 160, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.adminButton.setFont(font)
        self.adminButton.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"image: url(admin.png);\n"
"color: rgb(72, 72, 72);")
        self.adminButton.setText("")
        self.adminButton.setObjectName("adminButton")
        self.label_2 = QtWidgets.QLabel(Inicio)
        self.label_2.setGeometry(QtCore.QRect(60, 253, 91, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Inicio)
        self.label_3.setGeometry(QtCore.QRect(210, 252, 111, 21))
        self.label_3.setObjectName("label_3")
        self.label.raise_()
        self.usuariosButton.raise_()
        self.adminButton.raise_()
        self.label_2.raise_()
        self.label_3.raise_()

        self.retranslateUi(Inicio)
        QtCore.QMetaObject.connectSlotsByName(Inicio)

    def goUsuario(self, Form):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_SignInWidget()
        self.ui.setupUi(self.window)
        Form.hide()
        self.window.show()

    def goAdmin(self, Form):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_adminLogIn()
        self.ui.setupUi(self.window)
        Form.hide()
        self.window.show()

    def retranslateUi(self, Inicio):
        _translate = QtCore.QCoreApplication.translate
        Inicio.setWindowTitle(_translate("Inicio", "Pystream"))
        self.label_2.setText(_translate("Inicio", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Usuarios</span></p></body></html>"))
        self.label_3.setText(_translate("Inicio", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Administradores</span></p></body></html>"))
        self.usuariosButton.clicked.connect(lambda:self.goUsuario(Inicio))
        self.adminButton.clicked.connect(lambda:self.goAdmin(Inicio))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Inicio = QtWidgets.QWidget()
    ui = Ui_Inicio()
    ui.setupUi(Inicio)
    Inicio.show()
    sys.exit(app.exec_())
