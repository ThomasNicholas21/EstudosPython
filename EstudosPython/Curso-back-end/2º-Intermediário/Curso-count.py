from itertools import count

passo = int(input('Digite como quer fazer a contagem: '))
inicio = int(input('Digite por onde quer começar: '))
final = int(input('Aonde terminar: '))

contador = count(inicio, passo)

for i in contador:
    if i >= final:
        break

    print(i)



