# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminActions.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from buscarUsuario import *
from Reportes import *
import sys


class Ui_adminActions(object):
    def setupUi(self, adminActions):
        adminActions.setObjectName("adminActions")
        adminActions.resize(298, 291)
        adminActions.setStyleSheet("background-color: rgb(85, 85, 255);\n"
"color: rgb(236, 236, 236);")
        adminActions.setWindowIcon(QIcon('icono.png'))
        self.actionsAdmin = QtWidgets.QPushButton(adminActions)
        self.actionsAdmin.setGeometry(QtCore.QRect(40, 170, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.actionsAdmin.setFont(font)
        self.actionsAdmin.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(72, 72, 72);")
        self.actionsAdmin.setObjectName("actionsAdmin")
        self.modificar = QtWidgets.QPushButton(adminActions)
        self.modificar.setGeometry(QtCore.QRect(40, 110, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.modificar.setFont(font)
        self.modificar.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(72, 72, 72);")
        self.modificar.setObjectName("modificar")
        self.label = QtWidgets.QLabel(adminActions)
        self.label.setGeometry(QtCore.QRect(20, 30, 261, 41))
        self.label.setObjectName("label")

        self.salir = QtWidgets.QPushButton(adminActions)
        self.salir.setGeometry(QtCore.QRect(40, 230, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.salir.setFont(font)
        self.salir.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(72, 72, 72);")
        self.salir.setObjectName("salir")

        self.retranslateUi(adminActions)
        QtCore.QMetaObject.connectSlotsByName(adminActions)

    def goReportes(self, Form):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Reportes()
        self.ui.setupUi(self.window)
        #Form.hide()
        self.window.show()

    def goPermisos(self, Form):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_buscarUsuario()
        self.ui.setupUi(self.window)
        #Form.hide()
        self.window.show()

    def goOut(self, Form):
        #self.window = QtWidgets.QWidget()
        #self.ui = Ui_buscarUsuario()
        #self.ui.setupUi(self.window)
        #Form.hide()
        #self.window.show()
        sys.exit()

    def retranslateUi(self, adminActions):
        _translate = QtCore.QCoreApplication.translate
        adminActions.setWindowTitle(_translate("adminActions", "Acciones administrador"))
        self.actionsAdmin.setText(_translate("adminActions", "Reportes"))
        self.modificar.setText(_translate("adminActions", "Activar/Desactivar Usuarios"))
        self.salir.setText(_translate("adminActions", "Salir"))
        self.label.setText(_translate("adminActions", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">Bienvenido</span></p></body></html>"))
        self.actionsAdmin.clicked.connect(lambda:self.goReportes(adminActions))
        self.modificar.clicked.connect(lambda:self.goPermisos(adminActions))
        self.salir.clicked.connect(lambda:self.goOut(adminActions))


"""if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    adminActions = QtWidgets.QWidget()
    ui = Ui_adminActions()
    ui.setupUi(adminActions)
    adminActions.show()
    sys.exit(app.exec_())"""
