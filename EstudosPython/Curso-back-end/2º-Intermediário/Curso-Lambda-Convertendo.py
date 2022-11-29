"""
Convertendo funções em funções lambdas
"""


def executa(funcao, *args):
    return funcao(*args)


# def soma(x, y):
#   return x + y

# def cria_multiplicador(multiplicador):
#    def multiplica(numero):
#        return numero * multiplicador
#    return multiplica


duplica = executa(
    lambda multiplicador: lambda numero: numero * multiplicador, 2
)
print(duplica(5))

print(executa(
    lambda x, y: x + y, 2, 3
)
)
