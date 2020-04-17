#Responsavel por gerar grafos aletórios para Testes do algoritmo
#em txt e de forma gráfica

'''
Formato do Arquivo de saída:

N M 
n m m m . . .
n m m m . . .
n m m m . . .
. . . .
. . . .
. . . .

'''
import random
import sys
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

n= param  = sys.argv[1] #recebe número de vertices
n = int(n)
saida = ''
valores = [1]*int(30/n) + [0]*int(70/n)
G = nx.Graph()

for i in range(n):
    G.add_node(i)

for i in range(n):
    lista_de_vertices = []
    for j in range(n-1):
        
        if (i == j):
            lista_de_vertices.append(0)

        vertice_sorteado = random.choice(valores)

        lista_de_vertices.append(vertice_sorteado)

        if (i == n-1 and j+1 == i):
            lista_de_vertices.append(0)

    for v in range(len(lista_de_vertices)):
        if i == v: pass
        if(lista_de_vertices[v] == 1):
            G.add_edge(i,v )

    #saida += str(lista_de_vertices) + " (" + str(i) + ")"+ "\n" 
    
    saida += str(lista_de_vertices) + "\n" 

saida = saida.replace("[","")   
saida = saida.replace("]","") 
print(saida)

pos = nx.kamada_kawai_layout(G)
cores = ["blue"] * (n)

nodes = nx.draw_networkx_nodes(G, pos, node_size=130, node_color=cores, label=True) #desenhando nodes
label = nx.draw_networkx_labels(G, pos, font_size=8, font_family="Arial", font_color='white')#desenhando nomes/labes nos nodes
edges = nx.draw_networkx_edges(G, pos, width=1)#desenhando arestas
ax = plt.gca()
ax.set_axis_off()
plt.savefig("Grafo.png", format="PNG") #salvando grafo
plt.show() #exibindo o grafo graficamente

arq = open('grafo'+str(n) +'.txt', 'w')
arq.write(saida)
arq.close()
