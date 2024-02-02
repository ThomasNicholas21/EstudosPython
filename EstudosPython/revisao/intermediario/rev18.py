# utilizando isinstance e aprendendo

def validador_inteiro(*numeros):
    for numero in numeros:
        if isinstance(numero, (int, float, set, dict, tuple)):
            return numeros
        return f'O valor digitado "{numero}" não é número!!'
    

validar1 = validador_inteiro(1, 2, 3, 4, 5)
validar2 = validador_inteiro('Thomas', 2, 5)
validar3 = validador_inteiro(2, (2, 3, 4), {'chave': 123}, {1, 2, 3, 4, 5, 6})

print(validar1)
print(validar2)
print(validar3)