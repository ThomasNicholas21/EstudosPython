# Desempacotamento de lista

lista = ['IDCliente', 'Senha', 'EMAIL', 'DADOS_IRRELEVANTES', 1, 2, 3, 4]
I1, I2, I3, *_ = lista
L1, L2, L3, *__ = _
print(f'{I1} : {I2} : {I3} ')
print(f' {_}')
print(f'{L1} : {L2} : {L3}')
print(f'{__}')
