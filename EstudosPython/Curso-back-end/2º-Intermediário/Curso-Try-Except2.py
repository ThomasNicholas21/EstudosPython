"""
TRY e EXCEPT
"""

# a = int(input('A: '))
# b = int(input('B: '))
# c = a / b

try:
    a = int(input('A: '))
    b = int(input('B: ')) 
    c = a / b
    print(c)
except ZeroDivisionError as error:
    print('MSG: ', error.__class__.__name__)
    print(error)

except ValueError:
    print('Valor invalido')

except (TypeError, IndexError):
    print('Erros: tipo e index')

except Exception:
    print('Erro desconhecido')
