# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ingresarCancion.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
import psycopg2
from config import config


class Ui_IngresarCancion(object):
    def __init__(self,id):
        self.id=id
    """def __init__(self,id):
        self.id=id
        print("este es el id del registrador "+str(id))"""
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(353, 525)
        Form.setStyleSheet("background-color: rgb(85, 85, 255);\n"
"color: rgb(236, 236, 236);")
        Form.setWindowIcon(QIcon('icono.png'))
        self.ingresarCancionLabel = QtWidgets.QLabel(Form)
        self.ingresarCancionLabel.setGeometry(QtCore.QRect(100, 30, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.ingresarCancionLabel.setFont(font)
        self.ingresarCancionLabel.setObjectName("ingresarCancionLabel")
        self.nombreLabel = QtWidgets.QLabel(Form)
        self.nombreLabel.setGeometry(QtCore.QRect(50, 100, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nombreLabel.setFont(font)
        self.nombreLabel.setObjectName("nombreLabel")
        self.albumLabel = QtWidgets.QLabel(Form)
        self.albumLabel.setGeometry(QtCore.QRect(50, 140, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.albumLabel.setFont(font)
        self.albumLabel.setObjectName("albumLabel")
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
        self.compositorLabel = QtWidgets.QLabel(Form)
        self.compositorLabel.setGeometry(QtCore.QRect(50, 260, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.compositorLabel.setFont(font)
        self.compositorLabel.setObjectName("compositorLabel")
        self.duracionLabel = QtWidgets.QLabel(Form)
        self.duracionLabel.setGeometry(QtCore.QRect(50, 300, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.duracionLabel.setFont(font)
        self.duracionLabel.setObjectName("duracionLabel")
        self.tamanoLabel = QtWidgets.QLabel(Form)
        self.tamanoLabel.setGeometry(QtCore.QRect(50, 340, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tamanoLabel.setFont(font)
        self.tamanoLabel.setObjectName("tamanoLabel")
        self.precioLabel = QtWidgets.QLabel(Form)
        self.precioLabel.setGeometry(QtCore.QRect(50, 380, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.precioLabel.setFont(font)
        self.precioLabel.setObjectName("precioLabel")
        self.nombreInput = QtWidgets.QLineEdit(Form)
        self.nombreInput.setGeometry(QtCore.QRect(140, 100, 161, 20))
        self.nombreInput.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(72, 72, 72);")
        self.nombreInput.setObjectName("nombreInput")
        self.albumInput = QtWidgets.QLineEdit(Form)
        self.albumInput.setGeometry(QtCore.QRect(140, 140, 161, 20))
        self.albumInput.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(72, 72, 72);")
        self.albumInput.setObjectName("albumInput")
        self.tipoInput = QtWidgets.QLineEdit(Form)
        self.tipoInput.setGeometry(QtCore.QRect(140, 180, 161, 20))
        self.tipoInput.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(72, 72, 72);")
        self.tipoInput.setObjectName("tipoInput")
        self.generoInput = QtWidgets.QLineEdit(Form)
        self.generoInput.setGeometry(QtCore.QRect(140, 220, 161, 20))
        self.generoInput.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(72, 72, 72);")
        self.generoInput.setObjectName("generoInput")
        self.compositorInput = QtWidgets.QLineEdit(Form)
        self.compositorInput.setGeometry(QtCore.QRect(140, 260, 161, 20))
        self.compositorInput.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(72, 72, 72);")
        self.compositorInput.setObjectName("compositorInput")
        self.duracionInput = QtWidgets.QLineEdit(Form)
        self.duracionInput.setGeometry(QtCore.QRect(140, 300, 161, 20))
        self.duracionInput.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(72, 72, 72);")
        self.duracionInput.setObjectName("duracionInput")
        self.tamanoInput = QtWidgets.QLineEdit(Form)
        self.tamanoInput.setGeometry(QtCore.QRect(140, 340, 161, 20))
        self.tamanoInput.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(72, 72, 72);")
        self.tamanoInput.setObjectName("tamanoInput")
        self.precioInput = QtWidgets.QLineEdit(Form)
        self.precioInput.setGeometry(QtCore.QRect(140, 380, 161, 20))
        self.precioInput.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(72, 72, 72);")
        self.precioInput.setObjectName("precioInput")
        #LINK A YOUTUBE
        self.youtubeLabel = QtWidgets.QLabel(Form)
        self.youtubeLabel.setGeometry(QtCore.QRect(50, 420, 90, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.youtubeLabel.setFont(font)
        self.youtubeLabel.setObjectName("youtubeLabel")
        self.youtubeInput = QtWidgets.QLineEdit(Form)
        self.youtubeInput.setGeometry(QtCore.QRect(140, 420, 161, 20))
        self.youtubeInput.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(72, 72, 72);")
        self.youtubeInput.setObjectName("youtubeInput")

        self.ingresarButton = QtWidgets.QPushButton(Form)
        self.ingresarButton.setGeometry(QtCore.QRect(120, 460, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ingresarButton.setFont(font)
        self.ingresarButton.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(72, 72, 72);")
        self.ingresarButton.setObjectName("ingresarButton")
        self.ingresarButton.clicked.connect(self.agregarCancion)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ingresar cancion"))
        self.ingresarCancionLabel.setText(_translate("Form", "Ingresar Canción"))
        self.nombreLabel.setText(_translate("Form", "Nombre:"))
        self.albumLabel.setText(_translate("Form", "Álbum:"))
        self.tipoLabel.setText(_translate("Form", "Tipo:"))
        self.generoLabel.setText(_translate("Form", "Género:"))
        self.compositorLabel.setText(_translate("Form", "Compositor:"))
        self.duracionLabel.setText(_translate("Form", "Duración:"))
        self.tamanoLabel.setText(_translate("Form", "Tamaño:"))
        self.precioLabel.setText(_translate("Form", "Precio:"))
        self.precioLabel.setText(_translate("Form", "Precio:"))
        self.youtubeLabel.setText(_translate("Form", "Youtube Link:"))
        self.ingresarButton.setText(_translate("Form", "Ingresar"))

    def agregarCancion(self):
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
            idRegistrador=self.id
            # Se obtienen los resultados
            db_version = cur.fetchone()
            nombre=self.nombreInput.text()
            album=self.albumInput.text()
            tipo=self.tipoInput.text()
            genero=self.generoInput.text()
            compositor=self.compositorInput.text()
            duracion=self.duracionInput.text()
            size=self.tamanoInput.text()
            precio=self.precioInput.text()
            link=self.youtubeInput.text()
            #id=self.id
            if nombre != '' or album != '' or tipo != '' or genero != '' or compositor != '' or duracion != '' or size != '' or precio != '' or link!= '':
                #Se selecciona el ID mayor y se crea el nuevo
                cur.execute( "SELECT MAX(track.trackid) FROM track" )
                IDTrack=cur.fetchall()
                IDoficial=(IDTrack[0][0])
                IDoficial += 1
                print(IDoficial)
                cur.execute( "SELECT MAX(creador_track.relacionid) FROM creador_track" )
                IDrelacion=cur.fetchall()
                IDoficialRel=(IDrelacion[0][0])
                IDoficialRel += 1
                #Se selecciona busca el ID del album ingresado
                cur.execute( "SELECT album.albumid FROM album WHERE album.title=%s",(album,))
                IDAlbum=cur.fetchall()
                cur.execute( "SELECT mediatype.mediatypeid FROM mediatype WHERE mediatype.name=%s",(tipo,))
                IDMediaType=cur.fetchall()
                cur.execute( "SELECT genre.genreid FROM genre WHERE genre.name=%s",(genero,))
                IDGenre=cur.fetchall()
                if (len(IDAlbum)==0):
                    blank=QMessageBox()
                    blank.setIcon(QMessageBox.Information)
                    blank.setWindowTitle("ERROR")
                    blank.setText("El campo de album no es válido")
                    blank.exec()
                elif (len(IDMediaType)==0):
                    blank=QMessageBox()
                    blank.setIcon(QMessageBox.Information)
                    blank.setWindowTitle("ERROR")
                    blank.setText("El campo de tipo de media no es válido")
                    blank.exec()
                elif (len(IDGenre)==0):
                    blank=QMessageBox()
                    blank.setIcon(QMessageBox.Information)
                    blank.setWindowTitle("ERROR")
                    blank.setText("El campo de género no es válido")
                    blank.exec()
                else:
                    IDAlbumOficial=(IDAlbum[0][0])
                    print(IDAlbum)
                    #Se selecciona busca el ID del tipo ingresado
                    
                    
                    print(IDMediaType)
                    IDMediaTypeOficial=(IDMediaType[0][0])
                    #Se selecciona busca el ID del genero ingresado
                    
                    
                    IDGenreOficial=(IDGenre[0][0])
                    #Se agrega a la DB
                    #cur.execute("""SELECT add_bitacora(%s::numeric, %s::varchar, 1::numeric, 1::numeric )""", (idRegistrador, nombre))
                    cur.execute("INSERT INTO track (trackid, name, albumid, mediatypeid, genreid, composer, milliseconds, bytes, unitprice, u_added, link_video) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", ( IDoficial, nombre, IDAlbumOficial, IDMediaTypeOficial, IDGenreOficial, compositor, duracion, size, precio, idRegistrador, link))
                    cur.execute("INSERT INTO actividad_track (actividadid, esta_activo, trackid) VALUES (%s, %s, %s)", (IDoficial, False, IDoficial,))
                    cur.execute("INSERT INTO creador_track (relacionid, creadorid, trackid) VALUES (%s, %s, %s)", (IDoficialRel, idRegistrador, IDoficial,))
                    conexion.commit()
                    """cur.execute("SELECT * FROM track ORDER BY track.trackid DESC LIMIT 10")
                    # Recorremos los resultados y los mostramos
                    for a,b,c,d,e,f,g,h,i,j in cur.fetchall() :
                            print(a,b,c,d,e,f,g,h,i,j)

                    print("--------------------------------------------------")"""
                    addedSong=QMessageBox()
                    addedSong.setIcon(QMessageBox.Information)
                    addedSong.setWindowTitle("Listo")
                    addedSong.setText("Cancion agregada")
                    addedSong.exec()
                    cur.execute("SELECT * FROM track")
                """canciones=cur.fetchall()
                n=1
                for i in canciones:
                        print (i[0])
                        cur.execute("INSERT INTO actividad_track (actividadid, esta_activo, trackid) VALUES (%s, %s, %s)", (n, True, i[0],))
                        n+=1"""
                        

            else:
                blank=QMessageBox()
                blank.setIcon(QMessageBox.Information)
                blank.setWindowTitle("INCOMPLETO")
                blank.setText("Por favor llene los campos")
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
    ui = Ui_IngresarCancion()
    ui.setupUi(Form)
    Form.show()
    Form.setWindowTitle("Ingresar Cancion")
    sys.exit(app.exec_())
