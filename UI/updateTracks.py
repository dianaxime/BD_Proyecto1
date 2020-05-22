# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'updateTracks.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem
import psycopg2
from config import config
import csv

class Ui_UpdateTracks(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(835, 471)
        Form.setWindowIcon(QIcon('icono.png'))
        Form.setStyleSheet("background-color: rgb(85, 85, 255);")
        self.tituloLabel = QtWidgets.QLabel(Form)
        self.tituloLabel.setGeometry(QtCore.QRect(260, 20, 311, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.tituloLabel.setFont(font)
        self.tituloLabel.setStyleSheet("color: rgb(236, 236, 236);")
        self.tituloLabel.setObjectName("tituloLabel")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(20, 60, 801, 321))
        self.tableWidget.setStyleSheet("background-color: rgb(234, 234, 234);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(17)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnWidth(0, 70)
        self.tableWidget.setColumnWidth(1, 70)
        self.tableWidget.setColumnWidth(2, 70)
        self.tableWidget.setColumnWidth(3, 70)
        self.tableWidget.setColumnWidth(4, 70)
        self.tableWidget.setColumnWidth(5, 70)
        self.tableWidget.setColumnWidth(6, 70)
        self.tableWidget.setColumnWidth(7, 70)
        self.tableWidget.setColumnWidth(8, 90)
        self.tableWidget.setColumnWidth(9, 90)
        self.tableWidget.setColumnWidth(10, 90)
        self.tableWidget.setColumnWidth(11, 90)
        self.tableWidget.setColumnWidth(12, 70)
        self.tableWidget.setColumnWidth(13, 70)
        self.tableWidget.setColumnWidth(14, 70)
        self.tableWidget.setColumnWidth(15, 70)
        self.tableWidget.setColumnWidth(16, 70)
        nombreColumnas = ("old_name", "new_name","old_album", "new_album","old_media", "new_media","old_genre", "new_genre", "old_composer", "new_composer","old_milliseconds", "new_milliseconds","old_bytes", "new_bytes","old_up", "new_up","User")
         # Establecer las etiquetas de encabezado horizontal usando etiquetas
        self.tableWidget.setHorizontalHeaderLabels(nombreColumnas)
        self.volverButton = QtWidgets.QPushButton(Form)
        self.volverButton.setGeometry(QtCore.QRect(30, 410, 75, 23))
        self.volverButton.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(72, 72, 72);")
        self.volverButton.setObjectName("volverButton")
        self.conectarDB()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Historial Tracks"))
        self.tituloLabel.setText(_translate("Form", "Especificaciones Update Tracks"))
        self.volverButton.setText(_translate("Form", "Volver"))
        self.volverButton.clicked.connect(lambda:self.openReportes(Form))

    def openReportes(self, Form):
        #self.window = QtWidgets.QWidget()
        #self.ui = Ui_Reportes()
        #self.ui.setupUi(self.window)
        Form.hide()
        #self.window.show()


    def conectarDB(self):
        """ Conexión al servidor de pases de datos PostgreSQL """
        self.tableWidget.setRowCount(0)
        conexion = None
        try:
            # Lectura de los parámetros de conexion
            params = config()
            # Conexion al servidor de PostgreSQL
            conexion = psycopg2.connect(**params)
            # creación del cursor
            cur = conexion.cursor()
            # Ejecución la consulta para obtener la conexión
            cur.execute('SELECT version()')
            # Se obtienen los resultados
            db_version = cur.fetchone()
            cur.execute('''SELECT * FROM track_historial''')
            #Insertamos los datos devueltos por la consulta en la tabla
            row = 0
            for x,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q in cur.fetchall():
                self.tableWidget.setRowCount(row + 1)
                self.tableWidget.setItem(row, 0, QTableWidgetItem(a))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(b))
                self.tableWidget.setItem(row, 2, QTableWidgetItem(c))
                self.tableWidget.setItem(row, 3, QTableWidgetItem(d))
                self.tableWidget.setItem(row, 4, QTableWidgetItem(e))
                self.tableWidget.setItem(row, 5, QTableWidgetItem(f))
                self.tableWidget.setItem(row, 6, QTableWidgetItem(g))
                self.tableWidget.setItem(row, 7, QTableWidgetItem(h))
                self.tableWidget.setItem(row, 8, QTableWidgetItem(i))
                self.tableWidget.setItem(row, 9, QTableWidgetItem(j))
                self.tableWidget.setItem(row, 10, QTableWidgetItem(k))
                self.tableWidget.setItem(row, 11, QTableWidgetItem(l))
                self.tableWidget.setItem(row, 12, QTableWidgetItem(m))
                self.tableWidget.setItem(row, 13, QTableWidgetItem(n))
                self.tableWidget.setItem(row, 14, QTableWidgetItem(str(o)))
                self.tableWidget.setItem(row, 15, QTableWidgetItem(str(p)))
                self.tableWidget.setItem(row, 16, QTableWidgetItem(q))
                row += 1
            # Cerremos el cursor
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conexion is not None:
                conexion.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_UpdateTracks()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
