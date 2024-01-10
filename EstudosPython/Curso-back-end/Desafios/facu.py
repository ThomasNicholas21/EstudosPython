def ler_dados():
    vetor = []
    print("Digite os elementos do vetor (20 elementos):")
    for _ in range(20):
        elemento = int(input())
        vetor.append(elemento)
    chave = int(input("Digite a chave de busca: "))
    return vetor, chave

def busca_sequencial(vetor, chave):
    comparacoes = 0
    for i, elemento in enumerate(vetor):
        comparacoes += 1
        if elemento == chave:
            return comparacoes
    return comparacoes

def busca_binaria(vetor, chave):
    comparacoes = 0
    esquerda = 0
    direita = len(vetor) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        comparacoes += 1
        if vetor[meio] == chave:
            return comparacoes
        elif vetor[meio] < chave:
            esquerda = meio + 1
        else:
            direita = meio - 1
    
    return comparacoes

def ordenar_vetor(vetor):
    vetor.sort()

def menu():
    vetor, chave = ler_dados()
    opcao = int(input("Escolha o tipo de busca:\n1. Busca Sequencial\n2. Busca Binária\n"))

    if opcao == 1:
        comparacoes = busca_sequencial(vetor, chave)
        print("Comparacoes realizadas:", comparacoes)
    elif opcao == 2:
        ordenar_vetor(vetor)
        comparacoes = busca_binaria(vetor, chave)
        print("Comparacoes realizadas:", comparacoes)
    else:
        print("Opção inválida.")

menu()
