from itertools import count
import random as rd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


#n es el numero de nodos
n = rd.randint(15, 50)

nodos=[x+1 for x in range(n)] #Creamos la lista de nodos

#m es el numero de arcos
m= int(n+n/2)
print(m)
G = nx.DiGraph(directed=True) #Creamos el grafo
G.add_nodes_from(nodos)

count=0
aristas_ready=[]
while count <=m:
    print("entre")
    vini= rd.randint(1, n)
    vfin= rd.randint(1, n)
    print(vini, vfin)
    if (vini, vfin) in aristas_ready or vini==vfin:
        continue
    else:
        G.add_edge(vini, vfin)
        aristas_ready.append((vini,vfin))
        count+=1
options = {
    'node_color': 'blue',
    'node_size': 500,
    'width': 3,
    'arrowstyle': '-|>',
    'arrowsize': 12,
    
}
nx.draw_networkx(G, arrows=True, **options)
plt.show()