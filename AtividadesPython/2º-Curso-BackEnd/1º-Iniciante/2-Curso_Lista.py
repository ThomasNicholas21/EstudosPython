string = 'O Brasil ta em crise, o Brasil ta vai ganhar ta copa!'
lista_1 = string.split()
print(lista_1)
lista_2 = string.split(',')
print(lista_2)

palavra = ''
contagem = 0
for valor in lista_1:
    qnt_vezes = lista_1.count(valor)

    if qnt_vezes > contagem:
        contagem = qnt_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes é "{palavra}" ({contagem}x)')
