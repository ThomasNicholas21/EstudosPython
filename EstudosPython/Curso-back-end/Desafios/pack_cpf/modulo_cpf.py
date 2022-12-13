def validador_cpf(cpf):
    novo_cpf1 = cpf[:9]
    novo_cpf2 = novo_cpf1 + str(avaliador1(novo_cpf1))
    novo_cpf3 = novo_cpf2 + str(avaliador2(novo_cpf2))
    if novo_cpf3 == cpf:
        return True
    return False

def avaliador1(args):
    soma = 0
    reverse = 10
    for i in  args:
        soma += int(i) * reverse
        reverse -= 1
    
    digito = (soma * 10) % 11
    digito = digito if digito <= 9 else 0
    return digito

def avaliador2(args):
    soma = 0
    reverse = 11
    for i in  args:
        soma += int(i) * reverse
        reverse -= 1
    
    digito = (soma * 10) % 11
    digito = digito if digito <= 9 else 0
    return digito
