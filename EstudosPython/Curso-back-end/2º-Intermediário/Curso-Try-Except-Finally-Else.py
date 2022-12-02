"""
Try, except, finally and else
"""
# a = int(input('A: '))
# b = int(input('B: '))

try:
    a = int(input('A: '))
    b = int(input('B: '))
    c = a * b
except ValueError as error:
    print(error.__class__.__name__)
else:
    print(c)
finally:
    print('Multiplicação realizada.')
    





