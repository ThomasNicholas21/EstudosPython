#aplicanto dictionary e set comprehension

dic = { 
    'Pessoa1' : 'Thomas', 
    'Idade' : 24, 
    'e-mail' : 'thomasnicholaas@gmail.com', 
    'numero' : '62 92445522', 
}

dic_novo = {
    chave:valor
    for chave, valor in dic.items()
}

print(dic_novo)

set = {i for i in range(20)}

print(set)