# raise tratamento de erro

def deve_ser_int_float(n):
    tipo = type(n)
    if not isinstance(n, (int, float)):
        raise TypeError (
            f'O numero {n} deve ser inteiro'
        )
    return n

def probido_zero(d):
    if d == 0:
        raise ZeroDivisionError (
            f'Não divido por zero!'
        )
    return d

def divisao(n, d):
    deve_ser_int_float(n)
    deve_ser_int_float(d)
    probido_zero(d)
    return n / d

def cria_funcao(funcao, *args):
    return funcao(*args)

divide_0 = cria_funcao(divisao, 1, 0)
print(divide_0)