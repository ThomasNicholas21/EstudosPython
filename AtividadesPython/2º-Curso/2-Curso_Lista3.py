"""
desempacotamento de listas
"""

while True:
    dados_armazenados = []
    dado1 = input('Digite seu nome: ')
    dados_armazenados.append(dado1)
    dado2 = input('Digite sua cidade natal: ')
    dados_armazenados.append(dado2)
    dado3 = input('Digite seu desenho favorito: ')
    dados_armazenados.append(dado3)
       
    print(dados_armazenados)

    dado1, dado2, dado3 = dados_armazenados


    sair = input('Sair? [S]im ou [N]ão: ').lower().startswith('s')
    if sair is True:
        break

   

    
  
       