# 2 - Consulta de Importância
# Crie um algoritmo que tenha um dicionário associando
#  cada stakeholder à sua importância:
# Superiores → definem recursos e prazos
# Usuários → determinam aceitação do produto
# Equipe → executa o trabalho
# Fornecedores → garantem recursos
# Comunidade → é impactada pelo projeto

stakeholder = {'Superiores': 'definem recursos e prazos',
               'Usuários': 'determinam aceitação do produto',
               'Equipe': 'executa o trabalho',
               'Fornecedores': 'garantem recursos',
               'Comunidade': 'é impactada pelo projeto'}

while True:
    tema = str(input('qual o tema que deseja perguntar? \n'
                     'ou ["sair"]: ')).strip().lower()

    if tema == 'sair':
        print('saindo...')
        break

    elif tema:
        resultado = (stakeholder.get(tema))
        if resultado is None:
            print('tema nao encontrado')
        else:
            print(resultado)
