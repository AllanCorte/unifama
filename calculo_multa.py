# 1 -Cálculo de multa por uso não autorizado
# Peça ao usuário o valor de um software e a porcentagem de multa prevista em
# contrato por uso indevido. Calcule e exiba o valor total da multa,
# acompanhado de uma mensagem com o nome do usuário.

nome = str(input('qual o seu nome: '))
valor_software = float(input('qual o valor de um software: '))
porcentagem = int(input('qual o porcentagem da multa: '))

multa = valor_software * (porcentagem / 100)

print(
    f'Olá SR.{nome} o valor do software é {valor_software:.2f} '
    f'e a porcentagem\n'
    f'de multa {porcentagem:.2f} o valor que deverá ser pago {multa:.2f}'
)
