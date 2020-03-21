# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminActions.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon


class Ui_adminActions(object):
    def setupUi(self, adminActions):
        adminActions.setObjectName("adminActions")
        adminActions.resize(298, 241)
        adminActions.setStyleSheet("background-color: rgb(85, 85, 255);\n"
"color: rgb(236, 236, 236);")
        adminActions.setWindowIcon(QIcon('icono.png'))
        self.signIn = QtWidgets.QPushButton(adminActions)
        self.signIn.setGeometry(QtCore.QRect(40, 170, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.signIn.setFont(font)
        self.signIn.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(72, 72, 72);")
        self.signIn.setObjectName("signIn")
        self.logIn = QtWidgets.QPushButton(adminActions)
        self.logIn.setGeometry(QtCore.QRect(40, 110, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.logIn.setFont(font)
        self.logIn.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(72, 72, 72);")
        self.logIn.setObjectName("logIn")
        self.label = QtWidgets.QLabel(adminActions)
        self.label.setGeometry(QtCore.QRect(20, 30, 261, 41))
        self.label.setObjectName("label")

        self.retranslateUi(adminActions)
        QtCore.QMetaObject.connectSlotsByName(adminActions)

    def retranslateUi(self, adminActions):
        _translate = QtCore.QCoreApplication.translate
        adminActions.setWindowTitle(_translate("adminActions", "Form"))
        self.signIn.setText(_translate("adminActions", "Reportes"))
        self.logIn.setText(_translate("adminActions", "Activar/Desactivar Usuarios"))
        self.label.setText(_translate("adminActions", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">Bienvenido</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    adminActions = QtWidgets.QWidget()
    ui = Ui_adminActions()
    ui.setupUi(adminActions)
    adminActions.show()
    sys.exit(app.exec_())
