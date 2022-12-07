# Variaveis livres e nonlocal

def fora(x):
    a = x

    def dentro():
        print(dentro.__code__.co_freevars)
        return a
    return dentro


dentro1 = fora(10)
dentro2 = fora(20)

print(dentro1())
print(dentro2())