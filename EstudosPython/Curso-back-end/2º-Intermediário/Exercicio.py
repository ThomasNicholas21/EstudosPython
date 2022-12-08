from Exercício_dados import preenchedor_5, preenchedor_7
from os import system

lista1 = []
lista2 = []


opcao1 = input(
    'Qual deseja preencher primeiro: \n'
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
    '[4] - Preencher mias uma lista\n'
    'Selecione: '
    )

if opcao2 == '1':
    lista1 = [lista for lista in lista1[::-1]]
    print(f'Sua lista invertida: \n{lista1}')
if opcao2 == '2':
    lista1 = [lista * 2 for lista in lista1]
    print(f'Sua lista multiplicada: \n{lista1}')
if opcao2 == '3':
    print(f'Sua lista: \n{lista1}')
