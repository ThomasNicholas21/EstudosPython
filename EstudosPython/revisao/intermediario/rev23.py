#Exercício de revisão:
#Criar gerenciamento de estoque
#Criar funcao de adicionar, remover e consultar produto
#Criar um dicionario 


# Criando funcoes 
def add_product(stock, name, amount, price):
    if amount < 0 or price < 0:
        raise ValueError("The amount or price has to be more tn zero!")
    if name in stock:
        stock[name]["Amount"] += amount
        stock[name]["Price"] = price
    else:
        stock[name] = {"Amount": amount, "Price": price}


def remove_product(stock, name, amount):
    if name not in stock:
        raise KeyError("This product is not in stock!")
    if amount > stock[name]["Amount"]:
        raise ValueError("This is more than we have in stock!")
    
    stock[name]["Amount"] -= amount

    if stock[name]["Amount"] == 0:
        del stock[name]


def find_product(stock, name):
    if name not in stock:
        raise KeyError("We don't have this product!")
    else:
        print(list(*stock.items()))
    

stock = {}
add_product(stock, "apple", 10, 1.5)
add_product(stock, "banana", 25, 3)
add_product(stock, "apple", 15, 1.5)
for key, item in stock.items():
    print(key, item)

remove_product(stock, "apple", 5)
remove_product(stock, "banana", 25)
#remove_product(stock, "pineapple", 1)
#remove_product(stock, "apple", 25)

for key, item in stock.items():
    print(key, item)

find_product(stock, "apple")
find_product(stock, "pineapple")