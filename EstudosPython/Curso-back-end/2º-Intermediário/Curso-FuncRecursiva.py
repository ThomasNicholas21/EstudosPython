# evitando stackoverflow


def recursiva(inicio=0, fim=10):
    #evitando stackoverflow
    if inicio >= fim:
        return fim
    
    inicio += 1
    return recursiva(inicio, fim)

