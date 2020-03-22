# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inactivarCancion.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
import psycopg2
from config import config


class Ui_InactivarCancion(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(344, 229)
        Form.setStyleSheet("background-color: rgb(85, 85, 255);\n"
"color: rgb(236, 236, 236);")
        Form.setWindowIcon(QIcon('icono.png'))
        self.buscarLabel = QtWidgets.QLabel(Form)
        self.buscarLabel.setGeometry(QtCore.QRect(50, 30, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.buscarLabel.setFont(font)
        self.buscarLabel.setObjectName("buscarLabel")
        self.nombreInput = QtWidgets.QLineEdit(Form)
        self.nombreInput.setGeometry(QtCore.QRect(140, 100, 161, 20))
        self.nombreInput.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(72, 72, 72);")
        self.nombreInput.setObjectName("nombreInput")
        self.continuarButton = QtWidgets.QPushButton(Form)
        self.continuarButton.setGeometry(QtCore.QRect(110, 150, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.continuarButton.setFont(font)
        self.continuarButton.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(72, 72, 72);")
        self.continuarButton.setObjectName("continuarButton")
        self.nombreLabel = QtWidgets.QLabel(Form)
        self.nombreLabel.setGeometry(QtCore.QRect(50, 100, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nombreLabel.setFont(font)
        self.nombreLabel.setObjectName("nombreLabel")
        self.continuarButton.clicked.connect(self.inactivarTrack)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.buscarLabel.setText(_translate("Form", "Ingrese canción a inactivar:"))
        self.continuarButton.setText(_translate("Form", "Inactivar"))
        self.nombreLabel.setText(_translate("Form", "Nombre:"))

    def inactivarTrack(self):
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
                #Se verifica que exista ese track
                cur.execute("SELECT actividad_track.trackid FROM actividad_track WHERE actividad_track.trackid IN (SELECT track.trackid FROM track WHERE track.name = %s)",(nombre,))
                IDTrack=cur.fetchall()
                if(len(IDTrack)!=0):
                    #Si si existe se obtine el ID y adquiere su estado
                    IDoficial=(IDTrack[0][0])
                    cur.execute("SELECT actividad_track.esta_activo FROM actividad_track WHERE actividad_track.trackid = %s",(IDoficial,))
                    estado=cur.fetchall()
                    actualState=(estado[0][0])
                    if(actualState==True):
                        #Si esta activada se desactiva el track
                        cur.execute("UPDATE actividad_track SET esta_activo = False WHERE actividadid = %s",(IDoficial,))
                        conexion.commit()
                        cur.execute("SELECT * FROM actividad_track ORDER BY actividad_track.trackid ASC LIMIT 10")
                        for a,b,c in cur.fetchall() :
                            print(a,b,c)
                        print("--------------------------------------------------")
                        actSong=QMessageBox()
                        actSong.setIcon(QMessageBox.Information)
                        actSong.setWindowTitle("Listo")
                        actSong.setText("Track desactivada")
                        actSong.exec()
                    else:
                        #Si esta desactivda se activa el track
                        newState = True
                        cur.execute("UPDATE actividad_track SET esta_activo = True WHERE actividadid = %s",(IDoficial,))
                        conexion.commit()
                        cur.execute("SELECT * FROM actividad_track ORDER BY actividad_track.trackid ASC LIMIT 10")
                        for a,b,c in cur.fetchall() :
                            print(a,b,c)
                        print("--------------------------------------------------")
                        actSong=QMessageBox()
                        actSong.setIcon(QMessageBox.Information)
                        actSong.setWindowTitle("Listo")
                        actSong.setText("Track activada")
                        actSong.exec()
                else:
                    #Sino existe se muestra error
                    blank=QMessageBox()
                    blank.setIcon(QMessageBox.Information)
                    blank.setWindowTitle("ERROR")
                    blank.setText("Ese track no existe en la base de datos")
                    blank.exec()                      
            else:
                blank=QMessageBox()
                blank.setIcon(QMessageBox.Information)
                blank.setWindowTitle("INCOMPLETO")
                blank.setText("Por favor ingresa el nombre del track a desactivar/Activar")
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
    ui = Ui_InactivarCancion()
    ui.setupUi(Form)
    Form.show()
    Form.setWindowTitle("Inactivar Cancion")
    sys.exit(app.exec_())
