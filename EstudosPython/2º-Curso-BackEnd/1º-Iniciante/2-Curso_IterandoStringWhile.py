"""
iterando strings com while
"""

nome = input('Digite seu nome: ')
adição = input('Digite oque deseja adicionar: ')

novo_nome = ''
indice = 0
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'{adição}{letra}'
    indice += 1

novo_nome += adição
print(novo_nome)
