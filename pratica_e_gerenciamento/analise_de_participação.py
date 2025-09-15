# 3 - Análise de Participação no Projeto
# Crie um algoritmo que receba o nome de um stakeholder e o número de horas
#  semanais que ele participa do projeto. Se for maior que 20 horas, exiba
# “Participação intensa”. Se for maior ou igual a 10 e menor ou igual a 20,
#  exiba “Participação moderada”. Caso contrário, exiba “Participação baixa”.

nome_da_stakeholder = str(input('qual o nome da stakeholder: '))
numero_de_horas = int(input('quantos o numero de horas'))

if numero_de_horas > 20:
    print('participação intensa')
elif numero_de_horas >= 10 and numero_de_horas <= 20:
    print('participação moderada')
else:
    print('participação baixa')
