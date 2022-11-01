
def add(x, y, z):
    adição = x + y + z
    return adição


n1 = float(input('Digite primeiro numero: '))
n2 = float(input('Digite segundo numero: '))
n3 = float(input('Digite terceiro numero: '))

d = add(n1, n2, n3)
print(f'{d:.2f}')
