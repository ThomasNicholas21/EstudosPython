# Fazer um programa para ler o nome e idade de duas pessoas.
# Ao final mostrar uma mensagem com os
# nomes e a idade média entre essas pessoas, com
# uma casa decimal, conforme exemplo.

# primeira pessoa
print(':Primeira pessoa: ')
nome1 = str(input('Insira seu nome: '))
idade1 = int(input('Insira seu idade: '))
print(f'Nome e idade, respectivamente: {nome1} e {idade1} anos.')

# segunda pessoa
print(':Segunda pessoa: ')
nome2 = str(input('Insira seu nome: '))
idade2 = int(input('Insira seu idade: '))
print(f'Nome e idade, respectivamente: {nome2} e {idade2} anos.')

# idade media
idade_media = (idade1 + idade2)/2
print(f'Idade media entre as duas pessoas: {idade_media}')
