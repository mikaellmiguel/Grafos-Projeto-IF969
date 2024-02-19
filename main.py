from classes import *
from gui import *
import pandas as pd
from geopy.distance import geodesic

# Tratamento da Base de Dados
df = pd.read_csv("./ConectaWifi.csv")  # Lendo a base de Dados
df = df.drop("_id", axis=1)  # Dropando a coluna de ID que veio na tabela para não duplicar com a do pandas

grafo = Grafo(len(df))  # Criação do objeto que vai armazenar o grafo

# Essa Matriz é para auxiliar na criação de arestas, onde os vertices se conectam apenas com os da mesma rpa ou vizinhas
matriz_vizinhança = [
    [1, 2, 3, 4, 5, 6],  # Centro (RPA1)
    [1, 2, 3],  # Norte (RPA2)
    [1, 2, 3, 4],  # Noroeste (RPA3)
    [1, 3, 4, 5],  # Oeste (RPA4)
    [1, 4, 5, 6],  # Sudeste (RPA5)
    [1, 5, 6]]  # Sul (RPA6)

# Dados obtidos de: https://www2.recife.pe.gov.br/servico/sobre-rpa-1

# Inserção de arestas e calculo de peso (Distância)
for i in range(len(df)):
    for j in range(i + 1, len(df)):
        if df["rpa"].iloc[j] in matriz_vizinhança[(df["rpa"].iloc[i]) - 1]:
            coordenadas1 = (df["latitude"].iloc[i], df["longitude"].iloc[i])
            coordenadas2 = (df["latitude"].iloc[j], df["longitude"].iloc[j])

            # Inserido a distancia como peso da aresta.
            grafo.add_aresta(i, j, geodesic(coordenadas1, coordenadas2).kilometers)

app = Interface(grafo, df)