# 4 - Comparação de Stakeholders
# Desenvolva um algoritmo que receba o nome e o nível de influência (0 a 10)
# de dois stakeholders. Compare os valores e exiba qual stakeholder tem mais
#  influência. Se forem iguais, exiba a mensagem “Stakeholders com influência
#  equivalente”.

nome1 = str(input('qual o nome do stakeholder: '))
valor1 = int(input('digite um valor numérico de 0 a 10:'))

nome2 = str(input('qual o nome do stakeholder: '))
valor2 = int(input('digite um valor numérico de 0 a 10:'))

if valor1 > valor2:
    print(f'{nome1} tem mais influencia')

elif valor2 > valor1:
    print(f'{nome2} tem mais influencia')

else:
    print('Stakeholders com influência equivalentes')
