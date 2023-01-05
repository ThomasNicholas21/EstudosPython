# Revisando módulo
from revisao import produtos

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
    elif escolha == '2':
        print(produtos['Celular'])
    elif escolha == '3':
        print(produtos['Mouse'])
    elif escolha == '4':
        print(produtos['Monitor'])
    else:
        print('Um erro ocorreu, tente novamente.')
    
