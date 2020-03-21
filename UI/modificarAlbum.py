# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modificarAlbum.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(333, 260)
        Form.setStyleSheet("background-color: rgb(85, 85, 255);\n"
"color: rgb(236, 236, 236);")
        Form.setWindowIcon(QIcon('icono.png'))
        self.modificarAlbumLabel = QtWidgets.QLabel(Form)
        self.modificarAlbumLabel.setGeometry(QtCore.QRect(90, 20, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.modificarAlbumLabel.setFont(font)
        self.modificarAlbumLabel.setObjectName("modificarAlbumLabel")
        self.tituloInput = QtWidgets.QLineEdit(Form)
        self.tituloInput.setGeometry(QtCore.QRect(130, 90, 161, 20))
        self.tituloInput.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(72, 72, 72);")
        self.tituloInput.setObjectName("tituloInput")
        self.modificarButton = QtWidgets.QPushButton(Form)
        self.modificarButton.setGeometry(QtCore.QRect(100, 190, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.modificarButton.setFont(font)
        self.modificarButton.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(72, 72, 72);")
        self.modificarButton.setObjectName("modificarButton")
        self.tituloLabel = QtWidgets.QLabel(Form)
        self.tituloLabel.setGeometry(QtCore.QRect(40, 90, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tituloLabel.setFont(font)
        self.tituloLabel.setObjectName("tituloLabel")
        self.albumLabel = QtWidgets.QLabel(Form)
        self.albumLabel.setGeometry(QtCore.QRect(40, 140, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.albumLabel.setFont(font)
        self.albumLabel.setObjectName("albumLabel")
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
        self.modificarAlbumLabel.setText(_translate("Form", "Modificar Álbum"))
        self.modificarButton.setText(_translate("Form", "Modificar"))
        self.tituloLabel.setText(_translate("Form", "Título:"))
        self.albumLabel.setText(_translate("Form", "Artista:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    Form.setWindowTitle("Modificar Album")
    sys.exit(app.exec_())
