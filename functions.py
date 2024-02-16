from classes import *

# Implementação do algoritmo de prim
def prim(grafo: Grafo, vertice_inicial:int):

    matriz = grafo.get_matriz() # Obtendo a matriz de adjacência do referente grafo

    parent = [None]*grafo.get_tamanho() # Armazena os antecersores de cada vertice
    custo = [float("inf")]*grafo.get_tamanho() # Armazena o custo para acessar cada vertice
    vertices_fila = [True] * grafo.get_tamanho() # Utilizada para controlar quais estão na lista

    custo[vertice_inicial] = 0  # Como iremos iniciar do vertice inicial o custo dele é 0

    # Fila de prioridade utilizando um Heap de Minimo, Heap ordenado com base no custo
    fila = HeapMinimo([[i, float("inf")] for i in range(grafo.get_tamanho())])
    fila.heap[vertice_inicial] = [vertice_inicial, 0] # Inserido o vertice inicial com custo 0 na fila

    while fila:
        vertice, valor = fila.remocao() # Extraindo o mínimo através do Heap
        vertices_fila[vertice] = False # Marcando como False informando que ele não está mais na fila

        for i in range(grafo.get_tamanho()):
            if matriz[vertice][i] != 0:  # Se tiver aresta
                if vertices_fila[i] and matriz[vertice][i] < custo[i]: # Se estiver na fila e o peso menor
                    custo[i] = matriz[vertice][i] # Substituindo o custo anterior pelo peso atual
                    parent[i] = vertice  # Substituindo o predecessor do vertice
                    fila.alterar_chave(i, matriz[vertice][i])  # Alternado a chave na fila de prioridades

    print(sum(custo))


grafo = Grafo(5)

grafo.add_aresta(0, 1, 2)
grafo.add_aresta(0, 2, 1)
grafo.add_aresta(0, 3, 6)
grafo.add_aresta(0, 4, 3)
grafo.add_aresta(1, 2, 3)
grafo.add_aresta(1, 3, 4)
grafo.add_aresta(2, 3, 5)

prim(grafo, 0)