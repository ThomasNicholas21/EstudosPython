

def escrever_arquivo(texto):
    arquivo = open('notas.txt', 'w')
    arquivo.write(texto)
    arquivo.close()


def atualizar_arquivo(texto):
    arquivo = open('notas.txt', 'a')
    arquivo.write(texto)
    arquivo.close()


def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)


if __name__ == '__main__':
    #escrever_arquivo('Primeira Linha!')
    aluno = 'Juaum,10,20,30,35'
    atualizar_arquivo('notas.txt', aluno)
    # ler_arquivo('teste.txt')
