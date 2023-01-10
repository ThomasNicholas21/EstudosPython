import getpass

def menu():
    print(
        'Opções:\n'
        '1 - Cadastro\n'
        '2 - Listagem de cadastro\n'
        '3 - Busca de cadastro\n'
        '4 - Remoção de cadastro\n'
        '5 - Sair'
        )

def cadastro(pessoas):
    id_usuario = input('Digite seu ID: ')
    nome_completo_usuario = input('Insira seu nome completo: ')
    data_nascimento_usuario = input('Insira sua data de nascimento: ')
    senha_usario = getpass.getpass('Insira a senha: ')
    senha_confirmada = getpass.getpass('Confirme a senha: ')
    while senha_usario != senha_confirmada:
        print('Senhas diferentes, tente novamente!')
        senha_usario = getpass.getpass('Insira a senha: ')
        senha_confirmada = getpass.getpass('Confirme a senha: ')
    pessoas.append((id_usuario, nome_completo_usuario, data_nascimento_usuario, senha_confirmada))

def listagem_cadastro(pessoas):
    for pessoa in pessoas:
        id_usuario, nome_completo_usuario, data_nascimento_usuario, senha_confirmada = pessoa
        print(f'Nome: {nome_completo_usuario}, Data: {data_nascimento_usuario}, Senha: {senha_confirmada}, ID: {id_usuario}')

def busca_cadastro(pessoas):
    identificador = input('Digite o ID: ')
    for pessoa in pessoas:
        id_usuario, nome_completo_usuario, data_nascimento_usuario, senha_confirmada = pessoa
        if identificador == id_usuario:
            print(f'Nome: {nome_completo_usuario}, Data: {data_nascimento_usuario}, Senha: {senha_confirmada}, ID: {id_usuario}')
            break
    else:
        print(f'O ID {identificador}, é invalido.')

def remocao_cadastro(pessoas):
    identificador = input('Digite o ID para ser removido: ')
    for pessoa in pessoas:
        id_usuario, nome_completo_usuario, data_nascimento_usuario, senha_confirmada = pessoa
        if identificador == id_usuario:
            print(f'O ID {id_usuario} será removido.')
            pessoas.remove((id_usuario, nome_completo_usuario, data_nascimento_usuario, senha_confirmada))
        else:
            print(f'O ID {identificador} não foi encontrado.')


