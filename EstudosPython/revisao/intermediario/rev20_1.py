# Exercício: Filtragem e Transformação de Palavras

lista1 = ['Generator', 'expression', 'python', 'Vida']
lista2 = []
lista3 = []

generator_lista1 = (
    palavra.upper()
    for palavra in lista1
    
)

for i in generator_lista1:
    if len(i) > 5:
        lista2.append(i)

generator_lista2 = (
    palavra.capitalize()
    for palavra in lista2
)

for j in generator_lista2:
    if len(j) <= 6:
        lista3.append(j)

print(*lista1, sep=' - ')
print(*lista2, sep=' - ')
print(*lista3, sep=' - ')
