# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'misCanciones.ui'
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

class Ui_MisCanciones(object):
    def __init__(self,id):
        self.id=id

    def conectar(self):
        #Buscar track
        self.tableWidget.setRowCount(0)
        id=self.id
        #nombreTrack=self.inputTrack.text()
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
            print(id)
            row=0
            cur.execute( """SELECT track.name, album.title , genre.name, artist.name, track.link_video from track 
                JOIN invoiceline on invoiceline.trackid=track.trackid
                JOIN invoice on invoiceline.invoiceid=invoice.invoiceid
                JOIN customer on invoice.customerid=customer.customerid
                JOIN album on album.albumid =track.albumid 
                JOIN artist on artist.artistid =album.artistid 
                JOIN genre on genre.genreid =track.genreid 
                WHERE  customer.customerid=%s
                union all 
                SELECT track.name, album.title , genre.name, artist.name, track.link_video from customer
                JOIN creador_track on creador_track.creadorid=customer.customerid 
                JOIN track on creador_track.trackid =track.trackid 
                JOIN album on album.albumid =track.albumid 
                JOIN artist on artist.artistid =album.artistid 
                JOIN genre on genre.genreid =track.genreid
                WHERE customer.customerid =%s""",(id,id))
            for a,b,c,d,e in cur.fetchall():
                self.tableWidget.setRowCount(row + 1)
                self.tableWidget.setItem(row, 0, QTableWidgetItem(a))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(b))
                self.tableWidget.setItem(row, 2, QTableWidgetItem(c))
                self.tableWidget.setItem(row, 3, QTableWidgetItem(d))
                self.tableWidget.setItem(row, 4, QTableWidgetItem(e))
                
                row += 1
            cur.close()                
            
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conexion is not None:
                conexion.close()
                print('Conexión finalizada.')
    def setupUi(self, Form):
        Form.setObjectName("MisCanciones")
        Form.resize(680, 464)
        Form.setStyleSheet("background-color: rgb(85, 85, 255)")
        Form.setWindowIcon(QIcon('icono.png'))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(250, 10, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(236, 236, 236);")
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(30, 70, 628, 311))
        self.tableWidget.setStyleSheet("background-color: rgb(234, 234, 234);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnWidth(0, 125)
        self.tableWidget.setColumnWidth(1, 125)
        self.tableWidget.setColumnWidth(2, 125)
        self.tableWidget.setColumnWidth(3, 125)
        self.tableWidget.setColumnWidth(4, 125)
        nombreColumnas = ("Track","Album", "Genero", "Artist", "Youtube")
        # Establecer las etiquetas de encabezado horizontal usando etiquetas
        self.tableWidget.setHorizontalHeaderLabels(nombreColumnas)
        self.conectar()
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Mis canciones"))
        self.label.setText(_translate("Form", "Mis Canciones"))
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_MisCanciones()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
