# 1 - Prioridade do Stakeholder pelo Nível de Influência
# Crie um algoritmo que solicite o nome de um stakeholder e um valor numérico
#  representando seu nível de influência no projeto (de 0 a 10). Se o valor for
#  maior ou igual a 8, exiba que ele é um “Stakeholder de alta prioridade”. Se
# for entre 5 e 7, exiba “Stakeholder de prioridade média”. Caso contrário,
# exiba “Stakeholder de baixa prioridade

nome = str(input('qual o nome do stakeholder: '))
valor = int(input('digite um valor numérico de 0 a 10:'))

if valor >= 8 and valor <= 10:
    print(f'o {nome} é de alta prioridade')
elif valor >= 5 and valor <= 7:
    print(f'o {nome} é de media prioridade')
elif valor > 10:
    print('por favor de 0 a 10')
else:
    print('Stakeholder de baixa prioridade')
