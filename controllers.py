from tkinter import dialog
from main import Ui_Main
from cadastrar import Ui_Cadastrar
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QDialog
from PyQt5.QtCore import QTimer
from models import Funcionario
import utils

class MainController(QMainWindow, Ui_Main):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.popular_tabela()
        self.btn_cadastrar.clicked.connect(self.abrir_dialog)
        self.btn_pesquisar.clicked.connect(self.popular_tabela)

    def popular_tabela(self):
        itens = Funcionario.listar()
        self.tbl_funcionarios.setRowCount(len(itens))

        for linha, funcionario in enumerate(itens):
            nome = QTableWidgetItem()
            nome.setText(funcionario.nome)

            sexo = QTableWidgetItem()
            sexo.setText('Masculino' if funcionario.sexo == 'M' else 'Feminino')

            salario = QTableWidgetItem()
            salario.setText(str(funcionario.salario))

            departamento = QTableWidgetItem()
            departamento.setText(funcionario.departamento)

            self.tbl_funcionarios.setItem(linha, 0, nome)
            self.tbl_funcionarios.setItem(linha, 1, sexo)
            self.tbl_funcionarios.setItem(linha, 2, salario)
            self.tbl_funcionarios.setItem(linha, 3, departamento)

    def abrir_dialog(self):
        dialog = CadastrarController(self)
        dialog.exec_()

class CadastrarController(QDialog, Ui_Cadastrar):

    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.btn_salvar.clicked.connect(self.salvar)
        self.lbl_mensagem.hide()

    
    def salvar(self):
        funcionario = Funcionario()
        funcionario.nome = self.edt_nome.text()
        funcionario.sexo = 'M' if self.cmb_sexo.currentIndex() == 0 else 'F'
        funcionario.salario = float(self.edt_salario.text())
        funcionario.departamento = self.edt_departamento.text()
        funcionario.salvar()
        self.lbl_mensagem.setVisible(True)
        self.lbl_mensagem.setText('Cadastrado com sucesso')
        utils.limpar_componentes(self.componentes)
        self.limpar_mensagem()


    def limpar_mensagem(self):
        self.timer = QTimer(self)
        self.timer.setInterval(2000)
        self.timer.timeout.connect(lambda : self.lbl_mensagem.hide())
        self.timer.start()