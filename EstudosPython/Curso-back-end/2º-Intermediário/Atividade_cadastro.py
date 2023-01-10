"""
Sistema de cadastro
"""
import getpass
from os import system
from pack_cadastro import menu, cadastro, listagem_cadastro, busca_cadastro,remocao_cadastro

pessoas = []
while True:
    menu()
    opcao = input('Selecione sua opção: ')

    if opcao == '1':
        cadastro(pessoas)
    elif opcao == '2':
        listagem_cadastro(pessoas)
    elif opcao == '3':
        busca_cadastro(pessoas)
    elif opcao == '4':
        remocao_cadastro(pessoas)
    elif opcao == '5':
        sair = input('Deseja sair? [S]im ou [N]ão: ').lower().startswith('s')
        if sair is True:
            break
        else:
            continue
    else:
        print('Comando inválido.')
        continue
    