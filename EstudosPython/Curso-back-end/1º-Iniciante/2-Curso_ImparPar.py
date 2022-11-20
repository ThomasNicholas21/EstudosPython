"""
Atividade
"""

numero = input('Digite um número: ')


try:
    numero = int(numero)
    par = numero % 2 == 0
    validação = 'ímpar'

    if par:
        validação = 'par'

    print(f'Numero {numero} é {validação}')

except:
    print('Você não digitou um numero intero.')
