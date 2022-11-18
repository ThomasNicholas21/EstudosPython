"""
Função
"""


def soma():
    a = input('Digite o primeiro valor: ')
    b = input('Digite o segundo valor: ')
    a_int = int(a)
    b_int = int(b)
    print(f'Soma = {a_int + b_int}')


def subtracao():
    a = input('Digite o primeiro valor: ')
    b = input('Digite o segundo valor: ')
    a_int = int(a)
    b_int = int(b)
    print(f'Subtração = {a_int - b_int}')


def divisao():
    a = input('Digite o primeiro valor: ')
    b = input('Digite o segundo valor: ')
    a_int = int(a)
    b_int = int(b)
    print(f'Divisão = {a_int / b_int}')


def multiplicacao():
    a = input('Digite o primeiro valor: ')
    b = input('Digite o segundo valor: ')
    a_int = int(a)
    b_int = int(b)
    print(f'Multiplicação = {a_int * b_int}')


while True:
    operador = input(
        'Selecione seu operador: '
        '\n[+] Soma '
        '\n[-] Subratração '
        '\n[/] Divisão '
        '\n[*] Multiplicação '
        '\nSelecione: '
    )

    if operador == '+':
        soma()
    elif operador == '-':
        subtracao()
    elif operador == '/':
        divisao()
    elif operador == '*':
        multiplicacao()
    else:
        print('Digite um operador.')

    sair = input('Deseja sair? [S]im ou [N]ão: ').lower().startswith('s')
    if sair is True:
        break
