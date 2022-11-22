"""
Crie funções que duplicam, triplicam e quadruplicam
o número recebido como parâmetro.
"""


def multiplicador(multiplica):
    def numero(number):
        return number * multiplica
    return numero


duplica = multiplicador(2)
triplica = multiplicador(3)
quadruplica = multiplicador(4)

numero = input(
    'Digite um numero para ser duplicado, '
    'triplicado e quadruplicado: '
)
numero_int = int(numero)

print(f'Duplicado = {duplica(numero_int)}')
print(f'Triplicado = {triplica(numero_int)}')
print(f'Quadruplicado = {quadruplica(numero_int)}')
