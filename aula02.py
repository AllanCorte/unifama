fonte = []

base = ['allan', 'corte']
while True:
    entrada = str(input('escreva sua fonte ou sair: ')).lower().strip()

    if entrada in base:
        fonte.append(entrada)
        print(f'{entrada}, cadastrada com sucesso.')
        print(fonte)
        continue
    elif entrada not in base:
        print('nao estar correta')
        continue
    elif fonte == base:
        print('esta todos corretas')
        print(fonte)
        break
    elif entrada == 'sair':
        print('saindo...')
        break
