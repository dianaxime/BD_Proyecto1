# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Reportes.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(388, 334)
        Form.setSizeIncrement(QtCore.QSize(0, 0))
        Form.setStyleSheet("background-color: rgb(85, 85, 255);")
        Form.setWindowIcon(QIcon('icono.png'))
        self.reportes = QtWidgets.QGroupBox(Form)
        self.reportes.setGeometry(QtCore.QRect(20, 40, 331, 251))
        self.reportes.setStyleSheet("color: rgb(236, 236, 236);")
        self.reportes.setObjectName("reportes")
        self.masCanciones = QtWidgets.QRadioButton(self.reportes)
        self.masCanciones.setGeometry(QtCore.QRect(20, 30, 151, 17))
        self.masCanciones.setStyleSheet("color: rgb(236, 236, 236);")
        self.masCanciones.setObjectName("masCanciones")
        self.masAlbums = QtWidgets.QRadioButton(self.reportes)
        self.masAlbums.setGeometry(QtCore.QRect(20, 60, 201, 17))
        self.masAlbums.setStyleSheet("color: rgb(236, 236, 236);")
        self.masAlbums.setObjectName("masAlbums")
        self.mayorDuracion = QtWidgets.QRadioButton(self.reportes)
        self.mayorDuracion.setGeometry(QtCore.QRect(20, 90, 161, 17))
        self.mayorDuracion.setStyleSheet("color: rgb(236, 236, 236);")
        self.mayorDuracion.setObjectName("mayorDuracion")
        self.masRegistradas = QtWidgets.QRadioButton(self.reportes)
        self.masRegistradas.setGeometry(QtCore.QRect(20, 120, 211, 17))
        self.masRegistradas.setStyleSheet("color: rgb(236, 236, 236);")
        self.masRegistradas.setObjectName("masRegistradas")
        self.promedioDuracion = QtWidgets.QRadioButton(self.reportes)
        self.promedioDuracion.setGeometry(QtCore.QRect(20, 150, 251, 17))
        self.promedioDuracion.setStyleSheet("color: rgb(236, 236, 236);")
        self.promedioDuracion.setObjectName("promedioDuracion")
        self.generarReporte = QtWidgets.QPushButton(self.reportes)
        self.generarReporte.setGeometry(QtCore.QRect(220, 190, 71, 41))
        self.generarReporte.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(72, 72, 72);")
        self.generarReporte.setObjectName("generarReporte")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.reportes.setTitle(_translate("Form", "Reportes"))
        self.masCanciones.setText(_translate("Form", "Géneros con más canciones"))
        self.masAlbums.setText(_translate("Form", "Artistas con más álbums individuales"))
        self.mayorDuracion.setText(_translate("Form", "Canciones de mayor duración"))
        self.masRegistradas.setText(_translate("Form", "Usuarios con más canciones registradas"))
        self.promedioDuracion.setText(_translate("Form", "Promedio de duración de canciones por género"))
        self.generarReporte.setText(_translate("Form", "Generar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    Form.setWindowTitle("Reportes")
    sys.exit(app.exec_())