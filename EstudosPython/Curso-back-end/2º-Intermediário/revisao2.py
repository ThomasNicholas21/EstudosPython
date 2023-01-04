#revisando conteudo

frase = input('Digite qualquer frase: ')

i = 0
apareceu_mais_vezes = 0 #Contador
letra_que_apareceu_mais_vezes = ''

while i < len(frase):
    letra = frase[i]

    if letra == ' ':
        i += 1
        continue
    
    apareceu_mais_vezes_atual = frase.count(letra)

    if apareceu_mais_vezes < apareceu_mais_vezes_atual:
        apareceu_mais_vezes = apareceu_mais_vezes_atual
        letra_que_apareceu_mais_vezes = letra
    
    i += 1
   
print(
    f'A letra que aparece mais vezes "{letra_que_apareceu_mais_vezes}"'
    f'aparecendo {apareceu_mais_vezes} vezes'
)