# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ingresarAlbum.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(335, 252)
        Form.setStyleSheet("background-color: rgb(85, 85, 255);\n"
"color: rgb(236, 236, 236);")
        Form.setWindowIcon(QIcon('icono.png'))
        self.nombreLabel = QtWidgets.QLabel(Form)
        self.nombreLabel.setGeometry(QtCore.QRect(40, 90, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nombreLabel.setFont(font)
        self.nombreLabel.setObjectName("nombreLabel")
        self.tituloInput = QtWidgets.QLineEdit(Form)
        self.tituloInput.setGeometry(QtCore.QRect(130, 90, 161, 20))
        self.tituloInput.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(72, 72, 72);")
        self.tituloInput.setObjectName("tituloInput")
        self.ingresarAlbumLabel = QtWidgets.QLabel(Form)
        self.ingresarAlbumLabel.setGeometry(QtCore.QRect(90, 20, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.ingresarAlbumLabel.setFont(font)
        self.ingresarAlbumLabel.setObjectName("ingresarAlbumLabel")
        self.ingresarButton = QtWidgets.QPushButton(Form)
        self.ingresarButton.setGeometry(QtCore.QRect(100, 180, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ingresarButton.setFont(font)
        self.ingresarButton.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(72, 72, 72);")
        self.ingresarButton.setObjectName("ingresarButton")
        self.artistaLabel = QtWidgets.QLabel(Form)
        self.artistaLabel.setGeometry(QtCore.QRect(40, 140, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.artistaLabel.setFont(font)
        self.artistaLabel.setObjectName("artistaLabel")
        self.artistaInput = QtWidgets.QLineEdit(Form)
        self.artistaInput.setGeometry(QtCore.QRect(130, 140, 161, 20))
        self.artistaInput.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(72, 72, 72);")
        self.artistaInput.setObjectName("artistaInput")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.nombreLabel.setText(_translate("Form", "Título:"))
        self.ingresarAlbumLabel.setText(_translate("Form", "Ingresar Álbum"))
        self.ingresarButton.setText(_translate("Form", "Ingresar"))
        self.artistaLabel.setText(_translate("Form", "Artista:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    Form.setWindowTitle("Ingresar Album")
    sys.exit(app.exec_())
