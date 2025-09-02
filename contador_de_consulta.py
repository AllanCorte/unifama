# 4 - Contador de Consultas de Jornada
# Crie um programa que pergunte repetidamente o nome de um funcionário
#  e suas horas semanais.
# “Está dentro da jornada” se estiver dentro do periodo de horas
#  definidos pela CLT
# “Está acima da jornada” se estiver acima do periodo de horas definidos
#  pela CLT
# Conte quantas consultas foram feitas. Ao final exiba: “Você consultou
# x (quantidade de trabalhadores) trabalhadores, sendo x dentro da jornada
#  e x acima da jornada”

consultas = 0
dentro_da_jornada = 0
acima_da_jornada = 0

while True:
    nome = input('escreva qual seu nome ou ["sair"] para sair: ').lower()

    if nome == 'sair':
        print(f'foram feitas {consultas} consultas,\n'
              f' sendo {dentro_da_jornada} dentro da jornada,\n',
              f'e {acima_da_jornada} acima da jornada')
        break

    horas = float(input('quantas horas semanais: '))

    if horas <= 44:
        print('Está dentro da jornada” se estiver dentro do periodo de horas '
              'definidos pela CLT')
        dentro_da_jornada += 1
    else:
        print('Está acima da jornada” se estiver acima do periodo de'
              ' horas definidos')
        acima_da_jornada += 1

    consultas += 1
