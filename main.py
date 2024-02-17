from classes import *
import pandas as pd
from geopy.distance import geodesic

# Tratamento da Base de Dados
df = pd.read_csv("ConectaWifi.csv")  # Lendo a base de Dados
df = df.drop("_id", axis=1)  # Dropando a coluna de ID que veio na tabela para não duplicar com a do pandas

grafo = Grafo(len(df))  # Criação do objeto que vai armazenar o grafo

