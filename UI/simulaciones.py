# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simulaciones.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
import psycopg2
from config import config
from random import randint
from datetime import date

class Ui_Simulaciones(object):
    def setupUi(self, Simulaciones):
        Simulaciones.setObjectName("Simulaciones")
        Simulaciones.resize(332, 235)
        Simulaciones.setStyleSheet("background-color: rgb(85, 85, 255);\n"
"color: rgb(236, 236, 236);")
        Simulaciones.setWindowIcon(QIcon('icono.png'))
        self.nombreLabel = QtWidgets.QLabel(Simulaciones)
        self.nombreLabel.setGeometry(QtCore.QRect(20, 30, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.nombreLabel.setFont(font)
        self.nombreLabel.setObjectName("nombreLabel")
        self.apellidoLabel = QtWidgets.QLabel(Simulaciones)
        self.apellidoLabel.setGeometry(QtCore.QRect(20, 70, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.apellidoLabel.setFont(font)
        self.apellidoLabel.setObjectName("apellidoLabel")
        self.emailLabel = QtWidgets.QLabel(Simulaciones)
        self.emailLabel.setGeometry(QtCore.QRect(20, 110, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.emailLabel.setFont(font)
        self.emailLabel.setObjectName("emailLabel")
        self.nombreInput = QtWidgets.QLineEdit(Simulaciones)
        self.nombreInput.setGeometry(QtCore.QRect(190, 30, 113, 20))
        self.nombreInput.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(72, 72, 72);")
        self.nombreInput.setText("")
        self.nombreInput.setObjectName("nombreInput")
        self.apellidoInput = QtWidgets.QLineEdit(Simulaciones)
        self.apellidoInput.setGeometry(QtCore.QRect(190, 70, 113, 20))
        self.apellidoInput.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(72, 72, 72);")
        self.apellidoInput.setObjectName("apellidoInput")
        self.emailInput = QtWidgets.QLineEdit(Simulaciones)
        self.emailInput.setGeometry(QtCore.QRect(190, 110, 113, 20))
        self.emailInput.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(72, 72, 72);")
        self.emailInput.setObjectName("emailInput")
        self.sigInButton = QtWidgets.QPushButton(Simulaciones)
        self.sigInButton.setGeometry(QtCore.QRect(110, 160, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.sigInButton.setFont(font)
        self.sigInButton.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(72, 72, 72);")
        self.sigInButton.setObjectName("sigInButton")
        self.sigInButton.clicked.connect(self.conectar)

        self.retranslateUi(Simulaciones)
        QtCore.QMetaObject.connectSlotsByName(Simulaciones)


    def conectar(self):
        """ Conexión al servidor de pases de datos PostgreSQL """
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

            #id de invoice e invoiceline
            cur.execute( "SELECT MAX(invoice.invoiceid) FROM invoice" )
            IDinvoice=cur.fetchall()
            invoiceoficial=IDinvoice[0][0]
            invoiceoficial += 1
            cur.execute( "SELECT MAX(invoiceline.invoicelineid) FROM invoiceline" )
            IDinvoiceline=cur.fetchall()
            invoicelineoficial=IDinvoiceline[0][0]
            invoicelineoficial += 1

            #quiero reproducir n canciones
            n=self.nombreInput.text()
            x=self.apellidoInput.text()
            #fecha introducida por el usuario
            d = self.emailInput.text()
            if n!='' and x!='' and d!='':
                n=int(n)
                x=int(x)
                cur.execute( "SELECT MAX(track.trackid) FROM track" )
                b = cur.fetchall()
                b = int(b[0][0])
                print(b)

                for i in range(n):
                    existente=False
                    while (existente==False):
                        cur.execute( "SELECT  trackid from track where trackid=%s",  (randint(1,b),) )
                        idtrack=cur.fetchall()#[0][0]
                        if (len(idtrack)!=0):
                            existente=True
                    idtrack=idtrack[0][0]
                    print(idtrack)
                    cur.execute( """INSERT into reproduccion (trackid) VALUES (%s) """,(idtrack,))
                    conexion.commit()

                print("------------------------------")
                #quiero comprar x canciones
                
                
                #cantidad de customers
                cur.execute( "SELECT MAX(customer.customerid) FROM customer" )
                c = cur.fetchall()
                c = int(c[0][0])
                print(c)

                for i in range(x):
                    existente=False
                    while (existente==False):
                        cur.execute( "SELECT  trackid, unitprice from track where trackid=%s",  (randint(1,b),) )
                        idtrack=cur.fetchall()#[0][0]
                        if (len(idtrack)!=0):
                            existente=True
                    idOtrack=idtrack[0][0]
                    uptrack=idtrack[0][1]
                    print("cancion: "+str(idOtrack))
                    print("precio: "+str(uptrack))
                    
                    existenteC=False
                    while (existenteC==False):
                        cur.execute( "SELECT  customerid from customer where customerid=%s",  (randint(1,c),) )
                        idCus=cur.fetchall()#[0][0]
                        if (len(idCus)!=0):
                            existenteC=True
                    idcustomer=idCus[0][0]
                    print ("comprador: "+str(idcustomer))
                    cur.execute( "INSERT INTO invoice (invoiceid, invoicedate, customerid, total) values (%s, %s, %s, %s)", (invoiceoficial, d, idcustomer, uptrack))
                    cur.execute( """INSERT INTO invoiceline (invoiceid, trackid, unitprice, quantity, invoicelineid) 
                            values (%s, %s, %s, %s, %s)""", (invoiceoficial, idOtrack, uptrack, 1, invoicelineoficial))
                    invoiceoficial+=1
                    invoicelineoficial+=1
                    print("--------------------------")

                #conexion.commit()
            else:
                blank=QMessageBox()
                blank.setIcon(QMessageBox.Information)
                blank.setWindowTitle("ERROR")
                blank.setText("Por favor complete los campos")
                blank.exec()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conexion is not None:
                conexion.close()
                print('Conexión finalizada.')

    def retranslateUi(self, Simulaciones):
        _translate = QtCore.QCoreApplication.translate
        Simulaciones.setWindowTitle(_translate("Simulaciones", "Simulaciones"))
        self.nombreLabel.setText(_translate("Simulaciones", "Cantidad de reproducciones:"))
        self.apellidoLabel.setText(_translate("Simulaciones", "Cantidad de compras:"))
        self.emailLabel.setText(_translate("Simulaciones", "Fecha:"))
        self.sigInButton.setText(_translate("Simulaciones", "Generar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Simulaciones = QtWidgets.QWidget()
    ui = Ui_Simulaciones()
    ui.setupUi(Simulaciones)
    Simulaciones.show()
    sys.exit(app.exec_())
