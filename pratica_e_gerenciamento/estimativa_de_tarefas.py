# 2 - Estimativa de Tarefas por Stakeholder
# Faça um algoritmo que receba o nome de um stakeholder, o número total de
#  tarefas do projeto e a quantidade de stakeholders na equipe. Calcule e exiba
#  quantas tarefas cabem a cada um (divisão inteira). Se o valor por
# stakeholder for maior que 10, exiba a mensagem “Carga de trabalho alta”,
# senão “Carga de trabalho adequada”.
nome_da_stakeholder = str(input('qual o nome da stakeholder: '))
tarefas_do_projeto = int(input('quantas tarefas tem: '))
quantidade_de_stakeholds = int(input('quantidade de stakeholds na equipe: '))

resultado = (tarefas_do_projeto / quantidade_de_stakeholds)

if resultado > 10:
    print('Carga de trabalho alta')
else:
    print('carga de trabalho adequada')
