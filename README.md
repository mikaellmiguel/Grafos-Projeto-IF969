<div align="center">
<img src="https://github.com/mikaellmiguel/Grafos-Projeto-IF969/assets/144696910/327c4a37-5ee5-430c-aff6-dca77b453882"  />
</div>

<h1 align="center">Gerador de MST com Prim em Python</h1> 
  <h3 align="center">Algoritmo e Estrutura de Dados - 2023.2 CIn/UFPE - Grupo #3.2 
  </h3>
   <h3 align="center">Discentes: Mikaell Miguel e Pablo Henrique 
  </h3>

<p align="center">
<br />
  <a href="https://github.com/mikaellmiguel/Grafos-Projeto-IF969"><strong>Ir para o repositório »</strong></a>
<br />
</p>

<p align="center">
    Descrição: Projeto de Grafos utilizando o algoritmo de prim para a disciplina IF 969 - Algoritmos e Estrutura de Dados do Curso de Sistemas de Informação do CIn - UFPE  
</p>

## Requesitos Mínimos ⚠️
* Estar em um ambiente desktop 🖥️
* Ter o Python instalado
* Ter uma IDE com suporte ao Python Instalada
* Ter um monitor com resolução acima ou igual a 1024x720

### Verifique a instalação das seguintes bibliotecas

Pandas, Networkx, Tkinter, Matplotlib, Scipy e Geopy.

Se não possuir algumas delas instale da seguinte forma:

```{r, echo=FALSE, warning=FALSE}
pip install pandas
pip install networkx
pip install tkinter
pip install matplotlib
pip install scipy
pip install geopy
```

## Organização do Codigo
Arquivo  | Função
:--------:| -------------
 <a href="https://github.com/mikaellmiguel/Grafos-Projeto-IF969/blob/main/classes.py">classes.py</a>|  Este arquivo, classes.py, é responsável por definir as classes e estruturas de dados que formam o programa, ou seja, contém a definição dos atributos dos objetos e os seus comportamentos (os métodos). É onde foi criado a estrutura de fila de prioridade (Heap de Mínimo) e a estrutura do Grafo.
<a href="https://github.com/mikaellmiguel/Grafos-Projeto-IF969/blob/main/functions.py">functions.py</a>| O arquivo possui as funções que serão utilizadas no projeto. Nesse caso, o arquivo contém a implmentação do **algoritmo de prim** que será utilizado para geração da mst.
<a href="https://github.com/mikaellmiguel/Grafos-Projeto-IF969/blob/main/gui.py">gui.py</a> | O arquivo gui.py é um arquivo que foi projetado totalmente para a criação da GUI (graphical user interface), ou seja, é nesse arquivo que é realizado a criação da interface gráfica do programa criado no projeto.
<a href="https://github.com/mikaellmiguel/Grafos-Projeto-IF969/blob/main/main.py">main.py</a>| O arquivo main.py é o que deve ser executado para que o usuário tenha acesso ao programa, é nele que são criado os objetos (grafo e interface gráfica) usando as classes. Além disso, é nele que é lido a base de dados e ocorre a inserção no grafo 


## Contexto do problema 
Na cidade do Recife (PE), existe um programa chamado Conecta Recife, um programa inovador espalha pontos de WIFI pela cidade, possibilitando o acesso de todos à internet (Prefeitura do Recife, 2023). Com base nisso, se a prefeitura fosse projetar uma rede que conecta cada ponto de WIFI desse programa da Cidade de Recife, de que maneira isso seria menos custoso em termos de infraestrutura de rede (menor metragem de cabo)?. Uma abordagem eficiente para este projeto seria a utilização de uma Minimum Spanning Tree (MST), já que a MST é uma árvore de custo mínimo que conecta todos os pontos de uma rede, garantindo que todos os pontos estejam conectados entre si com o menor custo possível, além de garantir que não tenha cabos redundantes e consequentemente um menor valor na execução do projeto.

### Base de Dados 📂
A Base de dados foi retirada do site dados recife e tem por título Localidades do Conecta Recife Wifi, que lista a Localidade de pontos de acesso à Internet gratuita disponibilizados pela prefeitura da cidade do Recife.

#### Contéudo
A Base contém **a rpa (Região Político Administrativa), região, bairro, local, quantidade de zonas, endereço e coordenadas geográficas (Latitude e Longitude)** referentes aos pontos de acesso. Alguns campos serão úteis para resolução do problema proposto, por isso a escolha da base.

