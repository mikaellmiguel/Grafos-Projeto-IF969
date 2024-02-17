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
    
# Implementando Heap de Minimo que irá auxiliar no algoritmo de prim
class HeapMinimo:

    def __init__(self, heap: list):

        self.heap = heap
        self.tamanho = len(heap)

    # Auxilia na troca de dois elemetos do heap
    def trocar(self, i: int, j: int):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    
    # Constroi o Heap de minímo seguindo as propriedades corretas 
    def heapify(self):

        for i in range(int(self.tamanho/2), -1, -1):
            self.corrigir_descendo(i)

    # Retorna indece do pai
    def pai(self, indice: int):
        return int((indice - 1) / 2)

    # Corrige o heap quando é necessario subir um elemento para a posição correta
    def corrigir_subindo(self, indice: int):
        pai = self.pai(indice)
        if self.heap[indice][1] < self.heap[pai][1]:
            self.trocar(indice, pai)
            self.corrigir_subindo(pai)

    # Corrige o heap quando é necessario descer um elemento para a posição correta
    def corrigir_descendo(self, indice: int):

        menor = indice

        if self.tamanho > (2*indice)+1 and self.heap[menor][1] > self.heap[(2 * indice) + 1][1]:
            menor = (2 * indice) + 1

        if self.tamanho > (2*indice)+2 and self.heap[menor][1] > self.heap[(2 * indice) + 2][1]:
            menor = (2 * indice) + 2

        if menor != indice:
            self.trocar(menor, indice)
            self.corrigir_descendo(menor)

    # Remove o primeiro elemento da lista (O mínimo) e restaura o Heap
    def remocao(self):
        if self.tamanho > 0:
            self.trocar(0, self.tamanho-1)
            elemento_removido = self.heap.pop()
            self.tamanho -= 1
            self.corrigir_descendo(0)

            return elemento_removido

    # Altera o valor de um elemento no heap
    def alterar_chave(self, vertice:int, chave:int):

        for indice, j in enumerate(self.heap):
            if j[0] == vertice:
                self.heap[indice][1] = chave
                indice = indice
                break

        # Realizando a correção para manter as propriedades
        if self.heap[self.pai(indice)][1] > chave:
            self.corrigir_subindo(indice)
        else:
            self.corrigir_descendo(indice)

    def __str__(self):
        return str(self.heap)

    def __len__(self):
        return self.tamanho