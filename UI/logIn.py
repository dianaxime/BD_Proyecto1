# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logIn.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SignInWidget(object):
    def setupUi(self, SignInWidget):
        SignInWidget.setObjectName("SignInWidget")
        SignInWidget.resize(322, 341)
        SignInWidget.setStyleSheet("background-color: rgb(85, 85, 255);\n"
"color: rgb(236, 236, 236);")
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
        self.userInput.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.userInput.setObjectName("userInput")
        self.passwordInput = QtWidgets.QLineEdit(SignInWidget)
        self.passwordInput.setGeometry(QtCore.QRect(130, 110, 151, 20))
        self.passwordInput.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.passwordInput.setObjectName("passwordInput")
        self.signIn = QtWidgets.QPushButton(SignInWidget)
        self.signIn.setGeometry(QtCore.QRect(90, 180, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.signIn.setFont(font)
        self.signIn.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(72, 72, 72);")
        self.signIn.setObjectName("signIn")
        self.logIn = QtWidgets.QPushButton(SignInWidget)
        self.logIn.setGeometry(QtCore.QRect(90, 250, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.logIn.setFont(font)
        self.logIn.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(72, 72, 72);")
        self.logIn.setObjectName("logIn")

        self.retranslateUi(SignInWidget)
        QtCore.QMetaObject.connectSlotsByName(SignInWidget)

    def retranslateUi(self, SignInWidget):
        _translate = QtCore.QCoreApplication.translate
        SignInWidget.setWindowTitle(_translate("SignInWidget", "Form"))
        self.userLabel.setText(_translate("SignInWidget", "Usuario:"))
        self.passwordLabel.setText(_translate("SignInWidget", "Contraseña:"))
        self.signIn.setText(_translate("SignInWidget", "Sign In"))
        self.logIn.setText(_translate("SignInWidget", "Log In"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SignInWidget = QtWidgets.QWidget()
    ui = Ui_SignInWidget()
    ui.setupUi(SignInWidget)
    SignInWidget.show()
    sys.exit(app.exec_())
