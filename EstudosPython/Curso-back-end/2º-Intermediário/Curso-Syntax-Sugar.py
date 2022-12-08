# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.

def criar_funcao(func):
    def interna(*args, **kwargs):
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        return resultado
    return interna
            
@criar_funcao                   
def inverte_string(string):   # Serve para simplificar e utilizar a                          
    return string[::-1]       # função de tratamento de erro
                              # sem precisar declara-la
def e_string(param):
    if not isinstance(param, str):
        raise TypeError('Parametro recebe apenas string')


string = input('Digite a palavra para ser invertida: ')
#string = int(input('Digite a palavra para ser invertida: '))
print(inverte_string(string))