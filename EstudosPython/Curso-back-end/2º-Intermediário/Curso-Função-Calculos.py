'''
Funções
'''


def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def divisao(a, b):
    return a / b


def multiplicacao(a, b):
    return a * b


a = int(input('Digite a:'))
b = int(input('Digite b: '))

s = soma(a, b)
d = divisao(a, b)
m = multiplicacao(a, b)
sub = subtracao(a, b)

print(f'soma = {s},subtração = {sub} divisão = {d}, multiplicação = {m}')
