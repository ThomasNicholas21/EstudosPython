# Desafio validador de CPF

while True:
    cpf = input('Digite seu cpf: ')
    n_cpf = cpf[:-2]
    rev = 10
    tl = 0

    for x in range(19):
        if x > 8:
            x -= 9

        tl += int(n_cpf[x]) * rev

        print(n_cpf[x], x, rev)  # Demonstration of calculation

        rev -= 1
        if rev < 2:
            rev = 11
            d = 11 - (tl % 11)

            if d > 9:
                d = 0
            tl = 0
            n_cpf += str(d)

    if cpf == n_cpf:
        print('Cpf Valido!')

    else:
        print('Cpf Invalido!')
