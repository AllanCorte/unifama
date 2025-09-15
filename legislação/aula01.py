# 1 - Consulta Simples
# Crie um algoritmo que pergunte ao usuário o tipo de norma (ex: Constituição,
#  Lei, Decreto, Resolução, Norma técnica).
# Mostre em qual nível hierárquico ela está.
# O programa encerra quando o usuário digitar “sair”.


while True:
    norma = int(input('digite o numero da tipo de norma\n'
                      '1- Constituição\n'
                      '2-lei\n'
                      '3-decreto\n'
                      '4-resolução\n'
                      '5-norma tecnica\n'
                      '6-sair\n'
                      'digite sua opção: '))

    if norma == 1:
        print('sua norma é constituição e estar no nivel 1')
        break
    elif norma == 2:
        print('sua norma é a Lei e estar no nivel 2')
        break
    elif norma == 3:
        print('sua norma é a decreto e estar no nivel 3')
        break
    elif norma == 4:
        print('sua norma é a resolução e estar no nivel 4')
        break
    elif norma == 5:
        print('sua norma é a norma tecnica e estar no nivel 5')
        break
    elif norma == 6:
        print('saindo...')
        break
    else:
        print('digite só numeros por favor')
