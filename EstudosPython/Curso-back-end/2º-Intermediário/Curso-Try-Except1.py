"""
TRY e EXCEPT
"""

# a = int(input('A: '))
# b = int(input('B: '))
# c = a / b

try:
    a = int(input('A: '))
    b = int(input('B: '))
    #  b = input('B: ') ativa o typerror 
    c = a / b
    print(c)

except ZeroDivisionError:
    print('Divisão por zero')

except ValueError:
    print('Valor invalido')

except (TypeError, IndexError):
    print('Erros: tipo e index')

except Exception:
    print('Erro desconhecido')
