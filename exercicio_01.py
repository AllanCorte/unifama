#Crie um programa que declare as seguintes variáveis:
#● nome: seu nome.
#● idade: sua idade.
#● altura: sua altura.
#● estudante: se você é estudante ou não (True/False).

nome = 'allan'
idade = 23
altura = 1.80
estudando = False

#Calcule o ano de nascimento com base na idade (considerando que o ano atual é 2025)
ano_nascimento = 2025 - idade

#Verifique se a pessoa é maior de idade (idade >= 18) e armazene o resultado em uma
#variável booleana.

maior_idade = idade >= 18

print(f'o meu nome é {nome}, e minha idade é {idade}, eu tenho {altura}, e estou estudando {estudando}')
print(f'o meu ano de nascimento é {ano_nascimento} é sou maior de idade {maior_idade}')