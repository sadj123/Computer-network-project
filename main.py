from itertools import count
import time

import random as rd
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.shortest_paths import weighted
from networkx.generators import directed
import numpy as np
import os


def question():
    print("What is your operative system?\n\t1.Linux or mac.\n\t2.Windows")
    choise = input("\t   >> ")
    if choise == "1":
        c = "clear"
    elif choise == "2":
        c = "cls"
    else:
        print("Error")
        c = question()
    return c


c = question()
os.system(c)
print("===================BIENVENIDO========================\n")
print("Seleccione una opción entre A y B")
print("A: Tomar los datos a traves de un csv ingresado a la carpeta")
print("B: ¡Python genera los datos al azar!\n")
des1= 0
while des1!= 'A' or des1!='B':
    des1=input("Su seleccion : ").upper()
    if des1== 'A' or des1=='B':
        break
    print("Opcion no valida\n")

if des1=='A':
    #data=pd.read_csv('data.csv')
    G=nx.read_edgelist("data.csv", delimiter=",", data=[("weight", int)], create_using=nx.Graph())
    options = {
        "node_color": "lightblue",
        "node_size": 200,
        "width": 1,
        "arrowstyle": "-|>",
        "arrowsize": 10,
    }
    nx.draw_circular(G, arrows=True, with_labels=1, font_size=6, **options)
    plt.show()
elif des1=='B' or 'b':

    # n es el numero de nodos
    n = rd.randint(15, 50)

    nodos = [x + 1 for x in range(n)]  # Creamos la lista de nodos

    # m es el numero de arcos
    G = nx.Graph() # Creamos el grafo
    G.add_nodes_from(nodos)

    # Lista para añadir aristas
    aristas_ready = []
    nodes_conected=[]
    # Lista de los pesos


    while len(nodes_conected) < len(list(G.nodes())):
        print(nodes_conected)
        vini = rd.randint(1, n)
        vfin = rd.randint(1, n)
        # print(vini, vfin)
        if (vini, vfin) in aristas_ready or vini == vfin or (vfin, vini) in aristas_ready:
            continue
        else:
            G.add_edge(vini, vfin, weight=rd.randint(1, 15))
            aristas_ready.append((vini, vfin))
            if vini not in nodes_conected:
                nodes_conected.append(vini)
            if vfin not in nodes_conected:
                nodes_conected.append(vfin)
    options = {
        "node_color": "lightblue",
        "node_size": 200,
        "width": 1,
        "arrowstyle": "-|>",
        "arrowsize": 10,
    }
    # Matriz de dispersion
    aristas = list(G.edges())
    matrix = np.zeros((len(aristas), 3))
    for idx in range(len(G.edges())):
        # print(idx)
        matrix[idx][0] = aristas[idx][0]
        matrix[idx][1] = aristas[idx][1]
        matrix[idx][2] = G.get_edge_data(aristas[idx][0], aristas[idx][1])["weight"]

    print("A continuación tenemos la matriz de disperción:\n")
    # print(matrix)

    # Para sacarlo como una tabla:
    print("| Nodo origen | Nodo destino | Peso del arco |")  # Los titulos de las columnas
    print("----------------------------------------------")
    for item in matrix:
        print(
            "|",
            " " * (3),
            item[0],
            " " * (6 - len(str(item[0]))),
            "|",
            " " * (3),
            item[1],
            " " * (7 - len(str(item[1]))),
            "|",
            " " * (3),
            item[2],
            " " * (8 - len(str(item[2]))),
            "|",
        )

    nx.draw_circular(G, arrows=True, with_labels=1, font_size=6, **options)
    plt.show()

os.system(c)
des=0
print("Una vez visto el grafo. Presione Enter para ejecutar el algoritmo de Djikstra")
while des!= "":
    des=input("")
