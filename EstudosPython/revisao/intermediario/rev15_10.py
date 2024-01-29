# Dada uma lista de palavras, crie uma nova lista contendo apenas as palavras que contêm vogais.

lista = ['Dd', 'M', 'Sabão', 'Morte', 'Dnç', 'Sanduiche']

lista_com_vogal = [
    palavra for palavra in lista if any(letra in 'aeiouAEIOUã' for letra in palavra)
]

print(lista_com_vogal)