'''
Faça um programa que leia um nome de usuário e a sua senha e 
não aceite a senha igual ao nome do usuário, mostrando uma 
mensagem de erro e voltando a pedir as informações.
'''

login = input("Insira um login: ")
senha = input("Insira uma senha: ")
usuario1 = []

while login == senha:
    print("Atencao, o usuario e senha nao deve ser igual! Tente novamente!")
    login = input("Insira um login: ")
    senha = input("Insira uma senha: ")
else:
    usuario1 = [f'usuario: {login}', f'senha: {senha}']

print(usuario1)