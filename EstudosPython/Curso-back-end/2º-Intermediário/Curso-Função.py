"""
Retorno de valores das Funções com 'return'
"""


def multiplicacao(x, y):
    return x * y


repetições = input('Quantas vezes deseja multiplicar: ')
repetições_int = int(repetições)
soma = 0
contador = 0

for i in range(repetições_int):
    x = int(input('Digite o primeiro valor: '))
    y = int(input('Digite o segundo valor: '))
    soma = soma + multiplicacao(x, y)
    contador += 1
    print(f'{contador}ª multiplicação = {multiplicacao(x, y)} \n')

print(f'soma total da multiplicação = {soma}')
