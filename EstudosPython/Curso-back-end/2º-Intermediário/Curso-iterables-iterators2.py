"""
generator expression, iterables e iterators
"""


def generator(a, b):
    while True:
        yield a
        a += 1

        if a > b:
            return


a = int(input('A: '))
b = int(input('B: '))

gen = generator(a, b)
for i in gen:
    print(i)

print()
# yiend from


def gen1():
    yield 1
    yield 2
    yield 3


def gen2():
    yield from gen1()
    yield 4
    yield 5
    yield 6


g = gen2()
for numero in g:
    print(numero)
