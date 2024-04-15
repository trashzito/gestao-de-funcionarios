class Funcionario:
    def __init__(self, nome, id, salario):
        self.nome = nome
        self.id = id
        self.salario = salario

    def aumentar_salario(self, percentual):
        self.salario *= (1 + percentual / 100)

class Gerente(Funcionario):
    def __init__(self, nome, id, salario, departamento):
        super().__init__(nome, id, salario)
        self.departamento = departamento