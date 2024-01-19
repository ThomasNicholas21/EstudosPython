#Criar função que duplica, triplica e quadriplica o número recebido como parâmetro

def cria(multiplicador):
    def multiplica(numero):
        return numero*multiplicador
    return multiplica

numero = int(input("Digite um número: "))

duplica = cria(2)
triplica = cria(3)
quadruplica = cria(4)

print(duplica(numero))
print(triplica(numero))
print(quadruplica(numero))
