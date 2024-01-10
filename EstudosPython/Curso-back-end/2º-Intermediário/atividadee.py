class Dado:
    def __init__(self, local_atual, local_destino, distancia):
        self.local_atual = local_atual
        self.local_destino = local_destino
        self.distancia = distancia

def inserir_dados(local_atual, local_destino, distancia, vetor):
    dado = Dado(local_atual, local_destino, distancia)
    vetor.append(dado)

def comparar_por_distancia(dado1, dado2):
    if dado1.distancia < dado2.distancia:
        return -1
    elif dado1.distancia > dado2.distancia:
        return 1
    else:
        return 0

def comparar_por_local_atual(dado1, dado2):
    return dado1.local_atual.lower().compare(dado2.local_atual.lower())

def comparar_por_local_destino(dado1, dado2):
    return dado1.local_destino.lower().compare(dado2.local_destino.lower())

def busca_sequencial(vetor, chave, comparar):
    for i, dado in enumerate(vetor):
        if comparar(dado, chave) == 0:  
            return i
    return -1

def busca_binaria(vetor, chave, comparar):
    inicio = 0
    fim = len(vetor) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        resultado = comparar(vetor[meio], chave)

        if resultado == 0:
            return meio
        elif resultado < 0:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1

def consultar_dados(vetor, ordenacao):
    if ordenacao == "distancia":
        vetor.sort(key=lambda dado: dado.distancia)
    elif ordenacao == "local_atual":
        vetor.sort(key=lambda dado: dado.local_atual.lower())
    elif ordenacao == "local_destino":
        vetor.sort(key=lambda dado: dado.local_destino.lower())
    else:
        print("Ordenacao invalida.")
        return None

    for dado in vetor:
        print("\nLocal Atual: %s" % dado.local_atual)
        print("Local Destino: %s" % dado.local_destino)
        print("Distancia: %.2f" % dado.distancia)

    chave = input("\nDigite o local atual a ser pesquisado: ")

    print("\nBuscando pelo local atual %s..." % chave)
    posicao = busca_binaria(vetor, chave, comparar_por_local_atual)

    if posicao == -1:
        print("Local nao encontrado.")
    else:
        dado = vetor[posicao]
        print("\nLocal Atual: %s" % dado.local_atual)
        print("Local Destino: %s" % dado.local_destino)
        print("Distancia: %.2f" % dado.distancia)

    return vetor

vetor = []
inserir_dados("Sao Paulo", "Rio de Janeiro", 432.1, vetor)
inserir_dados("Rio de Janeiro", "Salvador", 1573.3, vetor)
inserir_dados("Belo Horizonte", "Porto Alegre", 1467.5, vetor)
inserir_dados("Curitiba", "Recife", 3185.9, vetor)
inserir_dados("Recife", "Sao Paulo", 2775.8, vetor)

print("\n--- Dados ordenados por distancia ---")
consultar_dados(vetor, "distancia")

print("\n--- Dados ordenados por local atual ---")
consultar_dados(vetor, "local_atual")

print("\n--- Dados ordenados por local destino ---")
consultar_dados(vetor, "local_destino")
