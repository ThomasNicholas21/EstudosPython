"""
Validando CPF
"""

# Cálculo do Primeiro Digito

cpf = input('Digite seu CPF: ').replace('.', '') \
    .replace('-', '')
novo_cpf_1 = cpf[:9]
total_soma_1 = 0
reverso1 = 10

for i in novo_cpf_1:
    total_soma_1 += int(i) * reverso1
    reverso1 -= 1

digito_1 = (total_soma_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

# Cálculo do Segundo digito

novo_cpf_2 = novo_cpf_1 + str(digito_1)
reverso2 = 11
total_soma_2 = 0

for j in novo_cpf_2:
    total_soma_2 += int(j) * reverso2
    reverso2 -= 1

digito_2 = (total_soma_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

novo_cpf_3 = novo_cpf_2 + str(digito_2)

if novo_cpf_3 == cpf:
    print('Este CPF é válido!')
else:
    print('Este CPF não é valido!')
