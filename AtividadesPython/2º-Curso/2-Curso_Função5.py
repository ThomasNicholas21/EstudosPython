"""
Função
"""

def soma(a, b):
    print(f'Soma = {a + b}')


def subtracao(a, b):
    print(f'Subtração = {a - b}')


def divisao(a, b):
    print(f'Divisão = {a / b}')


def multiplicacao(a, b):
    print(f'Multiplicação = {a * b}')


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
    if sair is True:
        break
