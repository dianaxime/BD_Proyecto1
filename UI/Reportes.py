# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Reportes.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from masCanciones import *
from artistasAlbums import *
from cancionesDuracion import *
from generoPromedio import *
from usuariosCanciones import *
from artistasGeneros import *
from artistPlaylist import *
from duracionPlaylist import *
from PyQt5.QtWidgets import QMessageBox

class Ui_Reportes(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 500)
        Form.setSizeIncrement(QtCore.QSize(0, 0))
        Form.setStyleSheet("background-color: rgb(85, 85, 255);")
        Form.setWindowIcon(QIcon('icono.png'))
        self.reportes = QtWidgets.QGroupBox(Form)
        self.reportes.setGeometry(QtCore.QRect(20, 30, 375, 450))
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

        self.generosArtista = QtWidgets.QRadioButton(self.reportes)
        self.generosArtista.setGeometry(QtCore.QRect(20, 180, 251, 17))
        self.generosArtista.setStyleSheet("color: rgb(236, 236, 236);")
        self.generosArtista.setObjectName("generosArtista")

        self.playlistArtist = QtWidgets.QRadioButton(self.reportes)
        self.playlistArtist.setGeometry(QtCore.QRect(20, 210, 251, 17))
        self.playlistArtist.setStyleSheet("color: rgb(236, 236, 236);")
        self.playlistArtist.setObjectName("promedioDuracion")

        self.playlistDuracion = QtWidgets.QRadioButton(self.reportes)
        self.playlistDuracion.setGeometry(QtCore.QRect(20, 240, 251, 17))
        self.playlistDuracion.setStyleSheet("color: rgb(236, 236, 236);")
        self.playlistDuracion.setObjectName("promedioDuracion")

        self.ventasSemana = QtWidgets.QRadioButton(self.reportes)
        self.ventasSemana.setGeometry(QtCore.QRect(20, 270, 300, 17))
        self.ventasSemana.setStyleSheet("color: rgb(236, 236, 236);")
        self.ventasSemana.setObjectName("ventasSemana")

        self.ventasArtista = QtWidgets.QRadioButton(self.reportes)
        self.ventasArtista.setGeometry(QtCore.QRect(20, 300, 320, 17))
        self.ventasArtista.setStyleSheet("color: rgb(236, 236, 236);")
        self.ventasArtista.setObjectName("ventasArtista")

        self.ventasGenero = QtWidgets.QRadioButton(self.reportes)
        self.ventasGenero.setGeometry(QtCore.QRect(20, 330, 310, 17))
        self.ventasGenero.setStyleSheet("color: rgb(236, 236, 236);")
        self.ventasGenero.setObjectName("ventasGenero")

        self.reprodArtista = QtWidgets.QRadioButton(self.reportes)
        self.reprodArtista.setGeometry(QtCore.QRect(20, 360, 300, 17))
        self.reprodArtista.setStyleSheet("color: rgb(236, 236, 236);")
        self.reprodArtista.setObjectName("reprodArtista")

        self.generarReporte = QtWidgets.QPushButton(self.reportes)
        self.generarReporte.setGeometry(QtCore.QRect(240, 400, 71, 23))
        self.generarReporte.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(72, 72, 72);")
        self.generarReporte.setObjectName("generarReporte")
        #self.generarReporte.clicked.connect(self.goTo)
        self.volverButton = QtWidgets.QPushButton(Form)
        self.volverButton.setGeometry(QtCore.QRect(50, 430, 75, 23))
        self.volverButton.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(72, 72, 72);")
        self.volverButton.setObjectName("volverButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def goTo(self, Form):
        if self.masCanciones.isChecked():
            self.window = QtWidgets.QWidget()
            self.ui = Ui_masCanciones()
            self.ui.setupUi(self.window)
            #Form.hide()
            self.window.show()
        elif self.masAlbums.isChecked():
            self.window = QtWidgets.QWidget()
            self.ui = Ui_artistasAlbums()
            self.ui.setupUi(self.window)
            #Form.hide()
            self.window.show()
        elif self.mayorDuracion.isChecked():
            self.window = QtWidgets.QWidget()
            self.ui = Ui_cancionesDuracion()
            self.ui.setupUi(self.window)
            #Form.hide()
            self.window.show()
        elif self.masRegistradas.isChecked():
            self.window = QtWidgets.QWidget()
            self.ui = Ui_usuariosCanciones()
            self.ui.setupUi(self.window)
            #Form.hide()
            self.window.show()
        elif self.promedioDuracion.isChecked():
            self.window = QtWidgets.QWidget()
            self.ui = Ui_generoPromedio()
            self.ui.setupUi(self.window)
            #Form.hide()
            self.window.show()
        elif self.generosArtista.isChecked():
            self.window = QtWidgets.QWidget()
            self.ui = Ui_artistasGeneros()
            self.ui.setupUi(self.window)
            #Form.hide()
            self.window.show()
        elif self.playlistArtist.isChecked():
            self.window = QtWidgets.QWidget()
            self.ui = Ui_artistPlaylist()
            self.ui.setupUi(self.window)
            #Form.hide()
            self.window.show()
        elif self.playlistDuracion.isChecked():
            self.window = QtWidgets.QWidget()
            self.ui = Ui_duracionPlaylist()
            self.ui.setupUi(self.window)
            #Form.hide()
            self.window.show()
        elif self.ventasSemana.isChecked():
            self.window = QtWidgets.QWidget()
            self.ui = Ui_duracionPlaylist()
            self.ui.setupUi(self.window)
            #Form.hide()
            self.window.show()
        elif self.ventasArtista.isChecked():
            self.window = QtWidgets.QWidget()
            self.ui = Ui_duracionPlaylist()
            self.ui.setupUi(self.window)
            #Form.hide()
            self.window.show()
        elif self.ventasGenero.isChecked():
            self.window = QtWidgets.QWidget()
            self.ui = Ui_duracionPlaylist()
            self.ui.setupUi(self.window)
            #Form.hide()
            self.window.show()
        elif self.reprodArtista.isChecked():
            self.window = QtWidgets.QWidget()
            self.ui = Ui_duracionPlaylist()
            self.ui.setupUi(self.window)
            #Form.hide()
            self.window.show()
        else:
            blank=QMessageBox()
            blank.setIcon(QMessageBox.Information)
            blank.setWindowTitle("ERROR")
            blank.setText("Por favor seleccione una opción")
            blank.exec()

    def openActions(self, Form):
        #self.window = QtWidgets.QWidget()
        #self.ui = Ui_Reportes()
        #self.ui.setupUi(self.window)
        Form.hide()
        #self.window.show()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Reportes"))
        self.reportes.setTitle(_translate("Form", "Reportes"))
        self.masCanciones.setText(_translate("Form", "Géneros con más canciones"))
        self.masAlbums.setText(_translate("Form", "Artistas con más álbums individuales"))
        self.mayorDuracion.setText(_translate("Form", "Canciones de mayor duración"))
        self.masRegistradas.setText(_translate("Form", "Usuarios con más canciones registradas"))
        self.promedioDuracion.setText(_translate("Form", "Promedio de duración de canciones por género"))
        
        self.generosArtista.setText(_translate("Form", "Artistas con mayor diversidad de géneros"))
        self.playlistArtist.setText(_translate("Form", "Cantidad de artistas diferentes por playlist"))
        self.playlistDuracion.setText(_translate("Form", "Duración de cada playlist"))

        self.ventasSemana.setText(_translate("Form", "Total de ventas por semana dado un rango de fechas"))
        self.ventasArtista.setText(_translate("Form", "Los N artistas con las mayores ventas para un rango de fechas"))
        self.ventasGenero.setText(_translate("Form", "Total de ventas por género para un rango de fechas"))
        self.reprodArtista.setText(_translate("Form", "Las N canciones con más reproducciones para un artista"))
        
        self.generarReporte.setText(_translate("Form", "Generar"))
        self.volverButton.setText(_translate("Form", "Volver"))
        self.generarReporte.clicked.connect(lambda:self.goTo(Form))
        self.volverButton.clicked.connect(lambda:self.openActions(Form))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Reportes()
    ui.setupUi(Form)
    Form.show()
    Form.setWindowTitle("Reportes")
    sys.exit(app.exec_())
