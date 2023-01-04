#calculadora basic

def soma(a, b):
    add = a + b
    return add

def multiplicacao(a, b):
    mult = a * b
    return mult

def subtracao(a, b):
    sub = a - b
    return sub

def divisao(a, b):
    div = a / b
    return div

def potencia(a, b):
    pot = a**b
    return pot

operacao = input(
    'Digite a operação:\n'
    'soma [1]\n'
    'subtracao [2]\n'
    'multiplicacao [3]\n'
    'divisao [4]\n'
    'potencia [5]\n'
    'Escolha: '
)
n1 = input('Primeiro numero: ')
n2 = input('Segundo numero: ')
n1 = int(n1)
n2 = int(n2)

if operacao == '1':
    adicao = soma(n1, n2)
    print(adicao)
elif operacao == '2':
    sub = subtracao(n1, n2)
    print(sub)
elif operacao == '3':
    mult = multiplicacao(n1, n2)
    print(mult)
elif operacao == '4':
    div = divisao(n1, n2)
    print(div)
elif operacao == '5':
    pot = potencia(n1, n2)
    print(pot)
else:
    print('Opercao invalida')


