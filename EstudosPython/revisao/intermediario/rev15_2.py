#Gere uma lista dos primeiros 10 números pares.

lista = [
    numero
    for numero in range(1,11)
    if numero % 2 == 0
]

print(*lista)



# Jeito mais simples 
nova_lista = [
    numero for numero in range(0,10,2)
]

print(*nova_lista)