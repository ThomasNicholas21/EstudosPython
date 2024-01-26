# Dada uma lista de palavras, crie uma nova lista contendo apenas as palavras com mais de 5 letras.

lista_nomes = ['Thomas', 'Samara', 'Ana', 'Python', 'Anel', 'Dedo', 'mão']

lista_nomes_grandes = [
    palavra
    for palavra in lista_nomes
    if len(palavra) > 5 
]

print(*lista_nomes_grandes, sep='\n')