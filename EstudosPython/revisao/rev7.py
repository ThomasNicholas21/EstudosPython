#funcao que multiplica argumentos nao nomeados

def multiplica(*args):
    receptor = 1
    for arg in args:
        receptor *= arg
    return receptor

print("Insira 5 numeros para serem multiplicados!")
contador = 1 
lista = []
while contador <= 5:
    numero = int(input("DIgite:"))
    lista.append(numero)
    contador += 1
    
multiplicador = multiplica(*lista)
print(multiplicador)