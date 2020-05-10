# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ingresarAlbum.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
import psycopg2
from config import config

class Ui_IngresarAlbum(object):
    def __init__(self,id):
        self.id=id
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(335, 252)
        Form.setStyleSheet("background-color: rgb(85, 85, 255);\n"
"color: rgb(236, 236, 236);")
        Form.setWindowIcon(QIcon('icono.png'))
        self.nombreLabel = QtWidgets.QLabel(Form)
        self.nombreLabel.setGeometry(QtCore.QRect(40, 90, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nombreLabel.setFont(font)
        self.nombreLabel.setObjectName("nombreLabel")
        self.tituloInput = QtWidgets.QLineEdit(Form)
        self.tituloInput.setGeometry(QtCore.QRect(130, 90, 161, 20))
        self.tituloInput.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(72, 72, 72);")
        self.tituloInput.setObjectName("tituloInput")
        self.ingresarAlbumLabel = QtWidgets.QLabel(Form)
        self.ingresarAlbumLabel.setGeometry(QtCore.QRect(90, 20, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.ingresarAlbumLabel.setFont(font)
        self.ingresarAlbumLabel.setObjectName("ingresarAlbumLabel")
        self.ingresarButton = QtWidgets.QPushButton(Form)
        self.ingresarButton.setGeometry(QtCore.QRect(100, 180, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ingresarButton.setFont(font)
        self.ingresarButton.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(72, 72, 72);")
        self.ingresarButton.setObjectName("ingresarButton")
        self.artistaLabel = QtWidgets.QLabel(Form)
        self.artistaLabel.setGeometry(QtCore.QRect(40, 140, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.artistaLabel.setFont(font)
        self.artistaLabel.setObjectName("artistaLabel")
        self.artistaInput = QtWidgets.QLineEdit(Form)
        self.artistaInput.setGeometry(QtCore.QRect(130, 140, 161, 20))
        self.artistaInput.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(72, 72, 72);")
        self.artistaInput.setObjectName("artistaInput")
        self.ingresarButton.clicked.connect(self.agregarAlbum)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ingresar album"))
        self.nombreLabel.setText(_translate("Form", "Título:"))
        self.ingresarAlbumLabel.setText(_translate("Form", "Ingresar Álbum"))
        self.ingresarButton.setText(_translate("Form", "Ingresar"))
        self.artistaLabel.setText(_translate("Form", "Artista:"))

    def agregarAlbum(self):
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

            # Se obtienen los resultados
            db_version = cur.fetchone()
            albumName=self.tituloInput.text()
            artistName=self.artistaInput.text()
            id=self.id
            if (albumName != '' or artistName != ''):
                #Se verifica si ya existe ese album de ese artista o ese artista
                cur.execute( "SELECT * FROM album WHERE album.title=%s AND album.artistid IN (SELECT artist.artistid FROM artist WHERE artist.name = %s)",(albumName, artistName,))
                IDAlbum=cur.fetchall()
                cur.execute( "SELECT artist.artistid FROM artist WHERE artist.name = %s",(artistName,))
                IDArtist=cur.fetchall()
                if (len(IDAlbum)==0 and len(IDArtist)!=0):
                    #Si existe ese artista, pero no existe ese album, se crea su ID y se agrega
                    cur.execute( "SELECT MAX(album.albumid) FROM album")
                    IDAlbum=cur.fetchall()
                    IDoficial=(IDAlbum[0][0])
                    IDoficial += 1
                    IDoficialArtista=(IDArtist[0][0])
                    cur.execute("INSERT INTO album (albumid, title, artistid) VALUES (%s,%s,%s)", (IDoficial, albumName, IDoficialArtista))
                    cur.execute("""SELECT add_bitacora(%s::numeric, %s::varchar, 1::numeric, 2::numeric )""", (id, albumName))
                    conexion.commit()
                    cur.execute("SELECT * FROM album ORDER BY album.albumid DESC LIMIT 5")
                    # Recorremos los resultados y los mostramos
                    for a,b,c in cur.fetchall() :
                        print(a,b,c)
                    print("--------------------------------------------------")
                    addedArtist=QMessageBox()
                    addedArtist.setIcon(QMessageBox.Information)
                    addedArtist.setWindowTitle("Listo")
                    addedArtist.setText("Album agregado exitosamente")
                    addedArtist.exec()
                else:
                    blank=QMessageBox()
                    blank.setIcon(QMessageBox.Information)
                    blank.setWindowTitle("ERROR")
                    blank.setText("Ese album ya existe o el artista no se encuentra en la base de datos")
                    blank.exec()
            else:
                blank=QMessageBox()
                blank.setIcon(QMessageBox.Information)
                blank.setWindowTitle("INCOMPLETO")
                blank.setText("Por favor llene todos los campos")
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
    ui = Ui_IngresarAlbum()
    ui.setupUi(Form)
    Form.show()
    Form.setWindowTitle("Ingresar Album")
    sys.exit(app.exec_())
