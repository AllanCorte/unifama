notas = []
n = 1
while n <= 4:
    n += 1
    entrada = input('digite sua nonta ou [sair] para finalizar:')
    if entrada.lower() == 'sair':
        break
    else:
        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print('nota invalida digite so numero de 1 a 10')
        except ValueError:
            print('digite apenas numeros')

resultado = (sum(notas)) / (len(notas))
print(resultado)

maior_nota = max(notas)
print(maior_nota)

menor_nota = min(notas)
print(menor_nota)
