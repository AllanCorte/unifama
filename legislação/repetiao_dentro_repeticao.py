# 4 - Repetição dentro de Repetição
# Monte um algoritmo que desenhe uma pirâmide de hierarquia de Fontes
# do Direito:
# O usuário digita um número N (até 5).
# O programa exibe uma pirâmide com * representando o nível.
# Exemplo para N=3:
nivel = int(input('digite um numero de 1 a 5: '))

for i in range(1, nivel + 1):
    print('*' * i)


posicao = int(input('posição da hierarquia: '))
linha = ' '
for numero in range(1, posicao + 1):
    for estrela in range(numero):
        if estrela == 0:
            linha = '*'
        else:
            linha += '*'
    print(linha)
