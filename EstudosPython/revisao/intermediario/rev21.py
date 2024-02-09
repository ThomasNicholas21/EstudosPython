# Crie um programa em Python que solicite ao usuário o nome e a idade. O programa deve verificar se a idade fornecida é um número válido. 
# Se for válido, o programa deve imprimir uma mensagem no formato "Nome: [nome], Idade: [idade]". 
# Se a idade não for um número válido, o programa deve tratar o erro e imprimir uma mensagem apropriada.

try:
    idade = int(input('Digite sua idade: ')) # Código que pode gerar uma exceção
    print(idade)

except (IndentationError, ValueError) as error:
    print("Você colocou um número invalido:", error) # Código para lidar com Excecao

else:
    print('Parabéns:') # Código a ser executado se nenhum erro ocorrer no bloco try

finally:
    print(f'Idade {idade} é valido')   # Código a ser executado sempre, independentemente de ocorrerem exceções ou não