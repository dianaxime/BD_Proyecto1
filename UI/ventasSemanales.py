# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventasSemanales.ui'
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


class Ui_VentasSemanales(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(471, 425)
        Form.setStyleSheet("background-color: rgb(85, 85, 255);")
        Form.setWindowIcon(QIcon('icono.png'))
        self.titleForm = QtWidgets.QLabel(Form)
        self.titleForm.setGeometry(QtCore.QRect(150, 20, 301, 21))
        self.titleForm.setStyleSheet("color: rgb(236, 236, 236);")
        self.titleForm.setObjectName("titleForm")
        self.inputInicio = QtWidgets.QLineEdit(Form)
        self.inputInicio.setGeometry(QtCore.QRect(150, 70, 80, 21))
        self.inputInicio.setStyleSheet("color: rgb(72, 72, 72);\n"
"background-color: rgb(243, 243, 243);")
        self.inputInicio.setObjectName("inputInicio")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 70, 100, 16))
        self.label_2.setObjectName("label_2")
        self.buscarBoton = QtWidgets.QPushButton(Form)
        self.buscarBoton.setGeometry(QtCore.QRect(320, 100, 51, 23))
        self.buscarBoton.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(72, 72, 72);")
        self.buscarBoton.setObjectName("buscarBoton")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(30, 150, 411, 251))
        self.tableWidget.setStyleSheet("background-color: rgb(234, 234, 234);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnWidth(0, 66)
        self.tableWidget.setColumnWidth(1, 87)
        self.tableWidget.setColumnWidth(2, 87)
        self.tableWidget.setColumnWidth(3, 87)
        self.tableWidget.setColumnWidth(4, 81)
        nombreColumnas = ("Semana", "Incio", "Fin", "Total", "Ventas")
                # Establecer las etiquetas de encabezado horizontal usando etiquetas
        self.tableWidget.setHorizontalHeaderLabels(nombreColumnas)
        self.inputInicio_2 = QtWidgets.QLineEdit(Form)
        self.inputInicio_2.setGeometry(QtCore.QRect(150, 100, 80, 21))
        self.inputInicio_2.setStyleSheet("color: rgb(72, 72, 72);\n"
"background-color: rgb(243, 243, 243);")
        self.inputInicio_2.setObjectName("inputInicio_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 100, 100, 16))
        self.label_3.setObjectName("label_3")
        self.inputCantidad = QtWidgets.QLineEdit(Form)
        self.inputCantidad.setGeometry(QtCore.QRect(315, 70, 71, 21))
        self.inputCantidad.setStyleSheet("color: rgb(72, 72, 72);\n"
"background-color: rgb(243, 243, 243);")
        self.inputCantidad.setObjectName("inputCantidad")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(270, 70, 25, 16))
        self.label_4.setObjectName("label_4")
        self.buscarBoton.clicked.connect(self.generarDatos)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ventas Semanales"))
        self.titleForm.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Ventas Semanales</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:9pt; color:#ffffff;\">Semana de inicio:</span></p></body></html>"))
        self.buscarBoton.setText(_translate("Form", "Ver"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:9pt; color:#ffffff;\">Semana de fin:</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:9pt; color:#ffffff;\">Año:</span></p></body></html>"))

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
            anio=self.inputCantidad.text()
           
            if inicio != '' and fin != '' and anio!='':
                cur.execute( """SELECT week_of_year, first_day_of_week, last_day_of_week, sum, count
FROM ventasdatacube
WHERE year_actual = %s AND
    quarter_actual IS NULL AND month_actual IS NULL AND genero IS NULL AND artista is null and 
    week_of_year IS NOT null and week_of_year >= %s and week_of_year <= %s
AND date_actual IS null AND first_day_of_week IS not null AND last_day_of_week is not NULL""",(anio,inicio, fin,))
                query=cur.fetchall()#[0][0]
                if (len(query)!=0):
                    row = 0
                    for a,b,c,d,e in query:
                        self.tableWidget.setRowCount(row + 1)
                        self.tableWidget.setItem(row, 0, QTableWidgetItem(str(a)))
                        self.tableWidget.setItem(row, 1, QTableWidgetItem(str(b)))
                        self.tableWidget.setItem(row, 2, QTableWidgetItem(str(c)))
                        self.tableWidget.setItem(row, 3, QTableWidgetItem(str(d)))
                        self.tableWidget.setItem(row, 4, QTableWidgetItem(str(e)))
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



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_VentasSemanales()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