if des1== 'B':
    ori=input("Seleccione un nodo de origen: ")

    while int(ori) not in G.nodes():
        print("Lo sentimos, este nodo no se encuentra en la red")
        ori=input("Seleccione un nodo de origen: ")

    caminos= {}
    start= time.time()
    for d in range(len(G.nodes())):
        try: 
            djiks= nx.dijkstra_path(G, source=int(ori), weight= "weight", target=list(G.nodes())[d])
            
            
            if list(G.nodes())[d]==int(ori):
                continue
            else:

                caminos[list(G.nodes())[d]]= djiks
        except:
            
            continue
    end= time.time()
    print(f"Runtime of the program is {end - start}")
    A=nx.Graph()
    for k in caminos.keys():
        A.add_node(k)
    for v in caminos.values():
        for m in range(len(v)-1):
            A.add_edge(v[m], v[m+1])
    nx.draw_planar(A, arrows=True, with_labels=1, font_size=6, **options)
    dijk2=nx.dijkstra_predecessor_and_distance(G, source=int(ori)) 
    m= len(dijk2[0])
    matrix = np.zeros((m-1, 3))
    count=0
    for k in dijk2[0].keys():
        v=list(dijk2[0].values())
        matrix[count][0]=k
        matrix[count][1]=dijk2[1][k]
        if len(dijk2[0][k])==0:
            matrix[count][2]=k
            continue
        else:
            matrix[count][2]=dijk2[0][k][-1]
        count+=1
    print("A continuación tenemos la tabla de enrutamiento:\n")
    # print(matrix)

    # Para sacarlo como una tabla:
    print("|     Nodo    |     Costo    |   Predecesor  |")  # Los titulos de las columnas
    print("----------------------------------------------")
    for item in matrix:
        print(
            "|",
            " " * (3),
            item[0],
            " " * (6 - len(str(item[0]))),
            "|",
            " " * (3),
            item[1],
            " " * (7 - len(str(item[1]))),
            "|",
            " " * (3),
            item[2],
            " " * (8 - len(str(item[2]))),
            "|",
        )
    plt.show()
else: 
    ori=input("Seleccione un nodo de origen: ")
    while ori not in G.nodes():
        print("Lo sentimos, este nodo no se encuentra en la red")
        ori=input("Seleccione un nodo de origen: ")
    caminos= {}
    start= time.time()
    for d in range(len(G.nodes())):
        try: 
            
            djiks= nx.dijkstra_path(G, source=ori, weight= "weight", target=list(G.nodes())[d])
            if list(G.nodes())[d]==ori:
                continue
            else:

                caminos[list(G.nodes())[d]]= djiks
        except:
            
            continue
    end= time.time()
    print(f"Runtime of the program is {end - start}")
    A=nx.Graph()
    for k in caminos.keys():
        A.add_node(k)
    for v in caminos.values():
        for m in range(len(v)-1):
            A.add_edge(v[m], v[m+1])
    nx.draw_planar(A, arrows=True, with_labels=1, font_size=6, **options)
    dijk2=nx.dijkstra_predecessor_and_distance(G, source=ori) 
    m= len(dijk2[0])
    matrix = np.zeros((m-1, 3))
    count=0
    for k in dijk2[0].keys():
        v=list(dijk2[0].values())
        matrix[count][0]=k
        matrix[count][1]=dijk2[1][k]
        if len(dijk2[0][k])==0:
            matrix[count][2]=k
            continue
        else:
            matrix[count][2]=dijk2[0][k][-1]
        count+=1
    print("A continuación tenemos la tabla de enrutamiento:\n")
    # print(matrix)

    # Para sacarlo como una tabla:
    print("|     Nodo    |     Costo    |   Predecesor  |")  # Los titulos de las columnas
    print("----------------------------------------------")
    for item in matrix:
        print(
            "|",
            " " * (3),
            item[0],
            " " * (6 - len(str(item[0]))),
            "|",
            " " * (3),
            item[1],
            " " * (7 - len(str(item[1]))),
            "|",
            " " * (3),
            item[2],
            " " * (8 - len(str(item[2]))),
            "|",
        )
    plt.show()