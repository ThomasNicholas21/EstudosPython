"""
Utilizando raise para tratamento de erros
"""
def divisor_nao_pode_ser_zero(b):
    if b == 0:
        raise ValueError('Não pode ter divisão por zero.')
    return True

def numerador_int_ou_float(a):
    if not isinstance(a, (int, float)):
        raise TypeError(f'{a} não é um número.')
    return True

def divisor_int_ou_float(b):
    if not isinstance(b, (int, float)):
        raise TypeError(f'{b} não é um número.')
    return True

def divisao(a, b):
    numerador_int_ou_float(a)
    divisor_int_ou_float(b)
    divisor_nao_pode_ser_zero(b)
    return print('Divisão = ', a / b)

def receber_dados():
    a = 22
    b = 'teste'
    divisao(a, b)

receber_dados()