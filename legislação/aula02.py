# 2 - Repetição Definida
# Peça ao usuário para digitar as 5 fontes do direito.
# Para cada fonte digitada, mostre “Fonte cadastrada com sucesso”
# se esta forma for válida.
# No final, exiba “Fim do cadastro”.


fonte = []
base = ['Constituição', 'lei', 'decreto', 'resolução', 'norma tecnica']
while True:
    entrada = str(input('escreva sua fonte ou sair: ')).lower().strip()

    if entrada in base:
        fonte.append(entrada)
        print(f'{entrada}, cadastrada com sucesso.')
        print(fonte)

    elif entrada not in base:
        print('nao estar correta')

    elif fonte == base:
        print('esta todos corretas')
        print(fonte)

    elif entrada == 'sair':
        print('saindo...')
        break
