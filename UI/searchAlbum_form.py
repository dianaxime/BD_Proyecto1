# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'searchAlbum_form.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem
import psycopg2
from config import config


class Ui_searchAlbum_form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 368)
        Form.setStyleSheet("background-color: rgb(85, 85, 255);")
        Form.setWindowIcon(QIcon('icono.png'))
        self.titleForm = QtWidgets.QLabel(Form)
        self.titleForm.setGeometry(QtCore.QRect(250, 20, 141, 21))
        self.titleForm.setStyleSheet("color: rgb(236, 236, 236);")
        self.titleForm.setObjectName("titleForm")
        self.inputAlbum = QtWidgets.QLineEdit(Form)
        self.inputAlbum.setGeometry(QtCore.QRect(90, 70, 161, 21))
        self.inputAlbum.setStyleSheet("color: rgb(72, 72, 72);\n"
"background-color: rgb(243, 243, 243);")
        self.inputAlbum.setObjectName("inputAlbum")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 70, 41, 16))
        self.label_2.setObjectName("label_2")
        self.buscarBoton = QtWidgets.QPushButton(Form)
        self.buscarBoton.setGeometry(QtCore.QRect(280, 70, 51, 23))
        self.buscarBoton.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(72, 72, 72);")
        self.buscarBoton.setObjectName("buscarBoton")
        self.buscarBoton.clicked.connect(self.buscarAlbum)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(40, 120, 502, 211))
        self.tableWidget.setStyleSheet("background-color: rgb(234, 234, 234);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnWidth(0, 167)
        self.tableWidget.setColumnWidth(1, 167)
        self.tableWidget.setColumnWidth(2, 167)
        nombreColumnas = ("Artist", "Album", "Track")
        # Establecer las etiquetas de encabezado horizontal usando etiquetas
        self.tableWidget.setHorizontalHeaderLabels(nombreColumnas)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Buscar Album"))
        self.titleForm.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Buscar Album</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:9pt; color:#ffffff;\">Album:</span></p></body></html>"))
        self.buscarBoton.setText(_translate("Form", "Buscar"))

    def buscarAlbum(self):
        #Buscar track
        nombreAlbum=self.inputAlbum.text()
        conexion = None
        try:
            # Lectura de los parámetros de conexion
            params = config()

            #print(params)
            # Conexion al servidor de PostgreSQL
            print('Conectando a la base de datos PostgreSQL...')
            conexion = psycopg2.connect(**params)

            # creación del cursor
            cur = conexion.cursor()

            # Ejecución la consulta para obtener la conexión
            print('La version de PostgreSQL es la:')
            cur.execute('SELECT version()')

            # Se obtienen los resultados
            db_version = cur.fetchone()
            # Se muestra la versión por pantalla
            print(db_version)
    
            if nombreAlbum != '' :
                cur.execute( "SELECT album.title FROM album WHERE album.title=%s",(nombreAlbum,))
                IDalbumO=cur.fetchall()#[0][0]
                if (len(IDalbumO)==0):
                    blank=QMessageBox()
                    blank.setIcon(QMessageBox.Information)
                    blank.setWindowTitle("ERROR")
                    blank.setText("El album no esta registrado")
                    blank.exec()
                else:
                    cur.execute("""
                        SELECT artist.name, album.title, track.name
                        FROM album 
                            JOIN artist ON artist.artistid = album.artistid
                            JOIN track ON track.albumid = album.albumid
                        WHERE album.title = %s
                        """,(nombreAlbum,))

                    row = 0
                    for a,b,c in cur.fetchall():
                        self.tableWidget.setRowCount(row + 1)
                        self.tableWidget.setItem(row, 0, QTableWidgetItem(a))
                        self.tableWidget.setItem(row, 1, QTableWidgetItem(b))
                        self.tableWidget.setItem(row, 2, QTableWidgetItem(c))
                        row += 1
                    cur.close()                
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
                print('Conexión finalizada.')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_searchAlbum_form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
