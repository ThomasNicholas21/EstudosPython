"""
Valida CPF e o Armazena numa lista
"""
import re
from os import system
from pack_cpf import validador_cpf, apresentacao_dados

armazenamento = []
while True:
    nome = input('Insira o nome: ')
    cpf = input('Insira o CPF: ')
    cpf_re = re.sub(r'[^0-9]', '', cpf)
    print()
    validador_cpf(cpf_re)
    if validador_cpf(cpf_re) is True:
        opcao = input(
            f'O nome : {nome},\n'
            f'O CPF : {cpf_re},\n'
            'Estão corretos!\n'
            'Deseja armazena-los ?\n[S]im ou [N]ão: '
            ).lower().startswith('s')
        

        if opcao is True:
            armazenamento.append((nome, cpf_re))

    else:
        print('Opa, algo deu errado, tente novamente!')
        continue
    
    print()
    acessar = input(
        'Deseja acessar os dados armazenados? [S]im ou [N]ao: '
        ).lower().startswith('s')
    if acessar is True:
        apresentacao_dados(*armazenamento)

    print()
    sair = input('Deseja sair? [S]im ou [N]ao: ').lower().startswith('s')
    if sair is True:
        break
    else:
        system('cls')
        continue
