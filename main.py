from itertools import count
import random as rd
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.shortest_paths import weighted
import numpy as np


#n es el numero de nodos
n = rd.randint(15, 50)

nodos=[x+1 for x in range(n)] #Creamos la lista de nodos

#m es el numero de arcos
m= int(n+n/2)
G = nx.DiGraph(directed=True) #Creamos el grafo
G.add_nodes_from(nodos)

#Lista para añadir aristas
count=0
aristas_ready=[]

#Lista de los pesos
pesos=[]
for i in range(m):
    pesos.append(rd.randint(1, 15))


while count <m:
    print("entre")
    vini= rd.randint(1, n)
    vfin= rd.randint(1, n)
    print(vini, vfin)
    if (vini, vfin) in aristas_ready or vini==vfin:
        continue
    else:
        G.add_edge(vini, vfin, weight= pesos[count])
        aristas_ready.append((vini,vfin))
        count+=1
options = {
    'node_color': 'lightblue',
    'node_size': 500,
    'width': 1  ,
    'arrowstyle': '-|>',
    'arrowsize': 12,
    
}
#Matriz de dispersion
matrix= np.zeros((m, 3))
aristas= list(G.edges())
for idx in range(len(G.edges())):
    print(idx)
    matrix[idx][0]=aristas[idx][0]
    matrix[idx][1]=aristas[idx][1]
    matrix[idx][2]=G.get_edge_data(aristas[idx][0], aristas[idx][1])['weight']
    
print(matrix)


nx.draw_circular(G, arrows=True, with_labels=1, **options)
plt.show()