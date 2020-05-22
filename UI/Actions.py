# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Actions.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
from ingresarAlbum import Ui_IngresarAlbum
from ingresarArtista import Ui_IngresarArtista
from ingresarCancion import Ui_IngresarCancion
from buscarAlbum import Ui_BuscarAlbum
from buscarArtista import Ui_BuscarArtista
from buscarcancion import Ui_BuscarCancion
from eliminarAlbum import Ui_EliminarAlbum
from eliminarArtista import Ui_EliminarArtista
from eliminarCancion import Ui_EliminarCancion
from inactivarCancion import Ui_InactivarCancion
from searchArtist_form import Ui_searchArtist_form
from searchAlbum_form import Ui_searchAlbum_form
from searchTrack_form import Ui_searchTrack_form
from misCanciones import Ui_MisCanciones
from buscar_comprar import Ui_buscarComprar
import psycopg2
from config import config
import sys


class Ui_bienvenidaLabel(object):
    def __init__(self,id):
        self.id=id
        #print("este es el id del usuario "+str(id))
    def setupUi(self, bienvenidaLabel):
        bienvenidaLabel.setObjectName("bienvenidaLabel")
        bienvenidaLabel.resize(464, 570)
        bienvenidaLabel.setStyleSheet("background-color: rgb(85, 85, 255);")
        bienvenidaLabel.setWindowIcon(QIcon('icono.png'))
        self.label = QtWidgets.QLabel(bienvenidaLabel)
        self.label.setGeometry(QtCore.QRect(100, 30, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(236, 236, 236);")
        self.label.setObjectName("label")
        # GROUP BOX REGISTRO
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
        self.registrarBoton.clicked.connect(self.openRegistrar)
        # GROUP BOX MODIFICAR
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
        self.pushButton_3.clicked.connect(self.openModificar)
        # GROUP BOX ELIMINAR
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
        self.botonEliminar.clicked.connect(self.openEliminar)

        # GROUP BOX BUSCAR
        self.buscarGrupo = QtWidgets.QGroupBox(bienvenidaLabel)
        self.buscarGrupo.setGeometry(QtCore.QRect(30, 290, 122, 180))
        self.buscarGrupo.setStyleSheet("color: rgb(236, 236, 236);")
        self.buscarGrupo.setObjectName("buscarGrupo")
        self.buscarBoton = QtWidgets.QPushButton(self.buscarGrupo)
        self.buscarBoton.setGeometry(QtCore.QRect(25, 130, 75, 31))
        self.buscarBoton.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(72, 72, 72);")
        self.buscarBoton.setObjectName("registrarBoton")
        self.cancionBuscar = QtWidgets.QRadioButton(self.buscarGrupo)
        self.cancionBuscar.setGeometry(QtCore.QRect(20, 40, 82, 17))
        self.cancionBuscar.setObjectName("cancionBuscar")
        self.albumBuscar = QtWidgets.QRadioButton(self.buscarGrupo)
        self.albumBuscar.setGeometry(QtCore.QRect(20, 70, 82, 17))
        self.albumBuscar.setObjectName("albumBuscar")
        self.artistaBuscar = QtWidgets.QRadioButton(self.buscarGrupo)
        self.artistaBuscar.setGeometry(QtCore.QRect(20, 100, 82, 17))
        self.artistaBuscar.setObjectName("artistaBuscar")
        self.buscarBoton.clicked.connect(self.openBuscar)
        # GROUP BOX Inactivar
        self.inactivarGrupo = QtWidgets.QGroupBox(bienvenidaLabel)
        self.inactivarGrupo.setGeometry(QtCore.QRect(170, 290, 121, 180))
        self.inactivarGrupo.setStyleSheet("color: rgb(236, 236, 236);")
        self.inactivarGrupo.setObjectName("inactivarGrupo")
        self.cancionInactivar = QtWidgets.QRadioButton(self.inactivarGrupo)
        self.cancionInactivar.setGeometry(QtCore.QRect(20, 30, 82, 17))
        self.cancionInactivar.setObjectName("cancionInactivar")
        self.inactivarBoton = QtWidgets.QPushButton(self.inactivarGrupo)
        self.inactivarBoton.setGeometry(QtCore.QRect(25, 130, 75, 31))
        self.inactivarBoton.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(72, 72, 72);")
        self.inactivarBoton.setObjectName("inactivarBoton")
        self.inactivarBoton.clicked.connect(self.openInactivar)
        #GROUP BOX mis canciones
        self.misCancionesGrupo = QtWidgets.QGroupBox(bienvenidaLabel)
        self.misCancionesGrupo.setGeometry(QtCore.QRect(310, 290, 121, 180))
        self.misCancionesGrupo.setStyleSheet("color: rgb(236, 236, 236);")
        self.misCancionesGrupo.setObjectName("misCancionesGrupo")
        self.misCancionesBoton = QtWidgets.QPushButton(self.misCancionesGrupo)
        self.misCancionesBoton.setGeometry(QtCore.QRect(25, 130, 75, 31))
        self.misCancionesBoton.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(72, 72, 72);")
        self.misCancionesBoton.setObjectName("misCancionesBoton")
        self.misCancionesBoton.clicked.connect(self.openMisCanciones)
        self.comprar = QtWidgets.QRadioButton(self.misCancionesGrupo)
        self.comprar.setGeometry(QtCore.QRect(20, 40, 82, 17))
        self.comprar.setObjectName("Comprar")
        self.misCanciones = QtWidgets.QRadioButton(self.misCancionesGrupo)
        self.misCanciones.setGeometry(QtCore.QRect(20, 85, 90, 17))
        self.misCanciones.setObjectName("misCanciones")


        #Salir
        self.salir = QtWidgets.QPushButton(bienvenidaLabel)
        self.salir.setGeometry(QtCore.QRect(115, 500, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.salir.setFont(font)
        self.salir.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(72, 72, 72);")
        self.salir.setObjectName("salir")

        self.retranslateUi(bienvenidaLabel)
        QtCore.QMetaObject.connectSlotsByName(bienvenidaLabel)

    def goOut(self, Form):
        #self.window = QtWidgets.QWidget()
        #self.ui = Ui_buscarUsuario()
        #self.ui.setupUi(self.window)
        #Form.hide()
        #self.window.show()
        sys.exit()

    def retranslateUi(self, bienvenidaLabel):
        _translate = QtCore.QCoreApplication.translate
        bienvenidaLabel.setWindowTitle(_translate("bienvenidaLabel", "Principal"))
        self.label.setText(_translate("bienvenidaLabel", "Bienvenido"))
        # GROUP BOX REGISTRO
        self.registrarGrupo.setTitle(_translate("bienvenidaLabel", "Registrar"))
        self.registrarBoton.setText(_translate("bienvenidaLabel", "Añadir"))
        self.cancionRegistrar.setText(_translate("bienvenidaLabel", "Canción"))
        self.albumRegistrar.setText(_translate("bienvenidaLabel", "Álbum"))
        self.artistaRegistrar.setText(_translate("bienvenidaLabel", "Artista"))
        # GROUP BOX INACTIVAR
        self.inactivarGrupo.setTitle(_translate("bienvenidaLabel", "Inactivar"))
        self.cancionInactivar.setText(_translate("bienvenidaLabel", "Canción"))
        self.inactivarBoton.setText(_translate("bienvenidaLabel", "Inactivar"))
        # GROUP BOX MODIFICAR
        self.modificarGrupo.setTitle(_translate("bienvenidaLabel", "Modificar"))
        self.pushButton_3.setText(_translate("bienvenidaLabel", "Modificar"))
        self.cancionModificar.setText(_translate("bienvenidaLabel", "Canción"))
        self.albumModificar.setText(_translate("bienvenidaLabel", "Álbum"))
        self.artistaModificar.setText(_translate("bienvenidaLabel", "Artista"))
        # GROUP BOX BUSCAR
        self.buscarGrupo.setTitle(_translate("bienvenidaLabel", "Buscador"))
        self.buscarBoton.setText(_translate("bienvenidaLabel", "Buscar"))
        self.cancionBuscar.setText(_translate("bienvenidaLabel", "Canción"))
        self.albumBuscar.setText(_translate("bienvenidaLabel", "Álbum"))
        self.artistaBuscar.setText(_translate("bienvenidaLabel", "Artista"))
        # GROUP BOX ELIMINAR
        self.eliminarGrupo.setTitle(_translate("bienvenidaLabel", "Eliminar"))
        self.botonEliminar.setText(_translate("bienvenidaLabel", "Eliminar"))
        self.cancionEliminar.setText(_translate("bienvenidaLabel", "Canción"))
        self.albumEliminar.setText(_translate("bienvenidaLabel", "Álbum"))
        self.artistaEliminar.setText(_translate("bienvenidaLabel", "Artista"))
        self.salir.setText(_translate("bienvenidaLabel", "Salir"))
        self.salir.clicked.connect(lambda:self.goOut(bienvenidaLabel))
        # GROUP BOX MIS CANCIONES
        self.misCancionesGrupo.setTitle(_translate("bienvenidaLabel", "Mis canciones"))
        self.misCancionesBoton.setText(_translate("bienvenidaLabel", "Ir"))
        self.comprar.setText(_translate("bienvenidaLabel", "Comprar"))
        self.misCanciones.setText(_translate("bienvenidaLabel", "Mis Canciones"))
        #self.misCancionesLabel.setText(_translate("bienvenidaLabel", "Puedes ver tus\ntracks reproducidas\ny compradas"))

    
    def openRegistrar(self):
        conexion=None
        try:
            params = config()
            conexion = psycopg2.connect(**params)
            # creación del cursor
            cur = conexion.cursor()
            id=self.id
        #print(id)
            cur.execute("SELECT permisos_usuario.puede_registrar FROM permisos_usuario WHERE permisos_usuario.permisoid=%s",(id,))
            permisoRegistrar=cur.fetchall()[0][0]
            #print(permisoRegistrar)
            if permisoRegistrar:
                if self.cancionRegistrar.isChecked() == True:
                        self.window = QtWidgets.QWidget()
                        self.ui = Ui_IngresarCancion(self.id)
                        self.ui.setupUi(self.window)
                        #bienvenidaLabel.hide()
                        self.window.show()
                elif self.artistaRegistrar.isChecked() == True:
                        self.window = QtWidgets.QWidget()
                        self.ui = Ui_IngresarArtista(self.id)
                        self.ui.setupUi(self.window)
                        #bienvenidaLabel.hide()
                        self.window.show()
                elif self.albumRegistrar.isChecked() == True:
                        self.window = QtWidgets.QWidget()
                        self.ui = Ui_IngresarAlbum(self.id)
                        self.ui.setupUi(self.window)
                        #bienvenidaLabel.hide()
                        self.window.show()
                else:
                    blank=QMessageBox()
                    blank.setIcon(QMessageBox.Information)
                    blank.setWindowTitle("INCOMPLETO")
                    blank.setText("Por favor selecciona una opcion de registro")
                    blank.exec()
            else:
                blank=QMessageBox()
                blank.setIcon(QMessageBox.Information)
                blank.setWindowTitle("ERROR")
                blank.setText("Usted no tiene permiso de registrar")
                blank.exec()


        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conexion is not None:
                conexion.close()
    
    def openModificar(self):
        #Se verifica cual esta seleccionado
        conexion=None
        try:
            params = config()
            conexion = psycopg2.connect(**params)
            # creación del cursor
            cur = conexion.cursor()
            id=self.id
            #print(id)
            cur.execute("SELECT permisos_usuario.puede_modificar FROM permisos_usuario WHERE permisos_usuario.permisoid=%s",(id,))
            permisoModificar=cur.fetchall()[0][0]
            #print(permisoRegistrar)
            if permisoModificar:
                if self.cancionModificar.isChecked() == True:
                        self.window = QtWidgets.QWidget()
                        self.ui = Ui_BuscarCancion(self.id)
                        self.ui.setupUi(self.window)
                        #bienvenidaLabel.hide()
                        self.window.show()
                elif self.artistaModificar.isChecked() == True:
                        self.window = QtWidgets.QWidget()
                        self.ui = Ui_BuscarArtista(self.id)
                        self.ui.setupUi(self.window)
                        #bienvenidaLabel.hide()
                        self.window.show()
                elif self.albumModificar.isChecked() == True:
                        self.window = QtWidgets.QWidget()
                        self.ui = Ui_BuscarAlbum(self.id)
                        self.ui.setupUi(self.window)
                        #bienvenidaLabel.hide()
                        self.window.show()
                else:
                    blank=QMessageBox()
                    blank.setIcon(QMessageBox.Information)
                    blank.setWindowTitle("INCOMPLETO")
                    blank.setText("Por favor selecciona una opcion de modificacion")
                    blank.exec()
                
            else:
                blank=QMessageBox()
                blank.setIcon(QMessageBox.Information)
                blank.setWindowTitle("ERROR")
                blank.setText("Usted no tiene permiso para modificar")
                blank.exec()


        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conexion is not None:
                conexion.close()
    
    def openEliminar(self):
        conexion=None
        try:
            params = config()
            conexion = psycopg2.connect(**params)
            # creación del cursor
            cur = conexion.cursor()
            id=self.id
            #print(id)
            cur.execute("SELECT permisos_usuario.puede_eliminar FROM permisos_usuario WHERE permisos_usuario.permisoid=%s",(id,))
            permisoEliminar=cur.fetchall()[0][0]
            #print(permisoRegistrar)
            if permisoEliminar:
                if self.cancionEliminar.isChecked() == True:
                        self.window = QtWidgets.QWidget()
                        self.ui = Ui_EliminarCancion(self.id)
                        self.ui.setupUi(self.window)
                        #bienvenidaLabel.hide()
                        self.window.show()
                elif self.artistaEliminar.isChecked() == True:
                        self.window = QtWidgets.QWidget()
                        self.ui = Ui_EliminarArtista(self.id)
                        self.ui.setupUi(self.window)
                        #bienvenidaLabel.hide()
                        self.window.show()
                elif self.albumEliminar.isChecked() == True:
                        self.window = QtWidgets.QWidget()
                        self.ui = Ui_EliminarAlbum(self.id)
                        self.ui.setupUi(self.window)
                        #bienvenidaLabel.hide()
                        self.window.show()
                else:
                    blank=QMessageBox()
                    blank.setIcon(QMessageBox.Information)
                    blank.setWindowTitle("INCOMPLETO")
                    blank.setText("Por favor selecciona una opcion de eliminar")
                    blank.exec()
                
            else:
                blank=QMessageBox()
                blank.setIcon(QMessageBox.Information)
                blank.setWindowTitle("ERROR")
                blank.setText("Usted no tiene permiso para eliminar")
                blank.exec()


        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conexion is not None:
                conexion.close()
        

    def openInactivar(self):
        conexion=None
        try:
            params = config()
            conexion = psycopg2.connect(**params)
            # creación del cursor
            cur = conexion.cursor()
            id=self.id
            #print(id)
            cur.execute("SELECT permisos_usuario.puede_inactivar FROM permisos_usuario WHERE permisos_usuario.permisoid=%s",(id,))
            permisoInactivar=cur.fetchall()[0][0]
            #print(permisoRegistrar)
            if permisoInactivar:
                #Se verifica si esta seleccionado
                if self.cancionInactivar.isChecked() == True:
                        self.window = QtWidgets.QWidget()
                        self.ui = Ui_InactivarCancion()
                        self.ui.setupUi(self.window)
                        #bienvenidaLabel.hide()
                        self.window.show()
                else:
                    blank=QMessageBox()
                    blank.setIcon(QMessageBox.Information)
                    blank.setWindowTitle("INCOMPLETO")
                    blank.setText("Por favor selecciona una opcion de inactivar")
                    blank.exec()
                
            else:
                blank=QMessageBox()
                blank.setIcon(QMessageBox.Information)
                blank.setWindowTitle("ERROR")
                blank.setText("Usted no tiene permiso para inactivar")
                blank.exec()


        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conexion is not None:
                conexion.close()

    def openBuscar(self):
        #Se verifica cual esta seleccionado
        id=self.id
        if self.cancionBuscar.isChecked() == True:
            self.window = QtWidgets.QWidget()
            self.ui = Ui_searchTrack_form()
            self.ui.setupUi(self.window)
            #bienvenidaLabel.hide()
            self.window.show()
        elif self.artistaBuscar.isChecked() == True:
            self.window = QtWidgets.QWidget()
            self.ui = Ui_searchArtist_form()
            self.ui.setupUi(self.window)
            #bienvenidaLabel.hide()
            self.window.show()
        elif self.albumBuscar.isChecked() == True:
            self.window = QtWidgets.QWidget()
            self.ui = Ui_searchAlbum_form()
            self.ui.setupUi(self.window)
            #bienvenidaLabel.hide()
            self.window.show()
        else:
            blank=QMessageBox()
            blank.setIcon(QMessageBox.Information)
            blank.setWindowTitle("INCOMPLETO")
            blank.setText("Por favor selecciona una opcion de modificacion")
            blank.exec()

    def openMisCanciones(self):
        #Se verifica cual esta seleccionado
        id=self.id

        if self.comprar.isChecked() == True:
            self.window = QtWidgets.QWidget()
            self.ui = Ui_buscarComprar(self.id)
            self.ui.setupUi(self.window)
            #bienvenidaLabel.hide()
            self.window.show()
        elif self.misCanciones.isChecked() == True:
            self.window = QtWidgets.QWidget()
            self.ui = Ui_MisCanciones(self.id)
            self.ui.setupUi(self.window)
            #bienvenidaLabel.hide()
            self.window.show()
        else:
            blank=QMessageBox()
            blank.setIcon(QMessageBox.Information)
            blank.setWindowTitle("INCOMPLETO")
            blank.setText("Por favor selecciona una opcion de modificacion")
            blank.exec()
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    bienvenidaLabel = QtWidgets.QWidget()
    ui = Ui_bienvenidaLabel()
    ui.setupUi(bienvenidaLabel)
    bienvenidaLabel.show()
    bienvenidaLabel.setWindowTitle("Principal")
    sys.exit(app.exec_())
