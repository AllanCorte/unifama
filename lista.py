# 1.	Lista de Tarefas
# Crie um programa que gerencia uma lista de tarefas. O usuário deve ser capaz
#  de:
# ●	Adicionar uma tarefa
# ●	Remover uma tarefa
# ●	Listar todas as tarefas

lista_de_tarefas = []


def adicionar(tarefa):
    if tarefa in lista_de_tarefas:
        return ('tarefa esta na lista')
    else:
        lista_de_tarefas.append(tarefa)
        return f' Tarefa "{tarefa}" adicionada com sucesso!'


def remover(tarefa):
    if tarefa not in lista_de_tarefas:
        return ('tarefa nao esta na lista')
    else:
        lista_de_tarefas.remove(tarefa)
        return f'Tarefa "{tarefa}" removida com sucesso!'


def listar():
    if not lista_de_tarefas:
        return 'nenhuma tarefa na lista'

    resultado = 'lista de tarefas \n'
    for id, item in enumerate(lista_de_tarefas, 1):
        resultado += f'{id} - {item}\n'
    return resultado


while True:
    print('\n' + '='*30)
    menu = input('Escolha um opção\n'
                 ' 1-adicionar\n'
                 ' 2-remover \n'
                 ' 3-listar \n'
                 ' 4-Sair \n'
                 'Digite sua opção: ')
    try:
        opcao = int(menu)
    except ValueError:
        print('digite apenas numeros de 1 a 4!')
        continue

    if opcao == 1:
        tarefa = input('digita sua tarefa: ')
        if tarefa.strip():
            (adicionar(tarefa))
        else:
            print('tarefa não pode estar vazia')

    elif opcao == 2:
        if lista_de_tarefas:
            print(listar())
            tarefa = input('digita sua tarefa queira remover: ')
            print(remover(tarefa))
        else:
            print('lista vazia! nao ha tarefas para remover.')

    elif opcao == 3:
        print(listar())

    elif opcao == 4:
        print('saindo')
        break

    else:
        print('opçao invalida! digite 1, 2, 3, 4')
