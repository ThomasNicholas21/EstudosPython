# Faça um programa que leia um nome
# de usuário e a sua senha e não aceite a
# senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.

while True:
    print('Cadastro do usuario!')
    a = input('Insira o nome do seu usuario: ')
    b = input('Insira sua senha: ')

    if a == b:
        print('Seu nome de usuario e senha devem ser diferentes!')
        continue
    else:
        print('Seu cadastro foi concluido!')
        break
