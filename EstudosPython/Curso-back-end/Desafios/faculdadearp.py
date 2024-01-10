import sys

class UnidadeSaude:
    def __init__(self, nome):
        self.nome = nome
        self.vizinhos = {}

    def adicionar_vizinho(self, unidade, distancia):
        self.vizinhos[unidade] = distancia

class Grafo:
    def __init__(self):
        self.unidades = {}

    def adicionar_unidade(self, unidade):
        self.unidades[unidade.nome] = unidade

    def adicionar_conexao(self, unidade_origem, unidade_destino, distancia):
        if unidade_origem.nome in self.unidades and unidade_destino.nome in self.unidades:
            self.unidades[unidade_origem.nome].adicionar_vizinho(unidade_destino, distancia)
            self.unidades[unidade_destino.nome].adicionar_vizinho(unidade_origem, distancia)

    def obter_distancia(self, unidade_origem, unidade_destino):
        if unidade_origem.nome in self.unidades and unidade_destino.nome in self.unidades:
            visitados = set()
            distancia = {unidade: sys.maxsize for unidade in self.unidades.values()}
            distancia[unidade_origem] = 0
            atual = unidade_origem

            while atual:
                visitados.add(atual)

                for vizinho, distancia_vizinho in atual.vizinhos.items():
                    nova_distancia = distancia[atual] + distancia_vizinho
                    if nova_distancia < distancia[vizinho]:
                        distancia[vizinho] = nova_distancia

                proximo = None
                min_distancia = sys.maxsize
                for unidade in self.unidades.values():
                    if unidade not in visitados and distancia[unidade] < min_distancia:
                        proximo = unidade
                        min_distancia = distancia[unidade]

                atual = proximo

            return distancia[unidade_destino]

        return None



us1 = UnidadeSaude("US1")
us2 = UnidadeSaude("US2")
us3 = UnidadeSaude("US3")
us4 = UnidadeSaude("US4")
us5 = UnidadeSaude("US5")

grafo = Grafo()

grafo.adicionar_unidade(us1)
grafo.adicionar_unidade(us2)
grafo.adicionar_unidade(us3)
grafo.adicionar_unidade(us4)
grafo.adicionar_unidade(us5)

grafo.adicionar_conexao(us1, us2, 10)
grafo.adicionar_conexao(us1, us3, 15)
grafo.adicionar_conexao(us2, us3, 5)
grafo.adicionar_conexao(us3, us4, 20)
grafo.adicionar_conexao(us4, us5, 8)


distancia = grafo.obter_distancia(us1, us5)
print(f"A distância entre US1 e US5 é: {distancia} km")
