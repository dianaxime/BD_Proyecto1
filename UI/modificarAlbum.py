# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modificarAlbum.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import psycopg2
from config import config
from PyQt5.QtWidgets import QMessageBox

class Ui_ModificarAlbum(object):
    def __init__(self,id, IDArtO):
        self.id=id
        self.IDArtO=IDArtO
        """print("este es id user: "+str(id))
        print("este es id album: "+str(IDArtO))"""
    def setupUi(self, Form):
        conexion=None
        try:
            params = config()
            conexion = psycopg2.connect(**params)
            # creación del cursor
            cur = conexion.cursor()
            print("este si es album "+str(self.IDArtO))
            cur.execute( "SELECT album.title FROM album WHERE album.albumid=%s",(self.IDArtO,))
            nombre=cur.fetchall()[0][0]
            cur.execute( "SELECT artist.name FROM artist JOIN album ON album.artistid=artist.artistid WHERE album.albumid=%s",(self.IDArtO,))
            artista=cur.fetchall()[0][0]
            print(nombre)
            print(artista)
            

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conexion is not None:
                conexion.close()
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
        self.tituloInput.setText(nombre)
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
        self.modificarButton.clicked.connect(self.modificarAlbum)
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
        self.artistaInput.setText(artista)
        self.artistaInput.setGeometry(QtCore.QRect(130, 140, 161, 20))
        self.artistaInput.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(72, 72, 72);")
        self.artistaInput.setObjectName("artistaInput")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Modificar album"))
        self.modificarAlbumLabel.setText(_translate("Form", "Modificar Álbum"))
        self.modificarButton.setText(_translate("Form", "Modificar"))
        self.tituloLabel.setText(_translate("Form", "Título:"))
        self.albumLabel.setText(_translate("Form", "Artista:"))


    def modificarAlbum(self):
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
            nombre=self.tituloInput.text()
            id=self.id
            IDArtO=self.IDArtO
            print ("--------adentro de funcion-----------")
            print("este es id user: "+str(id))
            print("este es id album: "+str(IDArtO))
            artista=self.artistaInput.text()
            cur.execute( "SELECT artist.artistid FROM artist WHERE artist.name=%s",(artista,))
            newArtistid=cur.fetchall()
            if (len(newArtistid)==0):
                blank=QMessageBox()
                blank.setIcon(QMessageBox.Information)
                blank.setWindowTitle("ERROR")
                blank.setText("El artista seleccionado no esta registrado.")
                blank.exec()
            else:
                newArtistid=newArtistid [0][0]
                #cur.execute("""SELECT add_bitacora(%s::numeric, %s::varchar, 3::numeric, 1::numeric )""", (id, nombre))
                cur.execute('''
                        UPDATE album
                        SET title = %s,
                            artistid=%s,
                            u_updated=%s
                        WHERE albumid = %s
                        ''',(nombre, newArtistid,id, IDArtO))
                #cur.execute("""SELECT add_bitacora(%s::numeric, %s::varchar, 2::numeric, 2::numeric )""", (id, nombre))
                conexion.commit()
                print("Lo edito")
                addedArtist=QMessageBox()
                addedArtist.setIcon(QMessageBox.Information)
                addedArtist.setWindowTitle("Listo")
                addedArtist.setText("Album modificado exitosamente")
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
    ui = Ui_ModificarAlbum()
    ui.setupUi(Form)
    Form.show()
    Form.setWindowTitle("Modificar Album")
    sys.exit(app.exec_())
