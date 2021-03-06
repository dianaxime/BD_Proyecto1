# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eliminarArtista.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
import psycopg2
from config import config

class Ui_EliminarArtista(object):
    def __init__(self,id):
        self.id=id
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(331, 229)
        Form.setStyleSheet("background-color: rgb(85, 85, 255);\n"
"color: rgb(236, 236, 236);")
        Form.setWindowIcon(QIcon('icono.png'))
        self.nombreInput = QtWidgets.QLineEdit(Form)
        self.nombreInput.setGeometry(QtCore.QRect(130, 100, 161, 20))
        self.nombreInput.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(72, 72, 72);")
        self.nombreInput.setObjectName("nombreInput")
        self.eliminarArtistaLabel = QtWidgets.QLabel(Form)
        self.eliminarArtistaLabel.setGeometry(QtCore.QRect(90, 30, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.eliminarArtistaLabel.setFont(font)
        self.eliminarArtistaLabel.setObjectName("eliminarArtistaLabel")
        self.eliminarButton = QtWidgets.QPushButton(Form)
        self.eliminarButton.setGeometry(QtCore.QRect(100, 150, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.eliminarButton.setFont(font)
        self.eliminarButton.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(72, 72, 72);")
        self.eliminarButton.setObjectName("eliminarButton")
        self.nombreLabel = QtWidgets.QLabel(Form)
        self.nombreLabel.setGeometry(QtCore.QRect(40, 100, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nombreLabel.setFont(font)
        self.nombreLabel.setObjectName("nombreLabel")
        self.eliminarButton.clicked.connect(self.eliminarArtista)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Eliminar artista"))
        self.eliminarArtistaLabel.setText(_translate("Form", "Eliminar Artista"))
        self.eliminarButton.setText(_translate("Form", "Eliminar"))
        self.nombreLabel.setText(_translate("Form", "Nombre:"))

    def eliminarArtista(self):
        conexion=None
        try:
            params = config()

            #print(params)
            # Conexion al servidor de PostgreSQL
            #print('Conectando a la base de datos PostgreSQL...')
            conexion = psycopg2.connect(**params)

            # creación del cursor
            cur = conexion.cursor()

            # Ejecución la consulta para obtener la conexión
            print('La version de PostgreSQL es la:')
            cur.execute('SELECT version()')
            #print("hola1")
            # Se obtienen los resultados
            db_version = cur.fetchone()
            nombre=self.nombreInput.text()
            id=self.id
            if nombre != '':
                #Se verifica que exista ese artista
                cur.execute("SELECT artist.artistid FROM artist WHERE artist.name = '{0}'".format(nombre))
                IDArtist=cur.fetchall()
                if(len(IDArtist)!=0):
                    #Si si existe se obtine el ID y se borra 
                    #print("hola2")
                    IDoficial=(IDArtist[0][0])
                    cur.execute("DELETE FROM creador_track WHERE creador_track.trackid IN (SELECT track.trackid FROM track WHERE track.albumid IN (SELECT album.albumid FROM album WHERE album.artistid = %s))",(IDoficial,))
                    cur.execute("DELETE FROM playlisttrack WHERE playlisttrack.trackid IN (SELECT track.trackid FROM track WHERE track.albumid IN (SELECT album.albumid FROM album WHERE album.artistid = %s))",(IDoficial,))
                    cur.execute("DELETE FROM invoiceline WHERE invoiceline.trackid IN (SELECT track.trackid FROM track WHERE track.albumid IN (SELECT album.albumid FROM album WHERE album.artistid = %s))",(IDoficial,))
                    cur.execute("DELETE FROM actividad_track WHERE actividad_track.trackid IN (SELECT track.trackid FROM track WHERE track.albumid IN (SELECT album.albumid FROM album WHERE album.artistid = %s))",(IDoficial,))
                    ##agregar canciones de artisya eliminado
                    #cur.execute("SELECT track.name FROM track WHERE track.albumid IN (SELECT album.albumid FROM album WHERE album.artistid = %s)",(IDoficial,))
                    #tracks=cur.fetchall()
                    #for a in tracks :
                      #  print (a[0])
                       # cur.execute("""SELECT add_bitacora(%s::numeric, %s::varchar, 3::numeric, 1::numeric ) """, (id, a[0])) 
                    #print("hola3")
                    cur.execute("""UPDATE track set u_deleted=%s, u_updated=%s WHERE track.albumid IN (SELECT album.albumid FROM album WHERE album.artistid = %s)""", (id, id, IDoficial,))
                    cur.execute("DELETE FROM track WHERE track.albumid IN (SELECT album.albumid FROM album WHERE album.artistid = %s)",(IDoficial,))
                    #print("hola1")
                    ##agregar a bitacora albums eliminados de artista
                    #cur.execute("SELECT album.title FROM album WHERE album.artistid = '{0}'".format(IDoficial))
                    #albums=cur.fetchall()
                    #for a in albums :
                      #  print (a[0])
                       # cur.execute("""SELECT add_bitacora(%s::numeric, %s::varchar, 3::numeric, 2::numeric ) """, (id, a[0])) 
                    cur.execute("""UPDATE album set u_deleted=%s, u_updated=%s WHERE album.artistid = %s""", (id, id,IDoficial,))
                    cur.execute("DELETE FROM album WHERE album.artistid = '{0}'".format(IDoficial))
                    ##agregar a bitacora artista eliminado
                    #print("hola2")
                    cur.execute("""UPDATE artist set u_deleted=%s, u_updated=%s where artistid=%s""", (id, id, IDoficial,))
                    #print("hola3")
                    #conexion.commit()
                    cur.execute("DELETE FROM artist WHERE artist.artistid = '{0}'".format(IDoficial,))
                    #print("hola4")
                    conexion.commit()
                    cur.execute("SELECT * FROM artist ORDER BY artist.artistid ASC LIMIT 10")
                    # Recorremos los resultados y los mostramos
                    """for a,b in cur.fetchall() :
                            print(a,b)
                    print("--------------------------------------------------")"""
                    addedSong=QMessageBox()
                    addedSong.setIcon(QMessageBox.Information)
                    addedSong.setWindowTitle("Listo")
                    addedSong.setText("Artista eliminado exitosamente")
                    addedSong.exec()
                else:
                    #Sino existe se muestra error
                    blank=QMessageBox()
                    blank.setIcon(QMessageBox.Information)
                    blank.setWindowTitle("ERROR")
                    blank.setText("Ese artista no existe en la base de datos")
                    blank.exec()                      
            else:
                blank=QMessageBox()
                blank.setIcon(QMessageBox.Information)
                blank.setWindowTitle("INCOMPLETO")
                blank.setText("Por favor ingresa el nombre del artista a borrar")
                blank.exec()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conexion is not None:
                conexion.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_EliminarArtista()
    ui.setupUi(Form)
    Form.show()
    Form.setWindowTitle("Eliminar Artista")
    sys.exit(app.exec_())
