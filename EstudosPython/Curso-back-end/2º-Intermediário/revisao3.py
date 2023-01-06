# Revisando módulo
from revisao import produtos
from os import system

carrinho_de_compra = []
while True:
    escolha = input(
        'Produtos disponiveis:\n'
        'Perfume - [1]\n'
        'Celular - [2]\n'
        'Mouse   - [3]\n'
        'Monitor - [4]\n'
        'Qual das opcoes deseja: '
    )
    print()
    
    if escolha == '1':
        print(produtos['Perfume'])
        print('O valor é de:', produtos['Valor 1'])
        print()
    elif escolha == '2':
        print(produtos['Celular'])
        print('O valor é de:', produtos['Valor 2'])
        print()
    elif escolha == '3':
        print(produtos['Mouse'])
        print('O valor é de:', produtos['Valor 3'])
        print()
    elif escolha == '4':
        print(produtos['Monitor'])
        print('O valor é de:', produtos['Valor 4'])
        print()
    else:
        print('Um erro ocorreu, tente novamente.')

    compra = input(
        'Deseja colocar no carrinho de compra? [S]im ou [N]ão: '
    ).lower().startswith('s')
    if compra is True:
        carrinho_de_compra.append(escolha)
        print('Produto encaminhado para o seu Carrinho de compras 😀')
        system('cls')
    
    sair = input(
            'Deseja realizar a compra e sair? [S]im ou [N]ão: '
    ).lower().startswith('s')
    if sair is True:
        print('Compra(s) realizada(s) com sucesso!')
        print(f'Produtos adquiridos: {carrinho_de_compra}')
        break
    else:
        system('cls')
        print(f'Produtos: {carrinho_de_compra}, estão no carrinho.')
        continue
    
