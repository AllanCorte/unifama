# Crie um programa em Python que cadastre profissionais com email único, nome,
#  hard skills e soft skills. Cada profissional é armazenado em um dicionário
#  e adicionado a uma lista.
# Pergunte o email (o email deve ser único para cada profissional) e o nome.
# Inicie a repetição para cadastrar as hard skills do profissional, até que
# o usuário digite "sair".
# Após encerrar o cadastro das hard skills, inicie a repetição para cadastrar
# as soft skills, até que o usuário digite "sair".
# Ao finalizar o cadastro de um profissional, reinicie o processo para um
# novo profissional.
# O processo de cadastro de profissionais deve continuar até que o usuário
#  digite "sair" no campo de email.
# Cada profissional deve ser armazenado em um dicionário
# (com chaves: nome, email, hard skills, soft skills) e depois adicionado
# a uma lista de profissionais.

profissionais = []  # type: ignore
while True:
    email_existente = False
    email = str(input('digite seu email ou ["sair"]: '))
    if email == 'sair':
        break

    for p in (profissionais):
        if p.get('Email') == email:
            email_existente = True

    if email_existente:
        print('email ja cadastrado!, por favor coloque outro')
        continue

    nome = str(input('digite seu nome: '))

    hard_lista = []  # habilidades tecnicas
    while True:
        hard_skills = (input('Escreva sua Hard Skill, ou [sair]: '))
        if hard_skills == 'sair':
            break
        hard_lista.append(hard_skills)

    soft_lista = []  # habilidades comportamentais
    while True:
        soft_skills = (input('Escreva sua soft Skill, ou ["sair"]: '))
        if soft_skills == 'sair':
            break
        soft_lista.append(soft_skills)

    profissional = {'Nome': nome,
                    'Email': email,
                    'Hard-Skill': hard_lista,
                    'Soft-Skill': soft_lista
                    }

    profissionais.append(profissional)

print(profissionais)
