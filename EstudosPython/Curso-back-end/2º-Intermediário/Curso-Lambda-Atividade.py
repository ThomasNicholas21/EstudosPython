"""
Atribuindo lambda - atividade para fixação
OBS: Atividade 'simplificada'
"""


def executa(funcao, *args):
    return funcao(*args)


try:
    n1 = int(input('Primeiro número: '))
    n2 = int(input('Segundo número: '))

    som = executa(lambda n1, n2: n1 + n2, n1, n2)
    sub = executa(lambda n1, n2: n1 - n2, n1, n2)
    div = executa(lambda n1, n2: n1 / n2, n1, n2)
    mult = executa(lambda n1, n2: n1 * n2, n1, n2)

    print(
        f'Soma = {som}, Subtração = {sub}, '
        f'Divisão = {div:.2f}, Multiplicação = {mult}.'
    )

except ValueError:
    print('Digite números!')
