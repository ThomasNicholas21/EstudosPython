def perc(x, y):
    add = x + x*(y/100)
    return add


n1 = float(input('Insira o primeiro numero: '))
n2 = float(input('Insira o segundo numero: '))

d = perc(n1, n2)
print(d)
