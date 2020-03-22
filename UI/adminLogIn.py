# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminLogIn.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLineEdit

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

        self.retranslateUi(adminLogIn)
        QtCore.QMetaObject.connectSlotsByName(adminLogIn)

    def retranslateUi(self, adminLogIn):
        _translate = QtCore.QCoreApplication.translate
        adminLogIn.setWindowTitle(_translate("adminLogIn", "Form"))
        self.userLabel.setText(_translate("adminLogIn", "Usuario:"))
        self.passwordLabel.setText(_translate("adminLogIn", "Contraseña:"))
        self.signIn.setText(_translate("adminLogIn", "Sign In"))
        self.logIn.setText(_translate("adminLogIn", "Log In"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    adminLogIn = QtWidgets.QWidget()
    ui = Ui_adminLogIn()
    ui.setupUi(adminLogIn)
    adminLogIn.show()
    sys.exit(app.exec_())
