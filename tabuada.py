# Tabuada de um Número
# Peça ao usuário um número inteiro e exiba a tabuada desse número de 1 a 10.

numero = int(input('digite  um numero interio para a taboada: '))

for i in range(0, 11):
    print(f'{numero} x {i} = {numero * i}')
