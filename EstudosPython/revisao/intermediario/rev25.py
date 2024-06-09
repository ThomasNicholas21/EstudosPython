#Entendendo modulizacao
#O primeiro modulo executado é __main__
#Pode se importar outro modulo inteiro ou parte dele
#Reconhece aonde o arquivo __main__ esta, mas não módulos acima dele, ou seja, fora do arquivo.
#Reconhece todos os módulos presentes no caminhos de sys.path
import sys # boa prática deixar módulos no python e do usuário separado

from rev25_module import add_product, remove_product, find_product

#sys.path.append("D:\programação\EstudosPython\venv") # utiliza para adicionar caminhos de leitura
#print(*sys.path, sep='\n')

stock = {}
def mostra_dic(**kwargs):    
    for chave, valor in kwargs.items():
        print(chave, valor)

# funcoes de um modulo de adicionar produtos da revisao 25
add_product(stock, "apple", 12, 1)
print(list(*stock.items()))
remove_product(stock, "apple", 11)
add_product(stock, "apple", 0, 2)
print(list(*stock.items()))
