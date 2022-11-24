"""
Função - Calculadora, sem tratamento de erros
"""
import os

lista = []


def soma(a_int, b_int):
    return print(f'Subtração = {a_int + b_int}')


def subtracao(a_int, b_int):
    return print(f'Subtração = {a_int - b_int}')


def divisao(a_int, b_int):
    return print(f'Divisão = {a_int / b_int}')


def multiplicacao(a_int, b_int):
    return print(f'Multiplicação = {a_int * b_int}')


while True:
    operador = input(
        'Selecione seu operador: '
        '\n[+] Soma '
        '\n[-] Subratração '
        '\n[/] Divisão '
        '\n[*] Multiplicação '
        '\nSelecione: '
    )

    a = input('Digite o primeiro valor: ')
    b = input('Digite o segundo valor: ')
    a_int = int(a)
    b_int = int(b)

    if operador == '+':
        soma(a_int, b_int)
    elif operador == '-':
        subtracao(a_int, b_int)
    elif operador == '/':
        divisao(a_int, b_int)
    elif operador == '*':
        multiplicacao(a_int, b_int)
    else:
        print('Digite um operador.')

    sair = input('Deseja sair? [S]im ou [N]ão: ').lower().startswith('s')
    os.system('cls')
    if sair is True:
        break
    else:
        lista.append(operador)

print(lista)
