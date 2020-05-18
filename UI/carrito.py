# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'searchTrack_form.ui'
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
from PyQt5.QtWidgets import QMessageBox


class Ui_Carrito(object):
    def __init__(self,id):
        self.id=id
        print(self.id)

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
            cur.execute( """SELECT track.name, artist.name, track.unitprice from carrito 
                JOIN track on carrito.trackid=track.trackid
                JOIN album on track.albumid=album.albumid
                JOIN artist on album.artistid=artist.artistid
                where state='vigente' and customerid=%s""",(id,))
            for a,b,c in cur.fetchall():
                self.tableWidget.setRowCount(row + 1)
                self.tableWidget.setItem(row, 0, QTableWidgetItem(a))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(b))
                self.tableWidget.setItem(row, 2, QTableWidgetItem(str(c)))
                row += 1
            cur.close()                
            
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conexion is not None:
                conexion.close()
                print('Conexión finalizada.')

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 400)
        Form.setStyleSheet("background-color: rgb(85, 85, 255);")
        Form.setWindowIcon(QIcon('icono.png'))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(230, 20, 180, 21))
        self.label.setStyleSheet("color: rgb(236, 236, 236);")
        self.label.setObjectName("label")


        self.deleteButton = QtWidgets.QPushButton(Form)
        self.deleteButton.setGeometry(QtCore.QRect(100, 350, 51, 23))
        self.deleteButton.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(72, 72, 72);")
        self.deleteButton.setObjectName("deleteButton")
        self.deleteButton.clicked.connect(self.deleteItem)

        self.finalizarButton = QtWidgets.QPushButton(Form)
        self.finalizarButton.setGeometry(QtCore.QRect(440, 350, 100, 23))
        self.finalizarButton.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(72, 72, 72);")
        self.finalizarButton.setObjectName("finalizarButton")
        self.finalizarButton.clicked.connect(self.finalizarCompra)

        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(50, 70, 502, 250))
        self.tableWidget.setStyleSheet("background-color: rgb(234, 234, 234);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnWidth(0, 167)
        self.tableWidget.setColumnWidth(1, 167)
        self.tableWidget.setColumnWidth(2, 165)
        nombreColumnas = ("Track","Artist", "Unit Price")
        # Establecer las etiquetas de encabezado horizontal usando etiquetas
        self.tableWidget.setHorizontalHeaderLabels(nombreColumnas)
        self.conectar()
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Comprar Cancion"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Comprar Cancion</span></p></body></html>"))
        self.deleteButton.setText(_translate("Form", "Eliminar"))
        self.finalizarButton.setText(_translate("Form", "Finalizar Compra"))

    def finalizarCompra(self, Form):
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

            cur.execute( "SELECT MAX(invoice.invoiceid) FROM invoice" )
            IDinvoice=cur.fetchall()
            invoiceoficial=IDinvoice[0][0]
            invoiceoficial += 1
            cur.execute( "SELECT MAX(invoiceline.invoicelineid) FROM invoiceline" )
            IDinvoiceline=cur.fetchall()
            invoicelineoficial=IDinvoiceline[0][0]
            invoicelineoficial += 1
            total=0
            print("hola1")
            cur.execute("SELECT SUM(track.unitprice) FROM carrito JOIN track on carrito.trackid=track.trackid WHERE carrito.customerid = %s and carrito.state='vigente'",(id,))
            tracksB=cur.fetchall()
            total=tracksB[0][0]
            """print(tracksB)
            print(total)"""
            cur.execute( "INSERT INTO invoice (invoiceid, invoicedate, customerid, total) values (%s, now(), %s, %s)", (invoiceoficial, id, total))
            cur.execute("SELECT track.trackid, track.unitprice FROM carrito JOIN track on carrito.trackid=track.trackid WHERE carrito.customerid = %s and carrito.state='vigente'",(id,))
            tracksB=cur.fetchall()
            for a,b in tracksB :
                cur.execute( """INSERT INTO invoiceline (invoiceid, trackid, unitprice, quantity, invoicelineid) 
                    values (%s, %s, %s, %s, %s)""", (invoiceoficial, a, b, 1, invoicelineoficial))
                invoicelineoficial += 1
            from reportlab.lib.pagesizes import letter
            from reportlab.pdfgen import canvas
            from datetime import date 
            x=date.today()
            cur.execute( "SELECT firstname from customer where customerid=%s", (id,))
            tracksB=cur.fetchall()
            nombreComprador=tracksB[0][0]
            cur.execute( "SELECT lastname from customer where customerid=%s", (id,))
            tracksB=cur.fetchall()
            apellidoComprador=tracksB[0][0]
            canvas = canvas.Canvas("comprobanteVenta.pdf", pagesize=letter)
            canvas.setLineWidth(.3)
            canvas.setFont('Helvetica', 12)
            canvas.drawString(30,750,'PYSTREAM.SA')
            canvas.drawString(30,735,'COMPROBANTE DE COMPRA')
            canvas.drawString(520,750,str(x))
            canvas.line(480,747,580,747)
            canvas.drawString(275,725,'MONTO POR:')
            canvas.drawString(500,725,"$"+str(total))
            canvas.line(378,723,580,723)
            canvas.drawString(30,703,'REALIZADO POR:')
            canvas.line(120,700,580,700)
            canvas.drawString(160,703,nombreComprador+" "+apellidoComprador)
            canvas.line(30,680,580,680)
            canvas.drawString(190,682,"LISTADO DE CANCIONES COMPRADAS")
            #canvas.drawString(190,662,"LISTADO DE CANCIONES COMPRADAS")
            altura=642
            var1="hola"
            var2="vos"
            """for i in range(3):
                canvas.drawString(190,altura, var1+"..................."+var2)
                altura-=20"""
            row=0
            cur.execute( """SELECT track.name, track.unitprice from carrito 
                JOIN track on carrito.trackid=track.trackid
                where state='vigente' and customerid=%s""",(id,))
            tracksB=cur.fetchall()
            for a,b in tracksB:
                canvas.drawString(30,altura, a+".................................................................................................................$"+str(b))
                altura-=20
                row += 1
            canvas.save()
            
            cur.execute( """UPDATE carrito set state='completado' where customerid=%s""",(id,))
            conexion.commit()

            blank=QMessageBox()
            blank.setIcon(QMessageBox.Information)
            blank.setWindowTitle("Accion Exitosa")
            blank.setText("Compra realizada con exito")
            blank.exec()
            
            self.tableWidget.setRowCount(0)
            

#canvas.line(30,680,580,650)
            
            cur.close() 
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conexion is not None:
                conexion.close()
                print('Conexión finalizada.')

    def deleteItem(self, Form):
        try:
            # Lectura de los parámetros de conexion
            params = config()
            #print(params)
            id=self.id
            # Conexion al servidor de PostgreSQL
            print('Conectando a la base de datos PostgreSQL...')
            conexion = psycopg2.connect(**params)
            # creación del cursor
            cur = conexion.cursor()
            r = self.tableWidget.currentRow()
            nombretrack=self.tableWidget.item(r,0).text()
            print(nombretrack)
            cur.execute("SELECT track.trackid FROM track WHERE track.name = %s",(nombretrack,))
            trackid=cur.fetchall()
            trackid=trackid[0][0]
            cur.execute("DELETE FROM carrito WHERE trackid = %s and customerid=%s and state='vigente'",(trackid, id))
            
            conexion.commit()

            blank=QMessageBox()
            blank.setIcon(QMessageBox.Information)
            blank.setWindowTitle("Accion Exitosa")
            blank.setText("Se ha eliminado el track de su carrito")
            blank.exec()
            self.conectar()
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
    ui = Ui_Carrito()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
