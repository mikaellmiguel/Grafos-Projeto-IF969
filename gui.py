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
        self.tela_incial()
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

    def tela_incial(self):
        self.frame1 = Frame(self.root, bg="#cf1934")  # Criando o Frame da Tela Inicial
        self.titulo_inicial = Label(self.frame1, text="Árvore Geradora de Custo Mínimo com Prim",
                                    font=("Courier", 25, "bold"), bg="#cf1934", fg="white")

        self.descricao_inicial = Label(self.frame1, text="""Dados sobre a localização dos pontos do Connecta Wifi da Cidade de Recife, 
        um programa novador que está espalhando pontos de WIFI pela cidade, possibilitando o acesso de todos à internet""",
                  bg="#cf1934", fg="white", font=("Corier", 14), anchor="center")

        self.commando = Label(self.frame1, text="Escolha o Vertice Inicial",
                  bg="#cf1934", fg="white", font=("Corier", 14, "bold"), anchor="center")
        
        self.objetivo = Label(self.frame1, text="""Objetivo: Transformar os dados em um Grafo e gerar uma MST, obtendo assim a melhor forma
        de conectar todos esses pontos de Wifi, utilizando a menor metragem de cabos de rede possivel.""",
                 bg="#cf1934", fg="white", font=("Corier", 12, "bold"), anchor="center")


        # Criando a tabela de seleção de vertice inicial
        self.selecao = ttk.Treeview(height=3, columns=("col1", "col2"))
        self.scroolselecao = Scrollbar(self.frame1, orient="vertical", command=self.selecao.yview())
        self.selecao.configure(yscrollcommand=self.scroolselecao.set)


        self.selecao.heading("#0", text="")
        self.selecao.heading("#1", text="Local")
        self.selecao.heading("#2", text="Endereço")

        self.selecao.column("#0", width=0, minwidth=0, anchor="center")
        self.selecao.column("#1", width=250, anchor="center")
        self.selecao.column("#2", width=400, anchor="center")

        # Integração de Dados

        for local, endereco in zip(self.database["local"], self.database["endereco"]):
            self.selecao.insert("", END, values=(local, endereco))


        # Criando o botão que é responsavel por gerar mst
        #self.button_mst = Button(self.frame1, text = "Gerar MST", font = ("Courier", 15), command = self.exibir_tela2, bd = 4)

        # Definindo posição na tela de cada elemento
        self.frame1.place(relx=0, rely=0, relheight=1, relwidth=1)
        self.titulo_inicial.place(relx=0.15, rely=0.03, relwidth=0.7)
        self.descricao_inicial.place(relx=0.10, rely=0.10, relwidth=0.8)
        self.commando.place(relx=0.10, rely=0.18, relwidth=0.8)
        self.selecao.place(relx=0.10, rely=0.25, relwidth=0.8, relheight=0.55)
        #self.button_mst.place(relx=0.45, rely=0.83, relwidth=0.10)
        self.objetivo.place(relx=0.10, rely=0.9, relwidth=0.8)
        self.scroolselecao.place(relx=0.9,rely=0.25, relheight=0.55, relwidth=0.02)

    def visualizar_grafos(self):
        plt.close()

        grafo = nx.Graph()  # Inicializando o grafo
        grafo.add_weighted_edges_from(self.mst) # Adicionando os vertices, arestas e pesos

        pos = nx.kamada_kawai_layout(grafo)  # Layout que calcula a posição dos vertices e arestas
        fig = plt.figure()
        ax = fig.add_subplot(111)

        # Desenhar os nós
        nx.draw_networkx_nodes(grafo, pos, node_size=300, node_color='skyblue')

        # Desenhar as arestas
        nx.draw_networkx_edges(grafo, pos, alpha=0.5)

        edge_labels = nx.get_edge_attributes(grafo, "weight") # Obtendo os pesos das arestas

        nx.draw_networkx_edge_labels(grafo, pos, font_size=8, edge_labels=edge_labels)  # Desenhando os pesos
        nx.draw_networkx_labels(grafo, pos, font_size=5, font_weight='bold')  # Desenhando os vertices

        ax.axis('off')   # Tirando bordas

        canvas = FigureCanvasTkAgg(fig, master=self.aba1)
        canvas_widget = canvas.get_tk_widget()

        # Inserido a barra de navegação
        toolbar = NavigationToolbar2Tk(canvas, self.aba1)
        toolbar.update()
        canvas_widget.place(relx=0, rely=0, relwidth=1, relheight=1)    
