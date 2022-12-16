def cifra_de_cesar(texto, chave):
    texto_cifrado = ""

    # Percorre cada letra do texto
    for letra in texto:
        # Verifica se a letra é uma letra do alfabeto
        if letra.isalpha():
            # Obtém o código ASCII da letra
            codigo = ord(letra)

            # Verifica se a letra é maiúscula
            if letra.isupper():
                # Aplica a cifra de César na letra maiúscula
                codigo += chave
                if codigo > ord('Z'):
                    codigo -= 26
                elif codigo < ord('A'):
                    codigo += 26
            else:
                # Aplica a cifra de César na letra minúscula
                codigo += chave
                if codigo > ord('z'):
                    codigo -= 26
                elif codigo < ord('a'):
                    codigo += 26

            # Adiciona a letra cifrada ao texto cifrado
            texto_cifrado += chr(codigo)
        else:
            # Adiciona o caractere sem cifrar ao texto cifrado
            texto_cifrado += letra

    return texto_cifrado

# Testa a função
texto = "Estamos chegando na 3VA. Vamos estudar para não reprovar"
chave = 5
texto_cifrado = cifra_de_cesar(texto, chave)
print(texto_cifrado)