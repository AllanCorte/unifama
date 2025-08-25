# 2 - Tempo de proteção autoral
# Solicite ao usuário o ano de criação de um software e calcule quantos anos de
#  proteção restam, considerando que no Brasil os direitos autorais de software
#  duram 50 anos a partir da publicação. Exiba o resultado
# com uma mensagem explicativa.
ano_criacao = int(input('digite qual o ano de criação: '))
ano_atual = 2025
limite_protecao = ano_criacao + 50
resto_protecao = limite_protecao - ano_atual

if resto_protecao <= 0:
    print('infelizmente você não tem proteção ')
elif resto_protecao >= 0:
    print(f'voce ainda tem {resto_protecao} anos de proteção')
else:
    print('por somente numeros inteiros')
