"""
Lista de compras
"""

lista = []
while True:
    print('Lista de Compras')
    opção = input(
                'Deseja:'
                '\n[I]nserir'
                '\n[A]pagar'
                '\n[L]istar'
                '\nEscolha: '
                ).lower()
            
    if opção == 'i':
        valor = input('Insira o valor: ')
        lista.append(valor)

    elif opção == 'a':
        try:
            indice = input(f'Qual indice deseja apagar: {lista} : ')
            indice_int = int(indice)
            del lista[indice_int]

        except IndexError:
            print('\nEsse indice não existe na lista.')
        
        except ValueError:
            print('\nDigite apenas numeros.')

    elif opção == 'l':
        if len(lista) == 0:
            print('Não a nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    
    else:
        print('Digite "I", "A" ou "L".')
        continue

    if len(lista) == 5 or len(lista) == 10 or len(lista) == 15:    
        sair = input('Deseja sair? [S]im ou [N]ão : ').lower().startswith('s')
        if sair is True:
            break