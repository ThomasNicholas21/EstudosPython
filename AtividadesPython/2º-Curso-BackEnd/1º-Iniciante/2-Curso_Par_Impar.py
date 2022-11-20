import re


def is_float(val):
    if isinstance(val, float):
        return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val):
        return True

    return False


def is_int(val):
    if isinstance(val, int):
        return True
    if re.search(r'^\-{,1}[0-9]+$', val):
        return True

    return False


def is_number(val):
    return is_int(val) or is_float(val)


'''
código
'''

num1 = input('Digite um número inteiro: ')

if is_int(num1):
    print('Número inteiro inserido! ')
    num1 = int(num1)

    if num1 % 2 == 0:
        print('Número par!')
    else:
        print('Número impar!')

else:
    print('Número inteiro necessário! ')
