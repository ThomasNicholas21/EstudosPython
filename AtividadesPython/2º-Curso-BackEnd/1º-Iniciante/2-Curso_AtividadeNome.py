"""
nome usuário
idade usuário
confimação de nome e idade digitados

nome
nome invertido
nome contem espaços
quantidade de letras
primera letra do nome
ultima letra do nome
"""
while True:
    nome = input('Digite seu nome: ')
    idade = input('Digite sua idade: ')

    if len(nome) == 0:
        print('Desculpe, preencha os campos para prosseguir')
        continue
    elif len(idade) == 0:
        print('Desculpe, preencha os campos para prosseguir')
        continue

    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
        print('Contém espaço!')
    else:
        print('Não contém espaço!')

    print(f'Seu nome contém {len(nome)} letras')
    print(f'A primera letra do seu nome é {nome[0].upper()}')
    print(f'A ultima letra do seu nome é {nome[-1].lower()}')

    sair = input('Deseja sair? [s]im ou [n]ão: ').lower().startswith('s')
    if sair == True:
        break
