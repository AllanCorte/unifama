# 3.	Contagem de Caracteres em uma String
# Peça ao usuário para inserir uma frase e
# conte quantas vezes cada letra aparece.

entrada = input('escreva uma frase: ').lower()
letras: dict[str, int] = {}

for caratere in entrada:
    if caratere.isalpha():
        # Esta linha substitui todo o if/else que você tinha
        letras[caratere] = letras.get(caratere, 0) + 1

for letra, contagem in letras.items():
    print(letra, contagem)

print(letras)
