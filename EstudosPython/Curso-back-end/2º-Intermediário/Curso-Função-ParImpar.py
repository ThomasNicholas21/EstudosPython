"""
Função que fala se o número é par ou impar
"""


def parimpar(x):
    if x % 2 == 0:
        return print(f'{x} é par')
    return print(f'{x} é impar')


parimpar(4)
