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


class Ui_searchTrack_form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 250)
        Form.setStyleSheet("background-color: rgb(85, 85, 255);")
        Form.setWindowIcon(QIcon('icono.png'))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(230, 20, 121, 21))
        self.label.setStyleSheet("color: rgb(236, 236, 236);")
        self.label.setObjectName("label")
        self.inputTrack = QtWidgets.QLineEdit(Form)
        self.inputTrack.setGeometry(QtCore.QRect(100, 60, 161, 21))
        self.inputTrack.setStyleSheet("color: rgb(72, 72, 72);\n"
"background-color: rgb(243, 243, 243);")
        self.inputTrack.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 60, 41, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(290, 60, 51, 23))
        self.pushButton.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(72, 72, 72);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.buscarCancion)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(50, 110, 502, 100))
        self.tableWidget.setStyleSheet("background-color: rgb(234, 234, 234);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnWidth(0, 125)
        self.tableWidget.setColumnWidth(1, 125)
        self.tableWidget.setColumnWidth(2, 125)
        self.tableWidget.setColumnWidth(3, 125)
        nombreColumnas = ("Track","Album", "Artist", "Unit Price")
        # Establecer las etiquetas de encabezado horizontal usando etiquetas
        self.tableWidget.setHorizontalHeaderLabels(nombreColumnas)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Buscar Track"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Buscar Track</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:9pt; color:#ffffff;\">Track:</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "Buscar"))

    def buscarCancion(self):
        #Buscar track
        nombreTrack=self.inputTrack.text()
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
    
            if nombreTrack != '' :
                cur.execute( "SELECT track.name FROM track WHERE track.name=%s",(nombreTrack,))
                IDtrackO=cur.fetchall()#[0][0]
                if (len(IDtrackO)==0):
                    blank=QMessageBox()
                    blank.setIcon(QMessageBox.Information)
                    blank.setWindowTitle("ERROR")
                    blank.setText("El track no esta registrado")
                    blank.exec()
                else:
                    cur.execute("""
                            SELECT track.name, album.title, artist.name, track.unitprice
                            FROM track  
                                JOIN album ON album.albumid = track.albumid
                                JOIN artist ON artist.artistid = album.artistid
                            WHERE track.name = %s
                            """,(nombreTrack,))

                    row = 0
                    for a,b,c,d in cur.fetchall():
                        self.tableWidget.setRowCount(row + 1)
                        self.tableWidget.setItem(row, 0, QTableWidgetItem(a))
                        self.tableWidget.setItem(row, 1, QTableWidgetItem(b))
                        self.tableWidget.setItem(row, 2, QTableWidgetItem(c))
                        self.tableWidget.setItem(row, 3, QTableWidgetItem(str(d)))
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
    ui = Ui_searchTrack_form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
