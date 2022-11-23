"""
Desafio onde deve inverter as letras capitalizadas
e inverter a ordem da frase.
"""


def inverte_ordem_e_casos(frase):
    lista_palavra = frase.split()
    lista_reversa = lista_palavra[::-1]
    frase_reversa = ' '.join(lista_reversa)
    return frase_reversa.swapcase()


frase = input('Digite a frase: ')
ordem = inverte_ordem_e_casos(frase)
print(ordem)
