numero_1 = float(input('digite seu primeiro numero:'))
numero_2 = float(input('digite seu segundo numero:'))
operador = input('+ somar  - diminuir  * multiplicar  / dividir ')

if operador == '+' or operador == 'somar':
    resultado = numero_1 + numero_2 
    print(resultado)

elif operador == '-' or operador == 'diminuir':
    resultado = numero_1 - numero_2 
    print(resultado)

elif operador == '*' or operador == 'multiplicar':
    resultado = numero_1 * numero_2 
    print(resultado)

elif operador == '/' or operador == 'dividir':
    resultado = numero_1 / numero_2 
    print(resultado)

else: 
    print("operadores invalidos")