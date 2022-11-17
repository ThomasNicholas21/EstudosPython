"""
Gerador 
"""
import random

cpf_9_digitos = ''
for x in range(9):
    cpf_9_digitos += str(random.randint(0, 9))

reverso = 10
soma_total = 0


for i in cpf_9_digitos:
    soma_total += int(i) * reverso
    reverso -= 1

digito_1 = (soma_total * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

cpf_10_digitos = cpf_9_digitos + str(digito_1)
reverso2 = 11
soma_total_2 = 0

for j in cpf_10_digitos:
    soma_total_2 += int(j) * reverso2
    reverso2 -= 1

digito_2 = (soma_total_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_cálculado = cpf_10_digitos + str(digito_2)

print(cpf_cálculado)
