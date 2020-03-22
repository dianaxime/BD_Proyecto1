# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'permisosUsuario.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import psycopg2
from config import config

class Ui_permisosUsuario(object):
    def __init__(self, message):
        self.message=message
        """ Conexión al servidor de pases de datos PostgreSQL """
        conexion = None
        try:
            # Lectura de los parámetros de conexion
            params = config()
            # Conexion al servidor de PostgreSQL
            conexion = psycopg2.connect(**params)
            # creación del cursor
            cur = conexion.cursor()
            # Ejecución la consulta para obtener la conexión
            cur.execute('SELECT version()')
            # Se obtienen los resultados
            db_version = cur.fetchone()
            # Ejecutamos una consulta
            cur.execute( "SELECT permisos_usuario.puede_registrar, permisos_usuario.puede_inactivar, permisos_usuario.puede_eliminar, permisos_usuario.puede_modificar FROM permisos_usuario WHERE permisos_usuario.customerid=%s",(message[0][0],) )
            self.data=cur.fetchall()
            # Cerremos el cursor
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conexion is not None:
                conexion.close()

    def setupUi(self, permisosUsuario):
        permisosUsuario.setObjectName("permisosUsuario")
        permisosUsuario.resize(397, 273)
        permisosUsuario.setStyleSheet("background-color: rgb(85, 85, 255);\n"
"color: rgb(236, 236, 236);")
        permisosUsuario.setWindowIcon(QIcon('icono.png'))
        self.label = QtWidgets.QLabel(permisosUsuario)
        self.label.setGeometry(QtCore.QRect(20, 30, 351, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.permisoRegistrar = QtWidgets.QCheckBox(permisosUsuario)
        self.permisoRegistrar.setGeometry(QtCore.QRect(30, 120, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.permisoRegistrar.setFont(font)
        self.permisoRegistrar.setObjectName("permisoRegistrar")
        self.continuarButton = QtWidgets.QPushButton(permisosUsuario)
        self.continuarButton.setGeometry(QtCore.QRect(120, 210, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.continuarButton.setFont(font)
        self.continuarButton.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(72, 72, 72);")
        self.continuarButton.setObjectName("continuarButton")
        self.permisoModificar = QtWidgets.QCheckBox(permisosUsuario)
        self.permisoModificar.setGeometry(QtCore.QRect(30, 160, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.permisoModificar.setFont(font)
        self.permisoModificar.setObjectName("permisoModificar")
        self.permisoEliminar = QtWidgets.QCheckBox(permisosUsuario)
        self.permisoEliminar.setGeometry(QtCore.QRect(210, 160, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.permisoEliminar.setFont(font)
        self.permisoEliminar.setObjectName("permisoEliminar")
        self.permisoInactivar = QtWidgets.QCheckBox(permisosUsuario)
        self.permisoInactivar.setGeometry(QtCore.QRect(210, 120, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.permisoInactivar.setFont(font)
        self.permisoInactivar.setObjectName("permisoInactivar")

        self.permisoRegistrar.setChecked(self.data[0][0])
        self.permisoInactivar.setChecked(self.data[0][1])
        self.permisoEliminar.setChecked(self.data[0][2])
        self.permisoModificar.setChecked(self.data[0][3])
        self.label.setText(self.message[0][1]+' '+self.message[0][2])

        self.retranslateUi(permisosUsuario)
        QtCore.QMetaObject.connectSlotsByName(permisosUsuario)

    def modificar(self,Form):
        """ Conexión al servidor de pases de datos PostgreSQL """
        conexion = None
        try:
            # Lectura de los parámetros de conexion
            params = config()
            # Conexion al servidor de PostgreSQL
            conexion = psycopg2.connect(**params)
            # creación del cursor
            cur = conexion.cursor()
            # Ejecución la consulta para obtener la conexión
            cur.execute('SELECT version()')
            # Se obtienen los resultados
            db_version = cur.fetchone()
            # Ejecutamos una consulta
            cur.execute("UPDATE permisos_usuario SET puede_registrar=%s, puede_inactivar=%s, puede_eliminar=%s, puede_modificar=%s WHERE customerid=%s",(self.permisoRegistrar.isChecked(), self.permisoInactivar.isChecked(), self.permisoEliminar.isChecked(), self.permisoModificar.isChecked(),self.message[0][0]))
            conexion.commit()
            # Cerremos el cursor
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conexion is not None:
                conexion.close()
        #self.window = QtWidgets.QWidget()
        #self.ui = Ui_Reportes()
        #self.ui.setupUi(self.window)
        Form.hide()
        #self.window.show()

    def retranslateUi(self, permisosUsuario):
        _translate = QtCore.QCoreApplication.translate
        permisosUsuario.setWindowTitle(_translate("permisosUsuario", "Permisos usuario"))
        #self.label.setText(_translate("permisosUsuario", "<html><head/><body><p align=\"center\">Nombre_Usuario</p></body></html>"))
        self.permisoRegistrar.setText(_translate("permisosUsuario", "Permiso registrar"))
        self.continuarButton.setText(_translate("permisosUsuario", "Guardar Cambios"))
        self.permisoModificar.setText(_translate("permisosUsuario", "Permiso modificar"))
        self.permisoEliminar.setText(_translate("permisosUsuario", "Permiso eliminar"))
        self.permisoInactivar.setText(_translate("permisosUsuario", "Permiso inactivar"))
        self.continuarButton.clicked.connect(lambda:self.modificar(permisosUsuario))


"""if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    permisosUsuario = QtWidgets.QWidget()
    ui = Ui_permisosUsuario()
    ui.setupUi(permisosUsuario)
    permisosUsuario.show()
    sys.exit(app.exec_())"""
