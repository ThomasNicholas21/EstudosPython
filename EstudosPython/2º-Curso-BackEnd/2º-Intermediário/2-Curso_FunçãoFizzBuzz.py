from random import randint


def origin(x):
    if x % 5 == 0 and x % 3 == 0:
        return 'fizzbuzz'
    if x % 5 == 0:
        return 'buzz'
    if x % 3 == 0:
        return 'fizz'
    return x


for i in range(100):
    aleatorio = randint(0, 100)
    print(origin(aleatorio))
