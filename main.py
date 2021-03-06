# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(430, 491)
        Main.setStyleSheet("QWidget#titulo {\n"
"    background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QLabel#lbl_titulo {\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 20px;\n"
"}\n"
"\n"
"QLabel, QLineEdit, QPushButton {\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton#btn_cadastrar {    \n"
"    background-color: rgb(0, 170, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#btn_pesquisar {    \n"
"    background-color: rgb(85, 170, 255);\n"
"    color: rgb(255, 255, 255);\n"
"    border: none;\n"
"}\n"
"")
        self.painel_principal = QtWidgets.QWidget(Main)
        self.painel_principal.setObjectName("painel_principal")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.painel_principal)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.titulo = QtWidgets.QWidget(self.painel_principal)
        self.titulo.setMinimumSize(QtCore.QSize(0, 50))
        self.titulo.setMaximumSize(QtCore.QSize(16777215, 50))
        self.titulo.setObjectName("titulo")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.titulo)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lbl_titulo = QtWidgets.QLabel(self.titulo)
        self.lbl_titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_titulo.setObjectName("lbl_titulo")
        self.verticalLayout_4.addWidget(self.lbl_titulo)
        self.verticalLayout_3.addWidget(self.titulo)
        self.botoes = QtWidgets.QWidget(self.painel_principal)
        self.botoes.setObjectName("botoes")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.botoes)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_pesquisar = QtWidgets.QPushButton(self.botoes)
        self.btn_pesquisar.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_pesquisar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.btn_pesquisar.setObjectName("btn_pesquisar")
        self.horizontalLayout.addWidget(self.btn_pesquisar)
        self.btn_cadastrar = QtWidgets.QPushButton(self.botoes)
        self.btn_cadastrar.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_cadastrar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.btn_cadastrar.setObjectName("btn_cadastrar")
        self.horizontalLayout.addWidget(self.btn_cadastrar)
        self.verticalLayout_3.addWidget(self.botoes)
        self.tbl_funcionarios = QtWidgets.QTableWidget(self.painel_principal)
        self.tbl_funcionarios.setObjectName("tbl_funcionarios")
        self.tbl_funcionarios.setColumnCount(4)
        self.tbl_funcionarios.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_funcionarios.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_funcionarios.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_funcionarios.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_funcionarios.setHorizontalHeaderItem(3, item)
        self.verticalLayout_3.addWidget(self.tbl_funcionarios)
        Main.setCentralWidget(self.painel_principal)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "MainWindow"))
        self.lbl_titulo.setText(_translate("Main", "LISTAGEM DE FUNCION??RIO"))
        self.btn_pesquisar.setText(_translate("Main", "Atualizar"))
        self.btn_cadastrar.setText(_translate("Main", "Cadastrar"))
        item = self.tbl_funcionarios.horizontalHeaderItem(0)
        item.setText(_translate("Main", "Nome"))
        item = self.tbl_funcionarios.horizontalHeaderItem(1)
        item.setText(_translate("Main", "Sexo"))
        item = self.tbl_funcionarios.horizontalHeaderItem(2)
        item.setText(_translate("Main", "Sal??rio"))
        item = self.tbl_funcionarios.horizontalHeaderItem(3)
        item.setText(_translate("Main", "Departamento"))
