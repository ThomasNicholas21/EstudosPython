"""
Atividade com módulo
"""
import os
from Curso1 import somar, subtrair, dividir, multiplicar # type: ignore

armazenamento = []
while True:   
    a = input('Digite o primeiro número: ')
    b = input('Digite o segundo número: ')

    try:
        a = int(a)
        b = int(b)

    except ValueError:
        print('Valor invalido!')
        continue

    except Exception:
        print('Algo deu errado, tente novamente!')
        continue
    
    print()
    operador = input(
        '| Digite seu operador:|\n'
        '| [+] - Soma          |\n'
        '| [-] - Subtração     |\n'
        '| [/] - Divisão       |\n'
        '| [*] - Multiplicação |\n'
        'Qual deseja: '
        ).lower()
    
    if operador == '+':
        soma = somar(a, b)
        print(f'{a} + {b} = ', soma)
        armazenamento.append(soma)
    elif operador == '-':
        subtracao = subtrair(a, b)
        print(f'{a} - {b} = ', subtracao)
        armazenamento.append(subtracao)
    elif operador == '/':
        divisao = dividir(a, b)
        print(f'{a} / {b} = ', divisao)
        armazenamento.append(divisao)
    elif operador == '*':
        multiplicacao = multiplicar(a, b)
        print(f'{a} x {b} = ', multiplicacao)
        armazenamento.append(multiplicacao)
    else:
        print('Operação inválida tente novamente!')
        continue
    
    print('Valores finais operados: ', armazenamento)
    print()
    sair = input('Deseja sair? [S]im ou [N]ão: ').lower().startswith('s')
    if sair is True:
        break
    else:
        os.system('cls')
    