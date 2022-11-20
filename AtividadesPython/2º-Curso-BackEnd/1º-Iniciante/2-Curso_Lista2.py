"""
Exercicio Lista
"""
usuário = []

dado1 = input('Digite seu nome: ')
usuário.append(dado1)
dado2 = input('Digite seu sobrenome: ')
usuário.append(dado2)
dado3 = input('Digite seu email: ')
usuário.append(dado3)
dado4 = input('Digite sua senha: ')
usuário.append(dado4)

cont = 0

indices = range(len(usuário))
# numerando de formas diferentes
for dados in enumerate(usuário):
    print(f'{dados}')

print()

for dados in usuário:
    cont = + 1
    print(f'{cont}-{dados}')

print()

for indice in indices:
    print(f'{indice} {usuário[indice]}')
