# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

while True:
    nome = input('Insira seu nome:')
    qtd_nome = len(nome)
    if qtd_nome <= 3:
        print('Nome deve possuir mais que 3 caracteres!')
        continue

    idade = int(input('Insira sua idade: '))
    if idade < 0 and idade > 150:
        print('Idade incompativel!')
        continue

    salario = float(input('Insira seu salario: '))
    if salario == 0:
        print('Deve possuir salario!')
        continue

    sexo = input('Insira seu sexo, feminino ou masculino: ')
    f = 'feminino'
    m = 'masculino'
    if sexo != f and sexo != m:
        print('Insira seu sexo!')
        continue

    estado_civil = input('Insira seu estado civil '
                         '-solteiro(a) '
                         '-casado(a) '
                         '-viuvo(a) '
                         '-divorciado(a): ')
    s = 'solteiro'
    c = 'casado'
    v = 'viuvo'
    d = 'divorciado'
    if estado_civil != s and estado_civil != c and estado_civil != v and estado_civil != d:
        print('Insira seu estado civil!')
        continue

    break

print(f'Usuario se chama {nome}, possui {idade} anos, recebe {salario}, '
      f'seu sexo é {sexo}, e seu estado civil é {estado_civil}')
