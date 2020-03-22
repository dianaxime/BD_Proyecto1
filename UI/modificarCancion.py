# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modificarCancion.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import psycopg2
from config import config
from PyQt5.QtWidgets import QMessageBox


class Ui_ModificarCancion(object):
    def __init__(self,id):
        self.id=id
    def setupUi(self, Form):
        conexion=None
        try:
            params = config()
            conexion = psycopg2.connect(**params)
            # creación del cursor
            cur = conexion.cursor()
            print(self.id)
            cur.execute( "SELECT track.name FROM track WHERE track.trackid=%s",(self.id,))
            nombre=cur.fetchall()[0][0]
            cur.execute( "SELECT album.title FROM album JOIN track ON album.albumid=track.albumid WHERE track.trackid=%s",(self.id,))
            album=cur.fetchall()[0][0]
            cur.execute( "SELECT mediatype.name FROM mediatype JOIN track ON mediatype.mediatypeid=track.mediatypeid WHERE track.trackid=%s",(self.id,))
            media=cur.fetchall()[0][0]
            cur.execute( "SELECT genre.name FROM genre JOIN track ON genre.genreid=track.genreid WHERE track.trackid=%s",(self.id,))
            genre=cur.fetchall()[0][0]
            cur.execute( "SELECT track.composer FROM track WHERE track.trackid=%s",(self.id,))
            compositor=cur.fetchall()[0][0]
            cur.execute( "SELECT track.milliseconds FROM track WHERE track.trackid=%s",(self.id,))
            milli=cur.fetchall()[0][0]
            milli=str(milli)
            cur.execute( "SELECT track.bytes FROM track WHERE track.trackid=%s",(self.id,))
            bytesQ=cur.fetchall()[0][0]
            bytesQ=str(bytesQ)
            cur.execute( "SELECT track.unitprice FROM track WHERE track.trackid=%s",(self.id,))
            unitPrice=cur.fetchall()[0][0]
            unitPrice=str(unitPrice)
            print(nombre)
            print(album)
            print(media)
            print(genre)
            print(compositor)
            print(milli)
            print(bytesQ)
            print(unitPrice)
            

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conexion is not None:
                conexion.close()
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
        self.nombreInput.setText(nombre)
        self.nombreInput.setGeometry(QtCore.QRect(140, 100, 161, 20))
        self.nombreInput.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(72, 72, 72);")
        self.nombreInput.setObjectName("nombreInput")
        self.tipoInput = QtWidgets.QLineEdit(Form)
        self.tipoInput.setText(media)
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
        self.modificarButton.clicked.connect(self.modificarAlbum)
        self.nombreLabel = QtWidgets.QLabel(Form)
        self.nombreLabel.setGeometry(QtCore.QRect(50, 100, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nombreLabel.setFont(font)
        self.nombreLabel.setObjectName("nombreLabel")
        self.precioInput = QtWidgets.QLineEdit(Form)
        self.precioInput.setText(unitPrice)
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
        self.albumInput.setText(album)
        self.albumInput.setGeometry(QtCore.QRect(140, 140, 161, 20))
        self.albumInput.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(72, 72, 72);")
        self.albumInput.setObjectName("albumInput")
        self.compositorInput = QtWidgets.QLineEdit(Form)
        self.compositorInput.setText(compositor)
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
        self.duracionInput.setText(milli)
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
        self.tamanoInput.setText(bytesQ)
        self.tamanoInput.setGeometry(QtCore.QRect(140, 340, 161, 20))
        self.tamanoInput.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(72, 72, 72);")
        self.tamanoInput.setObjectName("tamanoInput")
        self.generoInput = QtWidgets.QLineEdit(Form)
        self.generoInput.setText(genre)
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
        Form.setWindowTitle(_translate("Form", "Modificar cancion"))
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
            nombre=self.nombreInput.text()
            id=self.id
            tipo=self.tipoInput.text()
            precio=self.precioInput.text()
            album=self.albumInput.text()
            compositor=self.compositorInput.text()
            duracion=self.duracionInput.text()
            tamano=self.tamanoInput.text()
            genero=self.generoInput.text()

            cur.execute( "SELECT album.albumid FROM album WHERE album.title=%s",(album,))
            newAlbumtid=cur.fetchall()
            cur.execute( "SELECT mediatype.mediatypeid FROM mediatype WHERE mediatype.name=%s",(tipo,))
            newTipoid=cur.fetchall()
            cur.execute( "SELECT genre.genreid FROM genre WHERE genre.name=%s",(genero,))
            newGeneroid=cur.fetchall()
            if (len(newAlbumtid)==0):
                blank=QMessageBox()
                blank.setIcon(QMessageBox.Information)
                blank.setWindowTitle("ERROR")
                blank.setText("El album seleccionado no esta registrado.")
                blank.exec()
            elif (len(newTipoid)==0):
                blank=QMessageBox()
                blank.setIcon(QMessageBox.Information)
                blank.setWindowTitle("ERROR")
                blank.setText("El tipo seleccionado no esta registrado.")
                blank.exec()
            elif (len(newGeneroid)==0):
                blank=QMessageBox()
                blank.setIcon(QMessageBox.Information)
                blank.setWindowTitle("ERROR")
                blank.setText("El genero seleccionado no esta registrado.")
                blank.exec()

            else:
                newAlbumtid=newAlbumtid [0][0]
                newTipoid=newTipoid [0][0]
                newGeneroid=newGeneroid [0][0]
                #print(newArtistid)
                #nombreNewAlb="11 pm"
                cur.execute('''
                    UPDATE track
                    SET name = %s,
                    albumid=%s,
                    mediatypeid=%s,
                    genreid=%s,
                    composer=%s,
                    milliseconds=%s,
                    bytes=%s,
                    unitprice=%s
                    WHERE trackid = %s
                    ''',(nombre, newAlbumtid, newTipoid,newGeneroid,compositor,duracion,tamano, precio,id))
                conexion.commit()
                addedArtist=QMessageBox()
                addedArtist.setIcon(QMessageBox.Information)
                addedArtist.setWindowTitle("Listo")
                addedArtist.setText("Canción modificada exitosamente")
                addedArtist.exec()
                print("Lo edito")
            
            

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conexion is not None:
                conexion.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_ModificarCancion()
    ui.setupUi(Form)
    Form.show()
    Form.setWindowTitle("Modificar Cancion")
    sys.exit(app.exec_())
