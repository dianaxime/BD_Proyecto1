# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'buscarUsuario.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(324, 251)
        Form.setStyleSheet("background-color: rgb(85, 85, 255);\n"
"color: rgb(236, 236, 236);")
        self.continuarButton = QtWidgets.QPushButton(Form)
        self.continuarButton.setGeometry(QtCore.QRect(100, 180, 131, 41))
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
        self.nombreInput.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.nombreInput.setObjectName("nombreInput")
        self.nombreLabel = QtWidgets.QLabel(Form)
        self.nombreLabel.setGeometry(QtCore.QRect(40, 90, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nombreLabel.setFont(font)
        self.nombreLabel.setObjectName("nombreLabel")
        self.apellidoInput = QtWidgets.QLineEdit(Form)
        self.apellidoInput.setGeometry(QtCore.QRect(130, 134, 161, 20))
        self.apellidoInput.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.apellidoInput.setObjectName("apellidoInput")
        self.apellidoLabel = QtWidgets.QLabel(Form)
        self.apellidoLabel.setGeometry(QtCore.QRect(40, 130, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.apellidoLabel.setFont(font)
        self.apellidoLabel.setObjectName("apellidoLabel")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.continuarButton.setText(_translate("Form", "Continuar"))
        self.buscarLabel.setText(_translate("Form", "Ingrese usuario a modificar:"))
        self.nombreLabel.setText(_translate("Form", "Nombre:"))
        self.apellidoLabel.setText(_translate("Form", "Apellido:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
