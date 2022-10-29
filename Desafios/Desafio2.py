from random import randint

cpf = str(randint(10000000000, 99999999999))
n_cpf = cpf
rev = 10
tl = 0

for x in range(19):
    if x > 8:
        x -= 9

    tl += int(n_cpf[x]) * rev

    rev -= 1
    if rev < 2:
        rev = 11
        d = 11 - (tl % 11)

        if d > 9:
            d = 0
        tl = 0
        n_cpf += str(d)

print(cpf)
