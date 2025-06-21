#4.	Verificando Ano Bissexto
#Crie um programa que verifica se um ano é bissexto.
#●	Um ano é bissexto se for divisível por 4.
#●	Mas não é bissexto se for divisível por 100, exceto se for divisível por 400.

ano = int(input('digite um ano: '))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0 ) :
    print(f"o ano {ano}, é bissexto")
else:
    print(f'o {ano}, nao é bissexto')