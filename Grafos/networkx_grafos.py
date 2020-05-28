# pip install networkx  . para instalar biblioteca

#1-Carga el fichero que has generado (trump_graph.csv) y y visualiza el grafo de la
#red utilizando la biblioteca networkx. Carga el grafo como un grafo no dirigido (nx.Graph)

import pickle
from pathlib import Path
import csv
import pandas as pd
# instalar biblioteca networkx
# %pip install networkx
import networkx as nx

Grafo = nx.Graph() # crear un grafo

with open('trump_graph.csv', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        #Añadir nodos
        Grafo.add_node(row)

#Si quieremos mostrar gráficamente el resultado podemos usar graphviz.
#pip install graphviz

import graphviz

A = nx.nx_agraph.to_agraph(Grafo)
A.layout('GRAFO')
#A.draw('salida.png') # guardar como png

graphviz.Source(A.to_string()) # mostrar en jupyter
