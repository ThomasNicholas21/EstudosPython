cpf = input('Digite seu CPF: ')
novo_cpf = cpf[:-2]
total_soma = 0
reverso = 10

for i in range(10):
    total_soma += int(novo_cpf[i]) * reverso
    print(novo_cpf[i], reverso, int(novo_cpf[i]) * reverso, total_soma)
    reverso -= 1
