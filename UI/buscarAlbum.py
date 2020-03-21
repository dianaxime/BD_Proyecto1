# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'buscarAlbum.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon



class Ui_BuscarAlbum(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(340, 214)
        Form.setStyleSheet("background-color: rgb(85, 85, 255);\n"
"color: rgb(236, 236, 236);")
        Form.setWindowIcon(QIcon('icono.png'))
        self.continuarButton = QtWidgets.QPushButton(Form)
        self.continuarButton.setGeometry(QtCore.QRect(100, 140, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.continuarButton.setFont(font)
        self.continuarButton.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(72, 72, 72);")
        self.continuarButton.setObjectName("continuarButton")
        self.buscarLabel = QtWidgets.QLabel(Form)
        self.buscarLabel.setGeometry(QtCore.QRect(40, 20, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.buscarLabel.setFont(font)
        self.buscarLabel.setObjectName("buscarLabel")
        self.nombreInput = QtWidgets.QLineEdit(Form)
        self.nombreInput.setGeometry(QtCore.QRect(130, 90, 161, 20))
        self.nombreInput.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(72, 72, 72);")
        self.nombreInput.setObjectName("nombreInput")
        self.nombreLabel = QtWidgets.QLabel(Form)
        self.nombreLabel.setGeometry(QtCore.QRect(40, 90, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nombreLabel.setFont(font)
        self.nombreLabel.setObjectName("nombreLabel")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.continuarButton.setText(_translate("Form", "Continuar"))
        self.buscarLabel.setText(_translate("Form", "Ingrese álbum a modificar:"))
        self.nombreLabel.setText(_translate("Form", "Nombre:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_BuscarAlbum()
    ui.setupUi(Form)
    Form.show()
    Form.setWindowTitle("Buscar Album")
    sys.exit(app.exec_())
