"""
Atividade verificação de nome
"""
while True:
    nome = input('Digite seu nome aqui: ')

    nome_curto = len(nome) <= 4
    nome_normal = len(nome) >= 5 and len(nome) <= 6
    nome_nulo = len(nome) == 0

    if nome_nulo:
        print('Insira seu nome novamente.')
        continue
    elif nome.isdigit():
        print('Desculpe, você digitou um número, tente novamente.')
        continue
    elif nome_curto:
        print(f'Seu nome, {nome.capitalize()}, é curto.')
        break
    elif nome_normal:
        print(f'Seu nome, {nome.capitalize()}, é normal.')
        break
    else:
        print(f'Seu nome, {nome.capitalize()}, é muito grande.')
        break
