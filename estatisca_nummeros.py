# 2.	Estatísticas de Números
# Peça ao usuário para inserir uma lista de números (separados por espaço)
# e calcule:
# ●	O maior número
# ●	O menor número
# ●	A soma dos números
# ●	A média dos números
entrada = input('digite numeros separados por espaço:')
numeros = [float(num) for num in entrada.split()]

maior_numero = max(numeros)

menor_nummero = min(numeros)

soma = sum(numeros)

media = soma / len(numeros)

print(f' o maior numero {maior_numero}')
print('##')
print(menor_nummero)
print('##')
print(soma)
print('##')
print(media)
