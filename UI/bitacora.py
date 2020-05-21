# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bitacora.ui'
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

class Ui_Bitacora(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(611, 471)
        Form.setStyleSheet("background-color: rgb(85, 85, 255);")
        Form.setWindowIcon(QIcon('icono.png'))
        self.tituloLabel = QtWidgets.QLabel(Form)
        self.tituloLabel.setGeometry(QtCore.QRect(260, 20, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.tituloLabel.setFont(font)
        self.tituloLabel.setStyleSheet("color: rgb(236, 236, 236);")
        self.tituloLabel.setObjectName("tituloLabel")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(20, 60, 571, 321))
        self.tableWidget.setStyleSheet("background-color: rgb(234, 234, 234);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        nombreColumnas = ("Item","Responsable", "Accion", "Tipo", "Fecha y hora")
        # Establecer las etiquetas de encabezado horizontal usando etiquetas
        self.tableWidget.setHorizontalHeaderLabels(nombreColumnas)
        self.tableWidget.setColumnWidth(0, 140)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 50)
        self.tableWidget.setColumnWidth(3, 50)
        self.tableWidget.setColumnWidth(4, 200)
        self.volverButton = QtWidgets.QPushButton(Form)
        self.volverButton.setGeometry(QtCore.QRect(30, 410, 75, 23))
        self.volverButton.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(72, 72, 72);")
        self.volverButton.setObjectName("volverButton")


        # GROUP BOX
        self.bitacoraGrupo = QtWidgets.QGroupBox(Form)
        self.bitacoraGrupo.setGeometry(QtCore.QRect(150, 390, 400, 50))
        self.bitacoraGrupo.setStyleSheet("color: rgb(236, 236, 236);")
        self.bitacoraGrupo.setObjectName("bitacoraGrupo")
        self.bitacoraBoton = QtWidgets.QPushButton(self.bitacoraGrupo)
        self.bitacoraBoton.setGeometry(QtCore.QRect(310, 12, 75, 31))
        self.bitacoraBoton.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(72, 72, 72);")
        self.bitacoraBoton.setObjectName("bitacoraBoton")
        self.add = QtWidgets.QRadioButton(self.bitacoraGrupo)
        self.add.setGeometry(QtCore.QRect(20, 20, 82, 17))
        self.add.setObjectName("add")
        self.update = QtWidgets.QRadioButton(self.bitacoraGrupo)
        self.update.setGeometry(QtCore.QRect(100, 20, 82, 17))
        self.update.setObjectName("update")
        self.delete = QtWidgets.QRadioButton(self.bitacoraGrupo)
        self.delete.setGeometry(QtCore.QRect(200, 20, 82, 17))
        self.delete.setObjectName("delete")
        self.bitacoraBoton.clicked.connect(self.conectarDB)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Bitacora", "Bitacora"))
        self.tituloLabel.setText(_translate("Form", "Bitácora"))
        self.volverButton.setText(_translate("Form", "Volver"))
        # GROUP BOX
        self.bitacoraGrupo.setTitle(_translate("Form", "Seleccionar"))
        self.bitacoraBoton.setText(_translate("Form", "Ver"))
        self.add.setText(_translate("Form", "Track"))
        self.update.setText(_translate("Form", "Artist"))
        self.delete.setText(_translate("Form", "Álbum"))
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
            if self.add.isChecked() == True:
                cur.execute("SELECT nombre_object, email, accion, tipo, date_on from bitacora where tipo='track' order by date_on DESC")
            elif self.update.isChecked() == True:
                cur.execute("SELECT nombre_object, email, accion, tipo, date_on from bitacora where tipo='artist' order by date_on DESC")
            elif self.delete.isChecked() == True:
                cur.execute("SELECT nombre_object, email, accion, tipo, date_on from bitacora where tipo='album' order by date_on DESC")
            else:
                cur.execute('''SELECT bitacora.nombre_object, 
                bitacora.email, 
                bitacora.accion, 
                bitacora.tipo, 
                bitacora.date_on
                FROM bitacora
                ORDER BY date_on DESC''')
            #Insertamos los datos devueltos por la consulta en la tabla
            row = 0
            for a,b,c,d,e in cur.fetchall():
                self.tableWidget.setRowCount(row + 1)
                self.tableWidget.setItem(row, 0, QTableWidgetItem(a))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(b))
                self.tableWidget.setItem(row, 2, QTableWidgetItem(c))
                self.tableWidget.setItem(row, 3, QTableWidgetItem(d))
                self.tableWidget.setItem(row, 4, QTableWidgetItem(str(e)))
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
    ui = Ui_Bitacora()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
