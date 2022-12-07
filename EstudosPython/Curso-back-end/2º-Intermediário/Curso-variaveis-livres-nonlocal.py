# Variaveis livres e nonlocal

def contatena(string_inicial):
    valor_final = string_inicial + ' '

    def interna(valor_a_concatenar):
        nonlocal valor_final
        valor_final += valor_a_concatenar + ' '
        return valor_final
    return interna

valor = contatena('Thomas')
print(valor('Nicholas'))
print(valor('Pedrosa'))
print(valor('Matias'))