class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumentar(self):
        self.canal += 1

    def diminuir(self):
        self.canal -= 1


televisao = Televisao()
televisao.power()  # comando de inicialização
print(televisao.ligada)
televisao.power()
print(televisao.ligada)
televisao.aumentar()
print(televisao.canal)
televisao.diminuir()
print(televisao.canal)
