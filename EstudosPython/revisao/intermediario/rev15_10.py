# Dada uma lista de palavras, crie uma nova lista contendo apenas as palavras que contêm vogais.

lista = ['Dd', 'M', 'Sabão', 'Morte', 'Dnç', 'Sanduiche']

lista_com_vogal = [
    caratectere for palavra in lista for caratectere in palavra
    
]

print(lista_com_vogal)