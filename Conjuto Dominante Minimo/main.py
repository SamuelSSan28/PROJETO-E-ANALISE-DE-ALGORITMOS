import networkx as nx
import matplotlib.pyplot as plt
import sys

def find_ccdm(G):
    '''
    Encontra o CONJUNTO CONECTADO DOMINANTE MÍNIMO
    '''
    adjacencia = {}
    for i in G.adj:
        lista  = list(G[i])
        lista.append(i)
        adjacencia.update({i: lista})
    
    print(adjacencia)

    transmissores = {}
    
    for i in adjacencia: 
       # print("Transmissores:",transmissores)

        for j in transmissores:
            if len(adjacencia[i]) > len(adjacencia[j]) and set(adjacencia[j]).intersection(adjacencia[i]) == set(adjacencia[j]):
                print("Troca:", len(adjacencia[j]),len(adjacencia[i]))
                j = i
                
        if set(adjacencia[i]).difference(Conjunto_Visitado(transmissores,adjacencia) ):
            print("Novo",i,adjacencia[i])
            transmissores.update({i:adjacencia[i]})
           
        

    print(len(Conjunto_Visitado(transmissores,adjacencia)))

def Conjunto_Visitado(transmissores,grafo):
    conjunto = []
    for i in transmissores:
        for j in grafo[i]:
            if j not in conjunto:    conjunto.append(j)
            
    print("Conjuto:",conjunto)
    return conjunto
                
     

    


n= param  = sys.argv[1] #recebe número de vertices
n = int(n)
arq = open('grafo'+str(n) +'.txt', 'r')
matriz_adjacencia = []
G = nx.Graph()
converte_int = lambda a : int(a)

for i in arq: 
    vertices_string = i.split(",")
    vertices_int = list(map(converte_int,vertices_string))
    matriz_adjacencia.append(vertices_int)

for i in range(n):
    G.add_node(i)

for i in range(n):
    for v in range(len(matriz_adjacencia[i])):
        if i == v: pass
        if(matriz_adjacencia[i][v] == 1):
            G.add_edge(i,v)

find_ccdm(G)


 



                