listar = []
desfazer = []

while True:

    print('Comandos: Listar, desfazer e refazer.')
    op = input('Digite a tarefa ou comando: ').lower()
    print()

    if op == 'listar':
        print('Tarefas:\n', *listar, sep='\n')
        print()
    elif op == 'desfazer':
        desfazer.append(listar.pop())
    elif op == 'refazer':
        listar.append(desfazer.pop())
    else:
        listar.append(op)