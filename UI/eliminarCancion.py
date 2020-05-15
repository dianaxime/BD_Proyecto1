# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eliminarCancion.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
import psycopg2
from config import config


class Ui_EliminarCancion(object):
    def __init__(self,id):
        self.id=id
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(337, 230)
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
        self.eliminarButton.clicked.connect(self.eliminarCancion)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Eliminar cancion"))
        self.nombreLabel.setText(_translate("Form", "Nombre:"))
        self.eliminarCancionLabel.setText(_translate("Form", "Eliminar Canción"))
        self.eliminarButton.setText(_translate("Form", "Eliminar"))

    def eliminarCancion(self):
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
            id=self.id
            if nombre != '':
                #Se verifica que exista esa cancion
                cur.execute("SELECT track.trackid FROM track WHERE track.name = '{0}'".format(nombre))
                IDTrack=cur.fetchall()
                if(len(IDTrack)!=0):
                    #Si si existe se borra
                    IDoficial=(IDTrack[0][0])

                    cur.execute("DELETE FROM creador_track WHERE creador_track.trackid = %s",(IDoficial,))
                    cur.execute("DELETE FROM playlisttrack WHERE playlisttrack.trackid = %s",(IDoficial,))
                    cur.execute("DELETE FROM actividad_track WHERE actividad_track.trackid = %s",(IDoficial,))
                    cur.execute("DELETE FROM invoiceline WHERE invoiceline.trackid = %s",(IDoficial,))
                    cur.execute("DELETE FROM creador_track WHERE creador_track.trackid = %s",(IDoficial,))
                    cur.execute("""UPDATE track set u_deleted=%s, u_updated=%s WHERE track.trackid = %s""", (id,id,IDoficial))
                    cur.execute("DELETE FROM track WHERE track.trackid = %s",(IDoficial,))
                    #cur.execute("""SELECT add_bitacora(%s::numeric, %s::varchar, 3::numeric, 1::numeric )""", (id, nombre))
                    conexion.commit()
                    """cur.execute("SELECT * FROM track ORDER BY track.trackid DESC LIMIT 10")
                    # Recorremos los resultados y los mostramos
                    for a,b,c,d,e,f,g,h,i in cur.fetchall() :
                            print(a,b,c,d,e,f,g,h,i)

                    print("--------------------------------------------------")"""
                    addedSong=QMessageBox()
                    addedSong.setIcon(QMessageBox.Information)
                    addedSong.setWindowTitle("Listo")
                    addedSong.setText("Cancion eliminada exitosamente")
                    addedSong.exec()
                else:
                    #Sino existe se muestra error
                    blank=QMessageBox()
                    blank.setIcon(QMessageBox.Information)
                    blank.setWindowTitle("ERROR")
                    blank.setText("Esa cancion no existe en la base de datos")
                    blank.exec()                      
            else:
                blank=QMessageBox()
                blank.setIcon(QMessageBox.Information)
                blank.setWindowTitle("INCOMPLETO")
                blank.setText("Por favor ingresa el nombre de la cancion a borrar")
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
    ui = Ui_EliminarCancion()
    ui.setupUi(Form)
    Form.show()
    Form.setWindowTitle("Eliminar Cancion")
    sys.exit(app.exec_())
