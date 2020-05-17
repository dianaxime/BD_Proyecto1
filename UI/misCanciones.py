# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'misCanciones.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

class Ui_MisCanciones(object):
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
