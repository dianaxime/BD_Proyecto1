# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Actions.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_bienvenidaLabel(object):
    def setupUi(self, bienvenidaLabel):
        bienvenidaLabel.setObjectName("bienvenidaLabel")
        bienvenidaLabel.resize(464, 425)
        bienvenidaLabel.setStyleSheet("background-color: rgb(85, 85, 255);")
        self.label = QtWidgets.QLabel(bienvenidaLabel)
        self.label.setGeometry(QtCore.QRect(100, 30, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(236, 236, 236);")
        self.label.setObjectName("label")
        self.registrarGrupo = QtWidgets.QGroupBox(bienvenidaLabel)
        self.registrarGrupo.setGeometry(QtCore.QRect(30, 100, 121, 181))
        self.registrarGrupo.setStyleSheet("color: rgb(236, 236, 236);")
        self.registrarGrupo.setObjectName("registrarGrupo")
        self.registrarBoton = QtWidgets.QPushButton(self.registrarGrupo)
        self.registrarBoton.setGeometry(QtCore.QRect(20, 130, 75, 31))
        self.registrarBoton.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(72, 72, 72);")
        self.registrarBoton.setObjectName("registrarBoton")
        self.cancionRegistrar = QtWidgets.QRadioButton(self.registrarGrupo)
        self.cancionRegistrar.setGeometry(QtCore.QRect(20, 40, 82, 17))
        self.cancionRegistrar.setObjectName("cancionRegistrar")
        self.albumRegistrar = QtWidgets.QRadioButton(self.registrarGrupo)
        self.albumRegistrar.setGeometry(QtCore.QRect(20, 70, 82, 17))
        self.albumRegistrar.setObjectName("albumRegistrar")
        self.artistaRegistrar = QtWidgets.QRadioButton(self.registrarGrupo)
        self.artistaRegistrar.setGeometry(QtCore.QRect(20, 100, 82, 17))
        self.artistaRegistrar.setObjectName("artistaRegistrar")
        self.inactivarGrupo = QtWidgets.QGroupBox(bienvenidaLabel)
        self.inactivarGrupo.setGeometry(QtCore.QRect(30, 290, 401, 111))
        self.inactivarGrupo.setStyleSheet("color: rgb(236, 236, 236);")
        self.inactivarGrupo.setObjectName("inactivarGrupo")
        self.cancionInactivar = QtWidgets.QRadioButton(self.inactivarGrupo)
        self.cancionInactivar.setGeometry(QtCore.QRect(20, 30, 82, 17))
        self.cancionInactivar.setObjectName("cancionInactivar")
        self.inactivarBoton = QtWidgets.QPushButton(self.inactivarGrupo)
        self.inactivarBoton.setGeometry(QtCore.QRect(160, 60, 75, 31))
        self.inactivarBoton.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(72, 72, 72);")
        self.inactivarBoton.setObjectName("inactivarBoton")
        self.modificarGrupo = QtWidgets.QGroupBox(bienvenidaLabel)
        self.modificarGrupo.setGeometry(QtCore.QRect(170, 100, 121, 181))
        self.modificarGrupo.setStyleSheet("color: rgb(236, 236, 236);")
        self.modificarGrupo.setObjectName("modificarGrupo")
        self.pushButton_3 = QtWidgets.QPushButton(self.modificarGrupo)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 130, 75, 31))
        self.pushButton_3.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(72, 72, 72);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.cancionModificar = QtWidgets.QRadioButton(self.modificarGrupo)
        self.cancionModificar.setGeometry(QtCore.QRect(20, 40, 82, 17))
        self.cancionModificar.setObjectName("cancionModificar")
        self.albumModificar = QtWidgets.QRadioButton(self.modificarGrupo)
        self.albumModificar.setGeometry(QtCore.QRect(20, 70, 82, 17))
        self.albumModificar.setObjectName("albumModificar")
        self.artistaModificar = QtWidgets.QRadioButton(self.modificarGrupo)
        self.artistaModificar.setGeometry(QtCore.QRect(20, 100, 82, 17))
        self.artistaModificar.setObjectName("artistaModificar")
        self.eliminarGrupo = QtWidgets.QGroupBox(bienvenidaLabel)
        self.eliminarGrupo.setGeometry(QtCore.QRect(310, 100, 121, 181))
        self.eliminarGrupo.setStyleSheet("color: rgb(236, 236, 236);")
        self.eliminarGrupo.setObjectName("eliminarGrupo")
        self.botonEliminar = QtWidgets.QPushButton(self.eliminarGrupo)
        self.botonEliminar.setGeometry(QtCore.QRect(20, 130, 75, 31))
        self.botonEliminar.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(72, 72, 72);")
        self.botonEliminar.setObjectName("botonEliminar")
        self.cancionEliminar = QtWidgets.QRadioButton(self.eliminarGrupo)
        self.cancionEliminar.setGeometry(QtCore.QRect(20, 40, 82, 17))
        self.cancionEliminar.setObjectName("cancionEliminar")
        self.albumEliminar = QtWidgets.QRadioButton(self.eliminarGrupo)
        self.albumEliminar.setGeometry(QtCore.QRect(20, 70, 82, 17))
        self.albumEliminar.setObjectName("albumEliminar")
        self.artistaEliminar = QtWidgets.QRadioButton(self.eliminarGrupo)
        self.artistaEliminar.setGeometry(QtCore.QRect(20, 100, 82, 17))
        self.artistaEliminar.setObjectName("artistaEliminar")

        self.retranslateUi(bienvenidaLabel)
        QtCore.QMetaObject.connectSlotsByName(bienvenidaLabel)

    def retranslateUi(self, bienvenidaLabel):
        _translate = QtCore.QCoreApplication.translate
        bienvenidaLabel.setWindowTitle(_translate("bienvenidaLabel", "Form"))
        self.label.setText(_translate("bienvenidaLabel", "Bienvenido"))
        self.registrarGrupo.setTitle(_translate("bienvenidaLabel", "Registrar"))
        self.registrarBoton.setText(_translate("bienvenidaLabel", "Añadir"))
        self.cancionRegistrar.setText(_translate("bienvenidaLabel", "Canción"))
        self.albumRegistrar.setText(_translate("bienvenidaLabel", "Álbum"))
        self.artistaRegistrar.setText(_translate("bienvenidaLabel", "Artista"))
        self.inactivarGrupo.setTitle(_translate("bienvenidaLabel", "Inactivar"))
        self.cancionInactivar.setText(_translate("bienvenidaLabel", "Canción"))
        self.inactivarBoton.setText(_translate("bienvenidaLabel", "Inactivar"))
        self.modificarGrupo.setTitle(_translate("bienvenidaLabel", "Modificar"))
        self.pushButton_3.setText(_translate("bienvenidaLabel", "Modificar"))
        self.cancionModificar.setText(_translate("bienvenidaLabel", "Canción"))
        self.albumModificar.setText(_translate("bienvenidaLabel", "Álbum"))
        self.artistaModificar.setText(_translate("bienvenidaLabel", "Artista"))
        self.eliminarGrupo.setTitle(_translate("bienvenidaLabel", "Eliminar"))
        self.botonEliminar.setText(_translate("bienvenidaLabel", "Eliminar"))
        self.cancionEliminar.setText(_translate("bienvenidaLabel", "Canción"))
        self.albumEliminar.setText(_translate("bienvenidaLabel", "Álbum"))
        self.artistaEliminar.setText(_translate("bienvenidaLabel", "Artista"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    bienvenidaLabel = QtWidgets.QWidget()
    ui = Ui_bienvenidaLabel()
    ui.setupUi(bienvenidaLabel)
    bienvenidaLabel.show()
    sys.exit(app.exec_())
