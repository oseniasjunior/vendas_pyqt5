from PyQt5.QtWidgets import ( 
    QMainWindow, 
    QLabel, 
    QVBoxLayout, QWidget, QLineEdit, QComboBox, QSpacerItem, QSizePolicy, QPushButton
)
from models import Funcionario
import utils

class MainForm(QMainWindow):

    def __init__(self, parent = None) -> None:
        super().__init__(parent)

        self.setStyleSheet("""
            QWidget {
                font-size: 16px;
            }
            QLabel {
                color: red;
            }
        """)

        self.label_nome = QLabel()
        self.label_nome.setText('Nome')

        self.line_edit_nome = QLineEdit()
        self.line_edit_nome.setFixedHeight(40)

        self.label_sexo = QLabel()
        self.label_sexo.setText('Sexo')

        self.combo_box_sexo = QComboBox()
        self.combo_box_sexo.setFixedHeight(40)
        self.combo_box_sexo.addItems(['Masculino', 'Feminino'])

        self.label_salario = QLabel()
        self.label_salario.setText('Salário')

        self.line_edit_salario = QLineEdit()
        self.line_edit_salario.setFixedHeight(40)

        self.label_departamento = QLabel()
        self.label_departamento.setText('Departamento')

        self.line_edit_departamento = QLineEdit()
        self.line_edit_departamento.setFixedHeight(40)

        self.button_salvar = QPushButton()
        self.button_salvar.setText('Salvar')
        self.button_salvar.clicked.connect(self.salvar)

        space = QSpacerItem(0, 0, QSizePolicy.Fixed, QSizePolicy.Expanding)

        layout = QVBoxLayout()
        layout.addWidget(self.label_nome)
        layout.addWidget(self.line_edit_nome)
        layout.addWidget(self.label_sexo)
        layout.addWidget(self.combo_box_sexo)
        layout.addWidget(self.label_salario)
        layout.addWidget(self.line_edit_salario)
        layout.addWidget(self.label_departamento)
        layout.addWidget(self.line_edit_departamento)
        layout.addWidget(self.button_salvar)
        layout.addItem(space)

        self.componentes = QWidget()
        self.componentes.setLayout(layout)

        self.setCentralWidget(self.componentes)

        self.setWindowTitle('Meu primeiro formulário com PyQt5')
        self.setGeometry(60, 60, 800, 400)


    def salvar(self):
        funcionario = Funcionario()
        funcionario.nome = self.line_edit_nome.text()
        funcionario.sexo = 'M' if self.combo_box_sexo.currentIndex() == 0 else 'F'
        funcionario.salario = float(self.line_edit_salario.text())
        funcionario.departamento = self.line_edit_departamento.text()
        funcionario.salvar()
        utils.limpar_componentes(self.componentes)