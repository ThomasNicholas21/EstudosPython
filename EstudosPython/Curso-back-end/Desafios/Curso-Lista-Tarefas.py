def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa listada.')
        return
    
    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()

def desfazer():
    print('Tarefa desfeita.\n')
    return tarefas_desfazer.append(tarefas.pop())

def refazer():
    print('Tarefa restaurada.\n')
    return tarefas.append(tarefas_desfazer.pop())

def adicionar(tarefa, tarefas):
    tarefa = tarefa.strip()
    if not tarefas:
        print('Isso não é uma tarefa.')
        return
    
    tarefas.append(tarefa)

tarefas = []
tarefas_desfazer = []

while True:

    print('Comandos: Listar, desfazer, refazer e sair.')
    op = input('Digite a tarefa ou comando: ')

    if op == 'listar':
        listar(tarefas)
    elif op == 'desfazer':
        desfazer()
    elif op == 'refazer':
        refazer()
    elif op == 'sair':
        break
    else:
        adicionar(op, tarefas)