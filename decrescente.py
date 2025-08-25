# 4. Ordenando uma Lista
# Peça ao usuário para inserir uma lista de números (separados por espaço) e
# exiba a lista em ordem crescente e decrescente.

entrada = input('Digite números separados por espaços: ')
numeros = [float(num) for num in entrada.split()]

# Ordem crescente
numeros_cresc = sorted(numeros)

# Ordem decrescente
numeros_desc = sorted(numeros, reverse=True)

print(f'Números originais: {numeros}')
print(f'Ordem crescente: {numeros_cresc}')
print(f'Ordem decrescente: {numeros_desc}')
