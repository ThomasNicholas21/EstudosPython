"""
Função que multiplica argumentos não nomeados
"""


def multiplicacao(*args):
    total = 1
    for i in args:
        total *= i
    return total


x = multiplicacao(1*2*3*4*5*6)
print(x)
