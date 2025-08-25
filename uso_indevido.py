# 3 - Cálculo de indenização por uso indevido
# Pergunte o valor de mercado de um software e quantas cópias não autorizadas
#  foram encontradas. Calcule o valor total da indenização (valor × quantidade)
#  e exiba junto de um aviso de “uso não autorizado”.
valor_software = float(input('qual o valor de mercado do software: '))
copias = int(input('quantas copias não autorizadas foram encontradas?: '))

Idenizacao = valor_software * copias

print(f'Aviso legal informando que o uso não autorizado do software é \n'
      f'proibido o valor da multa calculada. {Idenizacao:.3f}'
      )
