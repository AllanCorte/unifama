profissionais = []


while True:
    email = input('Digite seu email ou ["sair"]: ').strip().lower()
    if email == 'sair':
        break

    elif '@gmail.com' not in email:
        print('o email deve conter @gmail.com')
        continue

    email_existente = False
    for p in profissionais:
        if p.get('Email') == email:
            email_existente = True
            break

    if email_existente:
        print('Email já cadastrado! Por favor, coloque outro.')
        continue

    nome = input('Digite seu nome: ').strip()

    hard_lista = []
    while True:
        hard_skill = input(
            'Escreva sua Hard Skill, ou [sair]: ').strip().lower()
        if hard_skill == 'sair':
            break
        else:
            hard_lista.append(hard_skill)

    soft_lista = []
    while True:
        soft_skill = input(
            'Escreva sua Soft Skill, ou [sair]: ').strip().lower()
        if soft_skill == 'sair':
            break
        else:
            soft_lista.append(soft_skill)

    profissional = {
        'Nome': nome,
        'Email': email,
        'Hard-Skill': hard_lista,
        'Soft-Skill': soft_lista
    }

    profissionais.append(profissional)


titulo_vaga = input('Qual o título da vaga: ').strip()

lista_hards_skills_exigidas = []
while True:
    hard_skill_exigida = input(
        'Escreva a Hard Skill exigida, ou [sair]: ').strip().lower()
    if hard_skill_exigida == 'sair':
        break
    else:
        lista_hards_skills_exigidas.append(hard_skill_exigida)

lista_softs_skills_exigidas = []
while True:
    soft_skill_exigida = input(
        'Escreva a Soft Skill exigida, ou [sair]: ').strip().lower()
    if soft_skill_exigida == 'sair':
        break
    else:
        lista_softs_skills_exigidas.append(soft_skill_exigida)

vaga = {
    'titulo': titulo_vaga,
    'hards_skills': lista_hards_skills_exigidas,
    'softs_skills': lista_softs_skills_exigidas
}

ranking = []

for pessoa in profissionais:
    hard_match = []
    for comp in pessoa['Hard-Skill']:
        if comp in vaga['hards_skills']:
            hard_match.append(comp)

    soft_match = []
    for comp in pessoa['Soft-Skill']:
        if comp in vaga['softs_skills']:
            soft_match.append(comp)

    pontos = len(hard_match) * 2 + len(soft_match)

    ranking.append({
        'Nome': pessoa['Nome'],
        'Email': pessoa['Email'],
        'Pontuação': pontos,
    })

maior_pontuacao = 0
top = None

for r in ranking:
    if r['Pontuação'] > maior_pontuacao:
        maior_pontuacao = r['Pontuação']
        top = r

if maior_pontuacao > 0:
    print(f'{vaga['titulo']}')
    print(f'Nome: {top['Nome']}')
    print(f'Email: {top['Email']}')
else:
    print('Nenhum profissional cadastrado ou ninguém atingiu '
          'pontuação maior que zero.')
