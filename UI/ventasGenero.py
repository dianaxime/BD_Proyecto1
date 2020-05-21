# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventasGenero.ui'
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
import csv

class Ui_VentasGenero(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 440)
        Form.setStyleSheet("background-color: rgb(85, 85, 255);")
        Form.setWindowIcon(QIcon('icono.png'))
        self.titleForm = QtWidgets.QLabel(Form)
        self.titleForm.setGeometry(QtCore.QRect(140, 10, 181, 31))
        self.titleForm.setStyleSheet("color: rgb(236, 236, 236);")
        self.titleForm.setObjectName("titleForm")
        self.inputInicio = QtWidgets.QLineEdit(Form)
        self.inputInicio.setGeometry(QtCore.QRect(110, 60, 191, 21))
        self.inputInicio.setStyleSheet("color: rgb(72, 72, 72);\n"
"background-color: rgb(243, 243, 243);")
        self.inputInicio.setObjectName("inputInicio")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(60, 60, 41, 16))
        self.label_2.setObjectName("label_2")
        self.buscarBoton = QtWidgets.QPushButton(Form)
        self.buscarBoton.setGeometry(QtCore.QRect(340, 70, 51, 23))
        self.buscarBoton.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(72, 72, 72);")
        self.buscarBoton.setObjectName("buscarBoton")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(30, 140, 411, 251))
        self.tableWidget.setStyleSheet("background-color: rgb(234, 234, 234);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 109)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setColumnWidth(3, 100)
        nombreColumnas = ("Fecha", "Genero", "Total", "Ventas")
                # Establecer las etiquetas de encabezado horizontal usando etiquetas
        self.tableWidget.setHorizontalHeaderLabels(nombreColumnas)
        self.inputInicio_2 = QtWidgets.QLineEdit(Form)
        self.inputInicio_2.setGeometry(QtCore.QRect(110, 90, 191, 21))
        self.inputInicio_2.setStyleSheet("color: rgb(72, 72, 72);\n"
"background-color: rgb(243, 243, 243);")
        self.inputInicio_2.setObjectName("inputInicio_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(60, 90, 41, 16))
        self.label_3.setObjectName("label_3")
        self.buscarBoton.clicked.connect(self.generarDatos)
        self.reporteButton = QtWidgets.QPushButton(Form)
        self.reporteButton.setGeometry(QtCore.QRect(400, 410, 75, 23))
        self.reporteButton.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(72, 72, 72);")
        self.reporteButton.setObjectName("reporteButton")
        self.reporteButton.clicked.connect(self.generarCsv)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ventas por genero y fecha"))
        self.titleForm.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Ventas por género</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:9pt; color:#ffffff;\">Inicio:</span></p></body></html>"))
        self.buscarBoton.setText(_translate("Form", "Ver"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:9pt; color:#ffffff;\">Fin:</span></p></body></html>"))
        self.reporteButton.setText(_translate("Form", "CSV"))
    def generarDatos(self):
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
            inicio=self.inputInicio.text()
            fin=self.inputInicio_2.text()
           
            if inicio != '' and fin != '' :
                cur.execute( """SELECT date_actual, genero, sum,count
FROM ventasdatacube
WHERE year_actual is NULL AND 
    quarter_actual IS NULL AND month_actual is NULL AND genero IS not NULL AND artista is null and 
    week_of_year IS NULL AND first_day_of_week IS null AND last_day_of_week is null
    and date_actual >= %s and date_actual <= %s
ORDER BY date_actual asc""",(inicio, fin,))
                query=cur.fetchall()#[0][0]
                if (len(query)!=0):
                    row = 0
                    for a,b,c,d in query:
                        self.tableWidget.setRowCount(row + 1)
                        self.tableWidget.setItem(row, 0, QTableWidgetItem(str(a)))
                        self.tableWidget.setItem(row, 1, QTableWidgetItem(str(b)))
                        self.tableWidget.setItem(row, 2, QTableWidgetItem(str(c)))
                        self.tableWidget.setItem(row, 3, QTableWidgetItem(str(d)))
                        row += 1
                    cur.close() 
                    print("no hay mas")
                else:                      
                    blank=QMessageBox()
                    blank.setIcon(QMessageBox.Information)
                    blank.setWindowTitle("ERROR")
                    blank.setText("No se registraron ventas durante esas fechas")
                    blank.exec()                           
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

    def generarCsv(self):
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
            inicio=self.inputInicio.text()
            fin=self.inputInicio_2.text()
            ##escritura a .csv
            with open('ventasGeneroReporteria.csv', mode='w', newline='') as cvs_file:
                csv_writer = csv.writer(cvs_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                csv_writer.writerow(['Fecha', 'Artista', 'Total','Ventas'])
                if inicio != '' and fin != '' :
                    cur.execute( """SELECT date_actual, genero, sum,count
                    FROM ventasdatacube
                    WHERE year_actual is NULL AND 
                        quarter_actual IS NULL AND month_actual is NULL AND genero IS not NULL AND artista is null and 
                        week_of_year IS NULL AND first_day_of_week IS null AND last_day_of_week is null
                        and date_actual >= %s and date_actual <= %s
                    ORDER BY date_actual asc""",(inicio, fin,))
                    for a,b,c,d in cur.fetchall():
                        csv_writer.writerow([str(a), str(b), str(c), str(d)])
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
    ui = Ui_VentasGenero()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
