from functions import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


class Interface:
    def __init__(self, grafo:Grafo, database):
        # Integrando dados a Interface
        self.database = database
        self.grafo = grafo

        # Iniciando a Interface Gráfica
        self.root = Tk()
        self.configurar_root()
        #self.tela_incial()
        #self.sytles()
        self.root.protocol("WM_DELETE_WINDOW", self.fechar_janela)
        self.root.mainloop()

    # Função para fechar janela quando apertar no x do windows
    def fechar_janela(self):
        plt.close()  #Fechando todas as figuras
        self.root.quit() # Chamando o fechamento do programa

    def configurar_root(self):
        self.root.geometry("1024x720")              # Resolução de Inicialização
        self.root.configure(bg="#cf1934")           # Cor do Background
        self.root.maxsize(1920, 1080)               # Resolução Máxima
        self.root.minsize(1280, 600)                # Resolução Mímima
        self.root.title("Visualizador de MST's")    # Titulo da Janela
