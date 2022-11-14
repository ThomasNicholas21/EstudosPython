"""
Exercicio Lista
"""
dado1 = input('Digite seu nome: ')
dado2 = input('Digite seu sobrenome: ')
dado3 = input('Digite seu email: ')
dado4 = input('Digite sua senha: ')

usuário = [dado1, dado2, dado3, dado4]

for dados in enumerate(usuário):
    print(f'{dados}')
