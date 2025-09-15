# 4 - Conversão de multa internacional
# Peça ao usuário o valor da multa em dólares e a cotação atual do dólar.
# Converta o valor para reais e exiba junto com um aviso de proteção autoral.
valor_da_multa = float(input('qual o valor da multa em dolar?: '))
cotacao_atual = float(input('qual a cotação atual do dolar: '))

multa_convertida = (valor_da_multa * cotacao_atual)

print(f'a multa de R$: {multa_convertida:.2f} devido a proteção'
      'e política de uso não autorizado')
