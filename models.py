class Funcionario:

    def __init__(self, **parametros) -> None:
        self.nome = parametros.get('nome')
        self.sexo = parametros.get('sexo')
        self.salario = parametros.get('salario')
        self.departamento = parametros.get('departamento')

    def salvar(self):
        linha = f'{self.nome},{self.sexo},{self.salario},{self.departamento}\n'
        with open('db.txt', 'a') as arquivo:
            arquivo.write(linha)
