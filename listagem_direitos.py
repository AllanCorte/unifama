# 1 - Listagem de Direitos da CLT
# Crie uma lista com 5 direitos trabalhistas garantidos pela CLT:
# Ex: Jornada de trabalho, Horas extras, Férias.. etc
# Mostre cada direito numerado de 1 a 5.

direitos_trabalhistas = ["Jornada de trabalho limitada", "Férias anuais",
                         "Descanso semanal remunerado", "13° salário",
                         "Horas extras remuneradas"]


for i, direitos in enumerate(direitos_trabalhistas, 1):
    print(f'{i} - {direitos}')
