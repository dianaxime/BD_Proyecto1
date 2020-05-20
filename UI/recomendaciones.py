# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'recomendaciones.ui'
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
import datetime
import pymongo
#conectar a mongo
conexion=pymongo.MongoClient() 
db=conexion.proyectoBD
coleccion=db.recomendaciones

class Ui_Recomendaciones(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(515, 514)
        Form.setStyleSheet("background-color: rgb(85, 85, 255);\n"
"color: rgb(236, 236, 236);")
        Form.setWindowIcon(QIcon('icono.png'))
        self.titulo = QtWidgets.QLabel(Form)
        self.titulo.setGeometry(QtCore.QRect(130, 20, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.titulo.setFont(font)
        self.titulo.setObjectName("titulo")
        self.fechaInput = QtWidgets.QLineEdit(Form)
        self.fechaInput.setGeometry(QtCore.QRect(90, 90, 151, 21))
        self.fechaInput.setStyleSheet("color: rgb(72, 72, 72);\n"
"background-color: rgb(243, 243, 243);")
        self.fechaInput.setObjectName("fechaInput")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.agregarButton = QtWidgets.QPushButton(Form)
        self.agregarButton.setGeometry(QtCore.QRect(280, 90, 75, 23))
        self.agregarButton.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(72, 72, 72);")
        self.agregarButton.setObjectName("agregarButton")
        self.agregarButton.clicked.connect(self.agregar)
        self.generarButton = QtWidgets.QPushButton(Form)
        self.generarButton.setGeometry(QtCore.QRect(380, 90, 75, 23))
        self.generarButton.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(72, 72, 72);")
        self.generarButton.setObjectName("generarButton")
        self.generarButton.clicked.connect(self.generar)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(40, 140, 421, 331))
        self.tableWidget.setStyleSheet("background-color: rgb(234, 234, 234);\n"
"color: rgb(72, 72, 72);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnWidth(0, 210)
        self.tableWidget.setColumnWidth(1, 208)
        nombreColumnas = ("Track","Genero")
        # Establecer las etiquetas de encabezado horizontal usando etiquetas
        self.tableWidget.setHorizontalHeaderLabels(nombreColumnas)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Recomendaciones"))
        self.titulo.setText(_translate("Form", "Recomendado para ti"))
        self.label_2.setText(_translate("Form", "Fecha:"))
        self.agregarButton.setText(_translate("Form", "Agregar"))
        self.generarButton.setText(_translate("Form", "Generar"))

    def agregar(self):
        self.tableWidget.setRowCount(0)
        fecha=self.fechaInput.text()
        conexion = None
        try:
            # Lectura de los parámetros de conexion
            params = config()

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
            #fecha = '2009-01-06'
            if (fecha!=''):
                ahora = datetime.datetime.utcnow()
                tiempo = ahora - datetime.timedelta(days=30)
                cur.execute('''
                    SELECT customer.email, track."name", 
                    genre."name" as genre, invoice.invoicedate
                    FROM invoice
                    JOIN invoiceline ON invoiceline.invoiceid = invoice.invoiceid
                    join track on invoiceline.trackid = track.trackid
                    join genre on track.genreid = genre.genreid
                    join customer on customer.customerid = invoice.customerid
                    where invoice.invoicedate = %s
                ''',(fecha,))
                # Recorremos los resultados y los mostramos
                compras = cur.fetchall()
                for email, cancion, genero, fechac in compras:
                    #print(email, cancion, genero, fechac)
                    cur.execute('''
                        SELECT DISTINCT(track."name"), genre."name"
                        FROM bitacora
                        JOIN track ON bitacora.nombre_object = track."name"
                        JOIN genre ON track.genreid = genre.genreid
                        WHERE bitacora.nombre_object <> %s
                        AND bitacora.email <> %s 
                        AND bitacora.date_on > %s
                        AND bitacora.date_on < %s
                        AND bitacora.accion = %s
                    ''',(cancion, email, tiempo, ahora, 'add'))
                    resul = cur.fetchall()
                    for a, b in resul:
                        #print(a, b)
                        if (coleccion.find({'_id': email}).count() > 0):
                            if (coleccion.find({ '_id': email, 'sells.track': cancion}).count() <= 0):
                                result = coleccion.update({'_id': email }, { '$set': { 'modified': ahora },'$push': { 'sells': {'email': email, 'track': cancion, 'genre': genero, 'date': fechac}}}, w=1)
                            if (coleccion.find({ '_id': email, 'tracks.track': a}).count() <= 0):
                                result = coleccion.update({'_id': email }, { '$set': { 'modified': ahora },'$push': { 'tracks': {'track': a, 'genre': b, 'date': ahora} }}, w=1)
                        else:
                            result = coleccion.insert({'_id': email }, { '$set': { 'modified': ahora },'$push': { 'sells': {'email': email, 'track': cancion, 'genre': genero, 'date': fechac}, 'tracks': {'track': a, 'genre': b, 'date': ahora} } }, w=1)
                
                print("--------------------------------------------------")

                # Cerremos el cursor
                cur.close()
            else:
                print ("NECESITA FECHA")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conexion is not None:
                conexion.close()
                print('Conexión finalizada.')


    def generar(self):
        """ Conexión al servidor de pases de datos PostgreSQL """
        conexion = None
        try:
            # Lectura de los parámetros de conexion
            params = config()

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
            cur.execute(
            '''SELECT customer.email, genre.name, COUNT(genre.genreid)
                FROM creador_track
                JOIN customer ON customer.customerid = creador_track.creadorid
                JOIN track ON creador_track.trackid = track.trackid 
                JOIN genre ON track.genreid = genre.genreid
                WHERE customer.customerid IN (
                SELECT creador_track.creadorid 
                FROM creador_track
                GROUP BY creador_track.creadorid
                ORDER BY COUNT(creador_track.creadorid) DESC LIMIT 10)
                GROUP BY customer.email, genre.genreid
                ORDER BY customer.email DESC
                '''
            )
            resul = cur.fetchall()
            for email, genre, cuenta in resul:
                if cuenta > 5:
                    a = coleccion.aggregate([{ '$match': { '_id': email } },{ '$unwind': '$tracks' },{ '$match': { 'tracks.genre': genre }},{ '$project': { 'track': '$tracks.track', 'genre': '$tracks.genre' }}])
                    for i in a:
                        print(i['_id'],' ',i['track'],' ',i['genre'])
            

            

            
            # Recorremos los resultados y los mostramos
            print("--------------------------------------------------")

            # Cerremos el cursor
            cur.close()
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
    ##RECORDAR QUITAR ID
    ui = Ui_Recomendaciones()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
