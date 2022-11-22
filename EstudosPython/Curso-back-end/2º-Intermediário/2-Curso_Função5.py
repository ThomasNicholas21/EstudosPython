"""
Função
"""
import os

lista = []


def soma(*args):
    return print(f'Subtração = {a_int + b_int}')


def subtracao(*args):
    return print(f'Subtração = {a_int - b_int}')


def divisao(*args):
    return print(f'Divisão = {a_int / b_int}')


def multiplicacao(*args):
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
