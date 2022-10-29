"""
CPF = 168.995.350-09
------------------------------------------------
1 * 10 = 10           #    1 * 11 = 11 <-
6 * 9  = 54           #    6 * 10 = 60
8 * 8  = 64           #    8 *  9 = 72
9 * 7  = 63           #    9 *  8 = 72
9 * 6  = 54           #    9 *  7 = 63
5 * 5  = 25           #    5 *  6 = 30
3 * 4  = 12           #    3 *  5 = 15
5 * 3  = 15           #    5 *  4 = 20
0 * 2  = 0            #    0 *  3 = 0
                      # -> 0 *  2 = 0
         297          #             343
11 - (297 % 11) = x  #     11 - (343 % 11) = 9
x > 9 = 0            #
Digito 1 = 0          #   Digito 2 = 9
"""
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
