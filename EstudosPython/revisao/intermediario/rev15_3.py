# Dada uma lista de temperaturas em Celsius, converta-as para Fahrenheit usando a fórmula (C * 9/5) + 32.

lista_celsius = [20, 24, 26, 30, 34, 38]

lista_fahrenheit = [
    (numero * 9/5) + 32
    for numero in lista_celsius
]

print(*lista_celsius, sep='-')
print(*lista_fahrenheit, sep='-')