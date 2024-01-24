#revisando lambda

#tranformando funções normais em funções lambdas
# def soma(x, y):
#     return x + y


# def cria_multiplicador(multiplicador):
#     def multiplica(numero):
#         return numero * multiplicador
#     return multiplica


# duplica = cria_multiplicador(2)    
def executa(funcao, *args):
    return funcao(*args)

try:
    numero1 = int(input('Primeiro numero: '))
    numero2 = int(input('Segundo numero: '))
    print('Processando dados...')

    print(executa(lambda x, y : x + y, numero1, numero2))

except:
    print('Digite apenas digitos!')