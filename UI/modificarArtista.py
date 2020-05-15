# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modificarArtista.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import psycopg2
from PyQt5.QtWidgets import QMessageBox
from config import config

class Ui_ModificarArtista(object):
    def __init__(self,id, IDArtO):
        self.id=id
        self.IDArtO=IDArtO
    def setupUi(self, Form):

        conexion=None
        try:
            params = config()

            #print(params)
            # Conexion al servidor de PostgreSQL
            #print('Conectando a la base de datos PostgreSQL...')
            conexion = psycopg2.connect(**params)
            # creación del cursor
            cur = conexion.cursor()
            # Se obtienen los resultados
            #db_version = cur.fetchone()
            print(self.id)
            cur.execute( "SELECT artist.name FROM artist WHERE artist.artistid=%s",(self.IDArtO,))
            nombre=cur.fetchall()[0][0]
            print(nombre)
            

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conexion is not None:
                conexion.close()
        #aqui empieza lo que estaba originalmente------------------------------------------------------------------------------------------------------------
        Form.setObjectName("Form")
        Form.resize(333, 232)
        Form.setStyleSheet("background-color: rgb(85, 85, 255);\n"
"color: rgb(236, 236, 236);")
        Form.setWindowIcon(QIcon('icono.png'))
        self.modificarButton = QtWidgets.QPushButton(Form)
        self.modificarButton.setGeometry(QtCore.QRect(100, 150, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.modificarButton.setFont(font)
        self.modificarButton.clicked.connect(self.modificarArtista)
        self.modificarButton.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(72, 72, 72);")
        self.modificarButton.setObjectName("modificarButton")
        self.nombreLabel = QtWidgets.QLabel(Form)
        self.nombreLabel.setGeometry(QtCore.QRect(40, 100, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nombreLabel.setFont(font)
        self.nombreLabel.setObjectName("nombreLabel")
        self.modificarCancionLabel = QtWidgets.QLabel(Form)
        self.modificarCancionLabel.setGeometry(QtCore.QRect(90, 30, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.modificarCancionLabel.setFont(font)
        self.modificarCancionLabel.setObjectName("modificarCancionLabel")
        self.nombreInput = QtWidgets.QLineEdit(Form)
        self.nombreInput.setText(nombre)
        self.nombreInput.setGeometry(QtCore.QRect(130, 100, 161, 20))
        self.nombreInput.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(72, 72, 72);")
        self.nombreInput.setObjectName("nombreInput")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Modificar artista"))
        self.modificarButton.setText(_translate("Form", "Modificar"))
        self.nombreLabel.setText(_translate("Form", "Nombre:"))
        self.modificarCancionLabel.setText(_translate("Form", "Modificar Artista"))

    def modificarArtista(self):
        conexion=None
        try:
            params = config()

            #print(params)
            # Conexion al servidor de PostgreSQL
            #print('Conectando a la base de datos PostgreSQL...')
            conexion = psycopg2.connect(**params)
            # creación del cursor
            cur = conexion.cursor()
            # Se obtienen los resultados
            #db_version = cur.fetchone()
            nombre=self.nombreInput.text()
            id=self.id
            IDArtO=self.IDArtO
            cur.execute('''
                UPDATE artist
                SET name = %s,
                u_updated=%s
                WHERE artistid = %s
                ''',(nombre, id, IDArtO))
            #cur.execute("""SELECT add_bitacora(%s::numeric, %s::varchar, 2::numeric, 4::numeric )""", (id, nombre))
            conexion.commit()
            addedArtist=QMessageBox()
            addedArtist.setIcon(QMessageBox.Information)
            addedArtist.setWindowTitle("Listo")
            addedArtist.setText("Artista modificado exitosamente")
            addedArtist.exec()
            
            

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conexion is not None:
                conexion.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_ModificarArtista()
    ui.setupUi(Form)
    Form.show()
    Form.setWindowTitle("Modificar Artista")
    sys.exit(app.exec_())
