vet = [

     1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 17, 22, 
     35, 39, 41, 44, 47, 48, 49, 51, 55, 64, 67, 87, 
     89, 99, 100

    ]


def busca_binaria(vet, elemento):
    cont = 0
    inicio = 0
    fim = len(vet) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        cont += 1
        if vet[meio] == elemento:
            return meio, cont
        elif vet[meio] < elemento:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1, cont

elem = int(input('Digite o elemento: '))
indice, comp = busca_binaria(vet, elem)

if indice == -1:
    print(f"Erro: Elemento: {elem} não foi encontrado. ")
else:
    print(
        f"Busca binaria: Elemento: {elem} foi "
        f"encontrado no indice: {indice} com {comp} comparações.")
