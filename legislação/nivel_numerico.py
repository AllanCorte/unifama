# 3 - Níveis Numéricos
# Peça ao usuário um número de 1 a 5, representando um nível hierárquico.
# Se for válido, mostre a fonte do direito correspondente
# Se for inválido, mostre “Nível inválido” e peça novamente.
# O programa encerra se o usuário digitar 0

numero = int(input('digite um numero de 1 a 5: '))

while True:
    if numero == 1:
        print('constituição')
    elif numero == 2:
        print('leis')
    elif numero == 3:
        print('decreto')
    elif numero == 4:
        print('resoluções')
    elif numero == 5:
        print('normas técnicas')
    elif numero == 0:
        print('saindo...')
        break
    else:
        'nivel invalido'
