"""
Sistema de cadastro
"""
import getpass
from os import system
from pack_cadastro import menu, cadastro, listagem_cadastro

pessoas = []
while True:
    menu()
    opcao = int(input('Selecione sua opção: '))

    if opcao == 1:
        cadastro(pessoas)
    elif opcao == 2:
        listagem_cadastro(pessoas)
    #elif opcao == 3:
    #elif opcao == 4:
    #elif opcao == 5:
    #else:
    