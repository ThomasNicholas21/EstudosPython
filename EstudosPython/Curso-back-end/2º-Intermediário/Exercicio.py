from Exercício_dados import preenchedor_5, preenchedor_7
from os import system

lista1 = []
lista2 = []


opcao1 = input(
    'Como deseja preencher a primeira: \n'
    '[1] Lista de 5 números\n'
    '[2] Lista de 7 números\n'
    'Selecione: '
    )
system('cls')

if opcao1 == '1':
    lista1 = preenchedor_5()
    system('cls')

elif opcao1 == '2':
    lista1 = preenchedor_7()
    system('cls')

else:
    print('Voce nao selecionou o valor correspondente T_T ')
    system('cls')

print(f'Sua lista: {lista1}')
opcao2 = input(
    'O que deseja fazer:\n'
    '[1] - Inverter sua lista\n'
    '[2] - Multiplicar por 2\n'
    '[3] - Apenas Imprimir\n'
    '[4] - Preencher mais uma lista\n'
    'Selecione: '
    )

if opcao2 == '1':
    lista1 = [lista for lista in lista1[::-1]]
    print(f'Sua lista invertida: \n{lista1}')

elif opcao2 == '2':
    lista1 = [lista * 2 for lista in lista1]
    print(f'Sua lista multiplicada: \n{lista1}')

elif opcao2 == '3':
    print(f'Sua lista: \n{lista1}')

elif opcao2 == '4':
    opcao3 = input(
    'Como deseja preencher a segunda: \n'
    '[1] Lista de 5 números\n'
    '[2] Lista de 7 números\n'
    'Selecione: '
    )
    system('cls')

    if opcao3 == '1':
        lista2 = preenchedor_5()
        system('cls')

    elif opcao3 == '2':
        lista2 = preenchedor_7()
        system('cls')

    else:
        print('Voce nao selecionou o valor correspondente T_T ')
        system('cls')

    print(f'Suas listas: \n{lista1} e {lista2}')
    opcao4 = input(
    'O que deseja fazer:\n'
    '[1] - Somar as listas\n'
    '[2] - Multiplicar as listas\n'
    '[3] - Apenas Imprimir\n'
    'Selecione: '
    )

    if opcao4 == '1':
        lista_soma = [
            l1 + l2 for l1, l2 in zip(lista1, lista2)
        ]
        print(lista_soma)
    elif opcao4 == '2':
        lista_mult = [
            l1 * l2 for l1, l2 in zip(lista1, lista2)
        ]
        print(lista_mult)
    elif opcao4 == '3':
        print(f'Suas listas: \n{lista1} e {lista2}')
    else:
        print('Voce nao selecionou o valor correspondente T_T ')

else:
    print('Voce nao selecionou o valor correspondente T_T ')
