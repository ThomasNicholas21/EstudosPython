"""
Usando Truthy e Falsy
"""
# Tipos mutáveis
lista = [1]
dicionario = {2}
conjunto = set()
# Tipos Imutáveis
tupla = ()
string = ''
inteiro = 0
flutuante = 0.0
vazio = None
falso = False
intervalo = range(0)


def falsy(valor):
    return 'falsy' if not valor else 'truthy'


print('TESTE', falsy('TESTE'))
print(f'{lista=}', falsy(lista))
print(f'{dicionario=}', falsy(dicionario))
print(f'{conjunto=}', falsy(conjunto))
print(f'{tupla=}', falsy(tupla))
print(f'{string=}', falsy(string))
print(f'{inteiro=}', falsy(inteiro))
print(f'{flutuante=}', falsy(flutuante))
print(f'{vazio=}', falsy(vazio))
print(f'{falso=}', falsy(falso))
print(f'{intervalo=}', falsy(intervalo))
