# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'updateArtist.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem
import psycopg2
from config import config

class Ui_UpdateArtist(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(835, 471)
        Form.setStyleSheet("background-color: rgb(85, 85, 255);")
        Form.setWindowIcon(QIcon('icono.png'))
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
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnWidth(0, 266)
        self.tableWidget.setColumnWidth(1, 266)
        self.tableWidget.setColumnWidth(2, 266)
        nombreColumnas = ("old_name", "new_name","User")
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
        Form.setWindowTitle(_translate("Form", "Historial Artista"))
        self.tituloLabel.setText(_translate("Form", "Especificaciones Update Artista"))
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
            cur.execute('''SELECT * FROM artist_historial''')
            #Insertamos los datos devueltos por la consulta en la tabla
            row = 0
            for x,a,b,c in cur.fetchall():
                self.tableWidget.setRowCount(row + 1)
                self.tableWidget.setItem(row, 0, QTableWidgetItem(a))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(b))
                self.tableWidget.setItem(row, 2, QTableWidgetItem(c))
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
    ui = Ui_UpdateArtist()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
