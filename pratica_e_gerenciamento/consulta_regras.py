# 2 - Consulta de Regras Trabalhistas
# Crie um dicionário que associe um tema a uma regra da CLT. Exemplos:
# "horas_extras" → até 2h/dia, +50%, "jornada_semanal" → máximo 44h
# O programa deve perguntar o tema e mostrar a regra correspondente.
# Se o tema não existir, mostre “não encontrado”.
# Repita até digitar “sair”.
regras_trabalhistas = {
    "horas extras": "Até 2h/dia, acréscimo de 50% sobre a hora normal.",
    "jornada semanal": "Máximo de 44 horas semanais.",
    "ferias": "30 dias de férias a cada 12 meses de trabalho.",
    "descanso semanal": "Descanso semanal remunerado, preferencialmente aos"
    " domingos.",
    "13 salario": "Pagamento do 13º salário ao trabalhador."
}

while True:
    tema = str(input('qual o tema que deseja perguntar? \n'
                     'ou ["sair"]: ')).strip().lower()

    if tema == 'sair':
        print('saindo...')
        break

    elif tema:
        resultado = (regras_trabalhistas.get(tema))
        if resultado is None:
            print('tema nao encontrado')
        else:
            print(resultado)
