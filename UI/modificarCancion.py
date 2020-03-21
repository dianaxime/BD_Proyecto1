# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modificarCancion.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon


class Ui_ModificarCancion(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(353, 510)
        Form.setStyleSheet("background-color: rgb(85, 85, 255);\n"
"color: rgb(236, 236, 236);")
        Form.setWindowIcon(QIcon('icono.png'))
        self.tipoLabel = QtWidgets.QLabel(Form)
        self.tipoLabel.setGeometry(QtCore.QRect(50, 180, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tipoLabel.setFont(font)
        self.tipoLabel.setObjectName("tipoLabel")
        self.generoLabel = QtWidgets.QLabel(Form)
        self.generoLabel.setGeometry(QtCore.QRect(50, 220, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.generoLabel.setFont(font)
        self.generoLabel.setObjectName("generoLabel")
        self.nombreInput = QtWidgets.QLineEdit(Form)
        self.nombreInput.setGeometry(QtCore.QRect(140, 100, 161, 20))
        self.nombreInput.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(72, 72, 72);")
        self.nombreInput.setObjectName("nombreInput")
        self.tipoInput = QtWidgets.QLineEdit(Form)
        self.tipoInput.setGeometry(QtCore.QRect(140, 180, 161, 20))
        self.tipoInput.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(72, 72, 72);")
        self.tipoInput.setObjectName("tipoInput")
        self.precioLabel = QtWidgets.QLabel(Form)
        self.precioLabel.setGeometry(QtCore.QRect(50, 380, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.precioLabel.setFont(font)
        self.precioLabel.setObjectName("precioLabel")
        self.modificarButton = QtWidgets.QPushButton(Form)
        self.modificarButton.setGeometry(QtCore.QRect(120, 430, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.modificarButton.setFont(font)
        self.modificarButton.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(72, 72, 72);")
        self.modificarButton.setObjectName("modificarButton")
        self.nombreLabel = QtWidgets.QLabel(Form)
        self.nombreLabel.setGeometry(QtCore.QRect(50, 100, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nombreLabel.setFont(font)
        self.nombreLabel.setObjectName("nombreLabel")
        self.precioInput = QtWidgets.QLineEdit(Form)
        self.precioInput.setGeometry(QtCore.QRect(140, 380, 161, 20))
        self.precioInput.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(72, 72, 72);")
        self.precioInput.setObjectName("precioInput")
        self.duracionLabel = QtWidgets.QLabel(Form)
        self.duracionLabel.setGeometry(QtCore.QRect(50, 300, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.duracionLabel.setFont(font)
        self.duracionLabel.setObjectName("duracionLabel")
        self.compositorLabel = QtWidgets.QLabel(Form)
        self.compositorLabel.setGeometry(QtCore.QRect(50, 260, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.compositorLabel.setFont(font)
        self.compositorLabel.setObjectName("compositorLabel")
        self.albumInput = QtWidgets.QLineEdit(Form)
        self.albumInput.setGeometry(QtCore.QRect(140, 140, 161, 20))
        self.albumInput.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(72, 72, 72);")
        self.albumInput.setObjectName("albumInput")
        self.compositorInput = QtWidgets.QLineEdit(Form)
        self.compositorInput.setGeometry(QtCore.QRect(140, 260, 161, 20))
        self.compositorInput.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(72, 72, 72);")
        self.compositorInput.setObjectName("compositorInput")
        self.tamanoLabel = QtWidgets.QLabel(Form)
        self.tamanoLabel.setGeometry(QtCore.QRect(50, 340, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tamanoLabel.setFont(font)
        self.tamanoLabel.setObjectName("tamanoLabel")
        self.duracionInput = QtWidgets.QLineEdit(Form)
        self.duracionInput.setGeometry(QtCore.QRect(140, 300, 161, 20))
        self.duracionInput.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(72, 72, 72);")
        self.duracionInput.setObjectName("duracionInput")
        self.albumLabel = QtWidgets.QLabel(Form)
        self.albumLabel.setGeometry(QtCore.QRect(50, 140, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.albumLabel.setFont(font)
        self.albumLabel.setObjectName("albumLabel")
        self.tamanoInput = QtWidgets.QLineEdit(Form)
        self.tamanoInput.setGeometry(QtCore.QRect(140, 340, 161, 20))
        self.tamanoInput.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(72, 72, 72);")
        self.tamanoInput.setObjectName("tamanoInput")
        self.generoInput = QtWidgets.QLineEdit(Form)
        self.generoInput.setGeometry(QtCore.QRect(140, 220, 161, 20))
        self.generoInput.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(72, 72, 72);")
        self.generoInput.setObjectName("generoInput")
        self.modificarCancionLabel = QtWidgets.QLabel(Form)
        self.modificarCancionLabel.setGeometry(QtCore.QRect(100, 30, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.modificarCancionLabel.setFont(font)
        self.modificarCancionLabel.setObjectName("modificarCancionLabel")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.tipoLabel.setText(_translate("Form", "Tipo:"))
        self.generoLabel.setText(_translate("Form", "Género:"))
        self.precioLabel.setText(_translate("Form", "Precio:"))
        self.modificarButton.setText(_translate("Form", "Modificar"))
        self.nombreLabel.setText(_translate("Form", "Nombre:"))
        self.duracionLabel.setText(_translate("Form", "Duración:"))
        self.compositorLabel.setText(_translate("Form", "Compositor:"))
        self.tamanoLabel.setText(_translate("Form", "Tamaño:"))
        self.albumLabel.setText(_translate("Form", "Álbum:"))
        self.modificarCancionLabel.setText(_translate("Form", "Modificar Canción"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_ModificarCancion()
    ui.setupUi(Form)
    Form.show()
    Form.setWindowTitle("Modificar Cancion")
    sys.exit(app.exec_())
