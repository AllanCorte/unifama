#Classificação Etária
#Crie um programa que verifica se uma pessoa pode assistir a um filme classificado como "maiores de 16 anos".
#Dados:
#Idade da pessoa: Pergunte ao usuário

idade = int(input('qual é sua idade: '))

if idade > 16:
    print('ola voce pode assistir o filme')
else:
    print('infelizmente voce não tem idade suficiente para assitir')