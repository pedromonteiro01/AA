# @Author: Pedro Monteiro
# @Email:  pmapm@ua.pt

import networkx as nx
import matplotlib.pyplot as plt

def get_adjacency_list(edges):
    adj_list = {}
    
    for v1, v2 in edges:
        if v1 not in adj_list.keys():
            adj_list[v1] = list(v2)
        else:
            adj_list[v1].append(v2)
            
        if v2 not in adj_list.keys():
            adj_list[v2] = list(v1)
        else:
            adj_list[v2].append(v1)

    return adj_list

def show_adjacency_matrix(vertexes, edges):
    adj_matrix = [[0 for _ in range(len(vertexes))]for _ in range(len(vertexes))] # start matrix with 0's
    v_list = [v[0] for v in vertexes] # [v1, v2, v3, v4, ...]

    for e in edges:
        x = v_list.index(e[0]) # get index of vertex 1
        y = v_list.index(e[1]) # get index of vertex 2
        adj_matrix[x][y] = 1 # change matrix from 0 to 1 on (a,b)
        adj_matrix[y][x] = 1 # change matrix from 0 to 1 on (b,a)

    for el in adj_matrix:
        print(el)
    
    return adj_matrix

def show_incidence_matrix(vertexes, edges):
    inc_matrix = [[0 for _ in range(len(edges))]for _ in range(len(vertexes))] # start matrix with 0's
    v_list = [v[0] for v in vertexes] # [v1, v2, v3, v4, ...]

    for i, e in enumerate(edges):
        x = v_list.index(e[0]) # get index of vertex 1
        y = v_list.index(e[1]) # get index of vertex 2
        inc_matrix[x][i] = 1 # change matrix from 0 to 1
        inc_matrix[y][i] = 1 # change matrix from 0 to 1
    
    return inc_matrix

def show_graph(e):
    G = nx.Graph()
    for edge in e:
        G.add_edge(edge[0],edge[1])
    nx.draw(G, node_size=700 , with_labels=True)
    plt.show()

def show_results_graph():
    plt.plot([0, 1, 2, 3, 4, 5], [0, 1, 4, 9, 16, 25])
    plt.grid()
    plt.show()
