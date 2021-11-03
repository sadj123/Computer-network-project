from itertools import count


import random as rd
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.shortest_paths import weighted
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
    G=nx.read_edgelist("data.csv", delimiter=",", data=[("weight", int)], create_using=nx.DiGraph())
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
    m = int(n + n / 2)
    G = nx.DiGraph(directed=True)  # Creamos el grafo
    G.add_nodes_from(nodos)

    # Lista para añadir aristas
    count = 0
    aristas_ready = []

    # Lista de los pesos
    pesos = []
    for i in range(m):
        pesos.append(rd.randint(1, 15))


    while count < m:
        # print("entre")
        vini = rd.randint(1, n)
        vfin = rd.randint(1, n)
        # print(vini, vfin)
        if (vini, vfin) in aristas_ready or vini == vfin:
            continue
        else:
            G.add_edge(vini, vfin, weight=pesos[count])
            aristas_ready.append((vini, vfin))
            count += 1
    options = {
        "node_color": "lightblue",
        "node_size": 200,
        "width": 1,
        "arrowstyle": "-|>",
        "arrowsize": 10,
    }
    # Matriz de dispersion
    matrix = np.zeros((m, 3))
    aristas = list(G.edges())
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
    end=input("Seleccione un nodo de destino: ")
    while int(end) not in G.nodes():
        print("Lo sentimos, este nodo no se encuentra en la red")
        end=input("Seleccione un nodo de destino: ")


    try: 
        djiks= nx.dijkstra_path(G, source=int(ori), weight= "weight", target=int(end))
        print(djiks)
    except:
        print("No hay camino hacia ese nodo")
else: 
    ori=input("Seleccione un nodo de origen: ")
    while ori not in G.nodes():
        print("Lo sentimos, este nodo no se encuentra en la red")
        ori=input("Seleccione un nodo de origen: ")
    end=input("Seleccione un nodo de destino: ")
    while end not in G.nodes():
        print("Lo sentimos, este nodo no se encuentra en la red")
        end=input("Seleccione un nodo de destino: ")


    try: 
        djiks= nx.dijkstra_path(G, source=ori, weight= "weight", target=end)
        print(djiks)
    except:
        print("No hay camino hacia ese nodo")
