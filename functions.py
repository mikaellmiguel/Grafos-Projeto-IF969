from classes import *

# Implementação do algoritmo de prim
def prim(grafo: Grafo, vertice_inicial:int, tabela):

    matriz = grafo.get_matriz() # Obtendo a matriz de adjacência do referente grafo

    parent = [None]*grafo.get_tamanho() # Armazena os antecersores de cada vertice
    custo = [float("inf")]*grafo.get_tamanho() # Armazena o custo para acessar cada vertice
    vertices_fila = [True] * grafo.get_tamanho() # Utilizada para controlar quais estão na lista

    custo[vertice_inicial] = 0  # Como iremos iniciar do vertice inicial o custo dele é 0

    # Fila de prioridade utilizando um Heap de Minimo, Heap ordenado com base no custo
    fila = HeapMinimo([[i, float("inf")] for i in range(grafo.get_tamanho())])
    fila.heap[vertice_inicial] = [vertice_inicial, 0] # Inserido o vertice inicial com custo 0 na fila
    fila.heapify() # Ordenando a Fila

    mst = []  #Armazenar MST
    while fila:
        vertice, valor = fila.remocao() # Extraindo o mínimo através do Heap
        vertices_fila[vertice] = False # Marcando como False informando que ele não está mais na fila
        
        # Adicionando as arestas na mst, conforme cada vertice vai saindo da fila
        if parent[vertice] is not None:
            mst.append((tabela["local"][parent[vertice]], tabela["local"][vertice], round(valor * 1000, 2)))

        for i in range(grafo.get_tamanho()):
            if matriz[vertice][i] != 0:  # Se tiver aresta
                if vertices_fila[i] and matriz[vertice][i] < custo[i]: # Se estiver na fila e o peso menor
                    custo[i] = matriz[vertice][i] # Substituindo o custo anterior pelo peso atual
                    parent[i] = vertice  # Substituindo o predecessor do vertice
                    fila.alterar_chave(i, matriz[vertice][i])  # Alternado a chave na fila de prioridades

    # Retornando a MST e o custo total da MST
    return mst, sum(custo)