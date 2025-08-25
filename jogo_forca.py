palavra_secreta = 'carro'

# Converter para lista para poder modificar
letra_descoberta = list('_' * len(palavra_secreta))
tentativa = 8

while tentativa > 0 and '_' in letra_descoberta:
    print(f'Palavra: {" ".join(letra_descoberta)}')
    print(f'Tentativas restantes: {tentativa}')

    letra = input('Digite uma letra: ').lower().strip()

    # Validar entrada
    if len(letra) != 1 or not letra.isalpha():
        print('Digite apenas uma letra válida!')
        continue

    if letra in palavra_secreta:
        print(f'Boa! A letra "{letra}" está na palavra!')
        # Substituir todas as ocorrências da letra
        for id, letra_secreta in enumerate(palavra_secreta):
            if letra == letra_secreta:
                letra_descoberta[id] = letra
    else:
        tentativa -= 1
        print(f'Ops! A letra "{letra}" não está na palavra.')

# Verificar resultado final
if '_' not in letra_descoberta:
    print(
        f'\n🎉 Parabéns! Você descobriu a palavra: {"".join(letra_descoberta)}')
else:
    print(f'\n😞 Game Over! A palavra era: {palavra_secreta}')
