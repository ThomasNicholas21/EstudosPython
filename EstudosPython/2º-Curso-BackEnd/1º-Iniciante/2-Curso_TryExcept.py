"""
Try e except
"""

valor = input('Digite um número para ser dobrado: ')

try:
    valor = float(valor)
    print(f'Número dobrado é: {valor * 2}')
except:
    print('Dever ser digitado um número')
