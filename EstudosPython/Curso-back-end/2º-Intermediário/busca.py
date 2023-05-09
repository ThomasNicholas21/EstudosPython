vet = [

     1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 17, 22, 
     35, 39, 41, 44, 47, 48, 49, 51, 55, 64, 67, 87, 
     89, 99, 100

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
