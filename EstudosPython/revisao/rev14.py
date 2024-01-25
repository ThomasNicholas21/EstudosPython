#revisando empacotamento e desempacotamento 

lista = [1, 2, 3, 4, 5, 6]
print(*lista)   # O "*" serve para o desempacotamento dessa lista, extraindo os dados que estão nelas

dic = {
    'Nome' : 'Thomas',
    'Idade' : 'Nicholas',
}

def mostra_dic(**kwargs):    # serve desempacota palavra-chave, utilizado para um função
    for chave, valor in kwargs.items():
        print(chave, valor)

mostra_dic(**dic)
