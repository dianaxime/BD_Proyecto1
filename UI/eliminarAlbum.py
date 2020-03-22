# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eliminarAlbum.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
import psycopg2
from config import config


class Ui_EliminarAlbum(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(339, 230)
        Form.setStyleSheet("background-color: rgb(85, 85, 255);\n"
"color: rgb(236, 236, 236);")
        Form.setWindowIcon(QIcon('icono.png'))
        self.nombreLabel = QtWidgets.QLabel(Form)
        self.nombreLabel.setGeometry(QtCore.QRect(40, 100, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nombreLabel.setFont(font)
        self.nombreLabel.setObjectName("nombreLabel")
        self.eliminarCancionLabel = QtWidgets.QLabel(Form)
        self.eliminarCancionLabel.setGeometry(QtCore.QRect(90, 30, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.eliminarCancionLabel.setFont(font)
        self.eliminarCancionLabel.setObjectName("eliminarCancionLabel")
        self.nombreInput = QtWidgets.QLineEdit(Form)
        self.nombreInput.setGeometry(QtCore.QRect(130, 100, 161, 20))
        self.nombreInput.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(72, 72, 72);")
        self.nombreInput.setObjectName("nombreInput")
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
        self.eliminarButton.clicked.connect(self.eliminarAlbum)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.nombreLabel.setText(_translate("Form", "Nombre:"))
        self.eliminarCancionLabel.setText(_translate("Form", "Eliminar Álbum"))
        self.eliminarButton.setText(_translate("Form", "Eliminar"))

    def eliminarAlbum(self):
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
            nombre=self.nombreInput.text()

            if nombre != '':
                #Se verifica que exista ese album
                cur.execute("SELECT album.albumid FROM album WHERE album.title = '{0}'".format(nombre))
                IDAlbum=cur.fetchall()
                if(len(IDAlbum)!=0):
                    #Si si existe se obtine el ID y se borra 
                    IDoficial=(IDAlbum[0][0])
                    cur.execute("DELETE FROM playlisttrack WHERE playlisttrack.trackid IN (SELECT track.trackid FROM track WHERE track.albumid = %s)",(IDoficial,))
                    cur.execute("DELETE FROM invoiceline WHERE invoiceline.trackid IN (SELECT track.trackid FROM track WHERE track.albumid = %s)",(IDoficial,))
                    cur.execute("DELETE FROM actividad_track WHERE actividad_track.trackid IN (SELECT track.trackid FROM track WHERE track.albumid = %s)",(IDoficial,))
                    cur.execute("DELETE FROM track WHERE track.albumid = %s",(IDoficial,))
                    cur.execute("DELETE FROM album WHERE album.title = '{0}'".format(nombre))
                    conexion.commit()
                    cur.execute("SELECT * FROM album ORDER BY album.albumid ASC LIMIT 10")
                    # Recorremos los resultados y los mostramos
                    for a,b,c in cur.fetchall() :
                            print(a,b,c)
                    print("--------------------------------------------------")
                    addedSong=QMessageBox()
                    addedSong.setIcon(QMessageBox.Information)
                    addedSong.setWindowTitle("Listo")
                    addedSong.setText("Album eliminado exitosamente")
                    addedSong.exec()
                else:
                    #Sino existe se muestra error
                    blank=QMessageBox()
                    blank.setIcon(QMessageBox.Information)
                    blank.setWindowTitle("ERROR")
                    blank.setText("Ese album no existe en la base de datos")
                    blank.exec()                      
            else:
                blank=QMessageBox()
                blank.setIcon(QMessageBox.Information)
                blank.setWindowTitle("INCOMPLETO")
                blank.setText("Por favor ingresa el nombre del album a borrar")
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
    ui = Ui_EliminarAlbum()
    ui.setupUi(Form)
    Form.show()
    Form.setWindowTitle("Eliminar Album")
    sys.exit(app.exec_())