## Implementação
### Algoritmo utilizado
Algoritmo de Prim: O algoritmo de Prim é um algoritmo guloso, empregado para encontrar uma árvore geradora mínima num grafo conectado, com pesos e não direcionado, diferentes de outros algoritmos de geração de MST’s o de prim requer necessariamente um grafo conexo. Ele requer um vértice de início que a partir dele vão sendo criados subgrupos com as arestas de menor peso. (ALMEIDA, 2018). Para apoiar a implementação, utilizou-se um heap de mínimo já que constantemente é necessário extrair a aresta de menor peso.

### Desenvolvimento 👨‍💻
Inicialmente, foram criadas as estruturas de dados que seriam utilizadas para resolução do problema (O Grafo e o Heap de Mínimo), com o apoio dessas estruturas de dados foi desenvolvido o algoritmo responsável por gerar a Árvore de Custo Mínimo, o algoritmo de prim, após isso, foi realizada a leitura da base de dados e o tratamento da mesma, através da base de dados foram criados os vértices (que são os locais de ponto de acesso), as arestas (os vértices se conectam a outros vértices que estejam na mesma Região Político Administrativa (RPA) ou em vizinhas) e os pesos que são distância (Exibidas em metros) entre os vértices com base nas coordenadas geográficas da base. Por fim, foi criado o visualizador de grafos através do uso conjunto das bibliotecas Networkx, Matplotlib e Tkinter, e também a interface gráfica composta por duas telas, a tela inicial que escolhe o vértice de início e a segunda tela que demonstra duas visualizações (grafo e tabela).

### Bibliotecas utilizadas. 📚
**Pandas:** Biblioteca que fornece ferramentas de ferramentas poderosas para leitura, análise e limpeza de dados tabulares. Utilizada no projeto para realizar a leitura da Base de Dados e para obtenção dos valores desejados da base de dados discutida anteriormente.  

**Networkx:** é uma Bibloteca com uma ampla de gama de algoritmo que realiza a criação, manipulação de grafos, sendo utilizada, no projeto para manipular a MST e integrar ao mathplotlib para visualização 2D do grafo.  

**Geopy:** é uma biblioteca Python para trabalhar vários serviços web de geocodificação populares e inclui o módulo distance que calcula distância geográficas, utilizada para realizar o cálculo de distância de acordo com as coordenadas disponibilizadas na base de dados.  

**Tkinter:** O Tkinter é uma biblioteca que acompanha o python sendo utilizada para criação de interfaces gráficas simples. Foi utilizada para criação da interface do projeto.  

**Matplotlib:** O pacote Matplotlib é uma das bibliotecas gráficas mais empregadas para visualização de dados em Python (OLIVEIRA, 2020). A Biblioteca foi utilizada para exibir a visualização na tela gerada pelo Tkinter do grafo feito no Networkx.  

## Conclusão
O Programa funciona em uma interface gráfica que é dividida em duas telas, onde a tela inicial exibe uma tabela de seleção para escolha do vértice inicial, ao escolher o vértice e clicar no botão “Gerar MST”, ele vai executar o algoritmo de prim com o vértice inicial escolhido e em poucos segundos irá para segunda tela onde conterá duas abas uma de visualização gráfica e outra em tabela da Árvore de custo mínimo, na segunda tela além de conter os tipos de visualização da MST, ela contém o custo total de todas as arestas da MST e também contém um botão “voltar” que retorna à tela inicial, para fechar o aplicativo clique no botão de fechar a janela.

### Capturas de Tela


<h3 align="center">Imagem 1 - Tela Inicial</h3>

<div align="center">
<img src="https://github.com/mikaellmiguel/Grafos-Projeto-IF969/assets/144696910/d82598eb-0fdb-41cc-ba0c-d01764dc8b68" />
</div>

Selecione o vértice (Local) e clique em gerar MST, pode demorar um pouco por causa dos cálculos para posicionamento dos vértices na visualização gráfica 

<h3 align="center">Imagem 2 - Tela Secundária, ABA: Visualização em grafo</h3>

<div align="center">
<img src="https://github.com/mikaellmiguel/Grafos-Projeto-IF969/assets/144696910/ee27e5fb-1124-4dae-ac34-0a87b035bd1a" />
</div>

Nessa tela é possível visualizar a árvore de custo mínimo, recomenda-se aplicar a
ferramenta de zoom disponibilizada no canto inferior esquerdo da tela.

<h3 align="center">Imagem 3 - Tela Secundária, ABA: Visualiação em tabela</h3>

<div align="center">
<img src="https://github.com/mikaellmiguel/Grafos-Projeto-IF969/assets/144696910/ab086983-294a-4303-8a69-364ad9a36c54" />
</div>

Nessa tela é possível ver a visualização em tabela, os pesos são representados em metro e
os vértices são os nomes dos locais, assim como na visualização gráfica.

