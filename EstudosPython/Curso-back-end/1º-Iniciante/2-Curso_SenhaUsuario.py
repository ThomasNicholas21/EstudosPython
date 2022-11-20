senha_do_usuario = '123456789'
contador = 0
senha_digitada = ''
nova_senha = ''

while senha_do_usuario != senha_digitada:
    senha_digitada = input('Digite sua senha: ')
    contador += 1

    if contador == 5:
        print('Esqueceu sua senha? Deseja recupera-la? ')

        recuperação = input('[S]im ou [N]ão : ').lower().startswith('s')

        if recuperação is True:
            nova_senha = input('Digite sua nova senha: ')
            senha_do_usuario = nova_senha

            print(f'Sua nova senha é {nova_senha}')
            continue


print(f'Sua senha foi escrita {contador} vezes.')
