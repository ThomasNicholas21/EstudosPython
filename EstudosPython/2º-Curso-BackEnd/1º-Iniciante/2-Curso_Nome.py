nome = input('Digite o seu nome: ')
qnt_nome = len(nome)

if qnt_nome <= 4:
    print('Seu nome é curto!')
elif qnt_nome >= 5 and qnt_nome <= 6:
    print('Seu nome é normal! ')
else:
    print('Seu nome é muito grande! ')
