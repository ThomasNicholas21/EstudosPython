"""
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
"""

while True:
    nome = input("Qual seu nome: ")
    if len(nome) < 3:
        print("Insira um nome com mais de 3 caracteres!")
        continue

    idade = int(input("Qual sua idade: "))
    if idade <= 0 or idade >= 150:
        print("Insira uma idade válida!")
        continue

    salario = int(input("Quanto recebe: "))
    if salario == 0:
        print("Salário deve ser maior que zero!")
        continue

    sexo = input("Qual seu sexo: ")
    if not sexo.startswith("f") and not sexo.startswith("m"):
        print("Insira um sexo válido.")
        continue

    estado_civil = input("Qual seu estado civil: ")
    if  not estado_civil.startswith("s") or not estado_civil.startswith("v") or not estado_civil.startswith("d") or  estado_civil.startswith("c"):
        print("Insira um estado civil válido")
        continue
    
    lista_de_dados = [nome, idade, salario, sexo, estado_civil]
    print(lista_de_dados)

    sair = input("deseja sair: ").lower().startswith("s")
    if sair is True:
        break
    else:
        continue

    