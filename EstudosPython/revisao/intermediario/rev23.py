#Exercício de revisão:
#Criar gerenciamento de estoque
#Criar funcao de adicionar, remover e consultar produto
#Criar um dicionario 


# Criando funcoes 
def add_product(estoque, name, amount, price):
    if amount < 0 or price < 0:
        raise ValueError("A quantidade e o preco deve ser maior que zero!!")
    if name in estoque:
        estoque[name]["Quantidade"] += amount
        estoque[name]["Preco"] = price
    else:
        estoque[name] = {"Quantidade": amount, "Preco": price}


def remove_product():
    ...

def find_product():
    ...

estoque = {}
add_product(estoque, "maçã", 10, 1.5)
add_product(estoque, "banana", 25, 3)
add_product(estoque, "maçã", 15, 1.5)
print(list(estoque.items()))