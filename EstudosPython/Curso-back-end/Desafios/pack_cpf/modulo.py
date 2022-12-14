def apresentacao_dados(*args):
    cont = 1
    for i in args:
        print(f'Dado {cont}: {i}')
        cont += 1