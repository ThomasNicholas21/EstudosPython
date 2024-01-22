#Revisando dicionário
# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
import copy

dados = { 
    'Nome' : 'Thomas Nicholas',
    'sobrenome' : 'Pedrosa Matias', 
    'Idade' : 24,
    'Profissão' : 'Analista',
    'Endereço' : [
        {
            'Rua1' : 'Algermiro', 'Numero1': 28,
            'Rua2' :           5, 'Numero2' : 2,
        }
    ],
}


print()
print('Processando quantidade de dados...')
print(len(dados)) #Quantidade de chaves


print()
print('Iterando sobre o dicinário (chaves)...')
print(list(dados.keys())) # itera sobre o dicinário, voltando apenas para chaves, igual utilizar "For"
for chave in dados.keys(): # podendo ser - for chave in dados:
    print(chave)

print()
print('Iterando sobre o dicinário (valores)...')
print(list(dados.values()))
for valores in dados: # ou  for valores in dados.values(): print(valores)
    print(dados[valores])

print()
print('Iterando sobre o dicinário (valores e chaves)...')
print(list(dados.items()))
for chave, valor in dados.items():
    print(chave, valor)

print()
print('Atribuindo valor que não existe dentro do dicinário...')
dados.setdefault('Altura', 1.76) # adiciona valor caso a chave não exista, inserindo no dicinário
print(dados['Altura']) 
for chave, valor in dados.items():
    print(chave, valor)

print()
print('Realizando shallow copy...')
dados2 = copy.copy(dados) # utilizando modulo copy, porém utilizar dados2 = dados.copy, irá fazer uma copia raza tambem (copia dados imutaveis)
dados2['Nome'] = 'Manoel Gomes'
dados2['sobrenome'] = 'Gomes Gomes'
print(dados2)

dados2 = copy.deepcopy(dados) # copia dados mutaveis e imutaveis (processamento lento)

print()
print('Selecionando um valor do dicinário...')
print(dados.get('Idade'))
print(dados.get('Salario', 'Não tem salário')) # Caso a chave, retorna o segundo parametro(por padrão seria None)

print()
print('Selencionando um item para remover do dicinário...')
for chave, valor in dados.items():
    print(chave, valor)
deletando = dados.pop('sobrenome') # Retira a chave desejada
print()
for chave, valor in dados.items():
    print(chave, valor)

print()
print('Deletando o ultimo chave...')
eliminando_ultima_chave = dados.popitem()
print(list(dados.values()))

print()
print('Atualizando o dicinário com chaves eliminadas...')
dados.update({                           # atualiza seu dicinário
    'sobrenome': 'matias pedrosa',
    'idade' : 24,
})
print(list(dados.values()))