# 3 - Cadastro de Funcionários e Jornada
# Peça quantos funcionários serão cadastrados.
# Para cada um, pergunte:
# Nome
# Horas semanais trabalhadas
# Armazene cada funcionário como um dicionário dentro de uma lista.
#  Ao final, mostre todos cadastrados.

class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        self._idade = idade


class Funcionario(Pessoa):
    def __init__(self, nome, idade, horas):
        super().__init__(nome, idade)
        self.horas = horas

    def __str__(self):
        return (f'nome: {self.nome}, idade: {self.idade}, '
                f'horas: {self.horas}')


class Cadastro:
    def __init__(self):
        self.funcionarios = []

    def adicionar_cadastro(self, funcionario):
        self.funcionarios.append(funcionario)

    def mostrar_funcionario(self):
        for i in self.funcionarios:
            print(i)


if __name__ == '__main__':

    cadastro = Cadastro()

    numero_de_funcionarios = int(
        input('quantos funcionarios serao cadastrados: '))

    for n in range(numero_de_funcionarios):

        nome = str(input('seu nome: '))
        idade = int(input('qual sua idade:'))
        horas = float(input(' quantas horas semanais: '))

        p1 = Funcionario(nome, idade, horas)
        cadastro.adicionar_cadastro(p1)

    cadastro.mostrar_funcionario()
