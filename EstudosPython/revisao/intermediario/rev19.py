# Revisando iterator

lista_de_objetos = ['Caneta', 'Tesoura', 'Lápis']
iterator = lista_de_objetos.__iter__() # Este método aceita apenas __next__ e só vê o proximo elemento a iterar
                                        #Podendo se usar iterator = iter(lista_de_objetos)

print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())


# print(next(iterator))
