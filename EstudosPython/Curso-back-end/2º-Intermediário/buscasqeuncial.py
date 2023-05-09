vet = [
    1, 2, 5, 7, 10, 12, 13, 14, 16, 20
    ]

def busca_sequencial(vet, elemento):
    cont = 0
    for i in range(len(vet)):
        cont += 1
        if vet[i] == elemento:
            return i, cont
    return -1


elem = int(input('Digite o elemento: '))
indice, comp = busca_sequencial(vet, elem)

if indice == -1:
    print(f"Erro: Elemento: {elem} não foi encontrado. ")
else:
    print(
        f"Busca sequencial: Elemento: {elem} foi "
        f"encontrado no indice: {indice} com {comp} comparações.")
