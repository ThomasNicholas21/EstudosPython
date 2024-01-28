# Gere uma lista dos primeiros 10 números primos.

def validador_primo(n):
    cont = 0
    for i in range(2, n):
        if n % i == 0:
            cont += 1
    if cont == 0:
        return n
    return None


primeiro_primos = [
    numero for numero in range(100)
    if validador_primo(numero) 
]

print(*primeiro_primos)
