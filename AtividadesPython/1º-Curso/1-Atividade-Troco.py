""" 
Fazer um programa para calcular o troco no processo  
de pagamento de um produto de uma mercearia.
O programa deve ler o preço unitário do produto, 
a quantidade de unidades compradas deste produto,
e o valor em dinheiro dado pelo cliente. Seu programa deve
mostrar o valor do troco a ser devolvido ao cliente.

"""
valor_produto = float(input("Preço do produto: "))
qnt_comprada = int(input("Quantidade comprada: "))
valor_recebido = float(input("Qual valor recebido: "))

valor_total = valor_produto*qnt_comprada
troco = valor_recebido - valor_total

if valor_recebido < valor_total:
    print("Saldo insuficiente!")
elif valor_recebido == valor_total:
    print("Nao é necessário troco, valor recebido exato!")
else:
    print(f"O valor do troco: {troco:.2f}.")
