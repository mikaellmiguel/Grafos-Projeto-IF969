class Grafo:

    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.grafo = [[0] * num_vertices for i in range(num_vertices)]

    def add_aresta(self, v_inicial, v_final, peso):
        self.grafo[v_inicial][v_final] = peso
        self.grafo[v_final][v_inicial] = peso

    def get_matriz(self):
        return self.grafo

    def get_tamanho(self):
        return self.num_vertices