# 3 - Cadastro de Equipe
# Crie um algoritmo que permita cadastrar os membros de uma equipe de projeto.
#  O programa deve:
# Perguntar quantos membros serão cadastrados.
# Para cada membro, pedir o nome e a função.
# Guardar cada membro como um dicionário ({"nome": ..., "funcao": ...})
# dentro de uma lista chamada equipe.
# Ao final, mostrar todos os membros cadastrados

equipe = []

quantidades_de_menbros = int(input('quantos menbros serão cadastrados: '))
for i in range(quantidades_de_menbros):
    nome = str(input('qual o seu nome: '))
    funcao = str(input('qual sua função'))
    dicionario = {'nome': nome, 'função': funcao}
    equipe.append(dicionario)

print(equipe)
