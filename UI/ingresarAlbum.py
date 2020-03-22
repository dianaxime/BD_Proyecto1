# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ingresarAlbum.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon


class Ui_IngresarAlbum(object):
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

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
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
            nombreAlbum=self.tituloInput.text()
            nombreArtista=self.artistaInput.text()

            if nombre != '':
                #Se verifica si ya existe ese artista
                cur.execute( "SELECT artist.artistid FROM artist WHERE artist.name=%s",(nombre,))
                IDArtist=cur.fetchall()
                if (len(IDArtist)==0):
                    #Si no existe se crea su ID y se agrega
                    cur.execute( "SELECT MAX(artist.artistid) FROM artist" )
                    IDArtist=cur.fetchall()
                    IDoficial=(IDArtist[0][0])
                    IDoficial += 1
                    cur.execute("INSERT INTO artist (artistid, name)VALUES (%s, %s)", ( IDoficial, nombre))
                    conexion.commit()
                    cur.execute("SELECT * FROM artist ORDER BY artist.artistid DESC LIMIT 10")
                    # Recorremos los resultados y los mostramos
                    for a,b in cur.fetchall() :
                        print(a,b)
                    print("--------------------------------------------------")
                    addedArtist=QMessageBox()
                    addedArtist.setIcon(QMessageBox.Information)
                    addedArtist.setWindowTitle("Listo")
                    addedArtist.setText("Artista agregado")
                    addedArtist.exec()
                else:
                    blank=QMessageBox()
                    blank.setIcon(QMessageBox.Information)
                    blank.setWindowTitle("ERROR")
                    blank.setText("Ese artista ya existe en la Base de Datos")
                    blank.exec()
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

        ##Lo de prueba
        
        cur.execute( "SELECT MAX(album.albumid) FROM album" )
        idAlbum=cur.fetchall()
        idAlbum=idAlbum[0][0]
        idAlbum+=1
        cur.execute( "SELECT artist.artistid FROM artist WHERE artist.name=%s",(nombreArtistAlbum,) )
        IDArtistAlbum=cur.fetchall()
        IDArtistAlbum=IDArtistAlbum[0][0]
        postgres_insert_query="""INSERT INTO album (albumid, title, artistid) VALUES (%s,%s,%s)"""
        record_to_insert=(idAlbum, nombreAlbum,IDArtistAlbum)
        ##cur.execute(postgres_insert_query, record_to_insert)
        cur.execute("INSERT INTO album (albumid, title, artistid) VALUES (%s,%s,%s)", (idAlbum, nombreAlbum,IDArtistAlbum))
        #conexion.commit()
        cur.execute("SELECT * FROM album")
        # Recorremos los resultados y los mostramos
        for a,b,c in cur.fetchall() :
            print(a,b,c)

        print("--------------------------------------------------")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_IngresarAlbum()
    ui.setupUi(Form)
    Form.show()
    Form.setWindowTitle("Ingresar Album")
    sys.exit(app.exec_())
