profissionais = []
email_existente = False
while True:
    email = str(input('digite seu email ou ["sair"]: '))
    if email == 'sair':
        break

    for p in (profissionais):
        if p.get('Email') == email:
            print('email ja cadastrado!, por favor coloque outro')
            email_existente = True

    if email_existente:
        continue

    profissional = {'email': email}
    profissionais.append(profissional)
