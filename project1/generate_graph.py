# @Author: Pedro Monteiro
# @Email:  pmapm@ua.pt

import random, string

#random.seed(97484) # seed = student number
alphabet = list(string.ascii_lowercase) # get alphabet letters to use as vertex

def generate_graph(n): # create a graph with n vertexes
    vertexes = []
    edges = []

    if 0 < n < len(alphabet): # n should be greater than 0 and less than letters available
        for i in range(1, n+1): # generate n vertexes
            coords = []
            x = random.randint(1, 20)
            y = random.randint(1, 20)
            if (x,y) not in coords:
                coords.append((x,y))
            vertexes.append([alphabet[i-1], (x,y)]) # [['a', (x,y)], ['b', (x,y)], ['c', (x,y)], ...]
    
    # according to graph theory n-1 is the minimum number of edges
    min_edges = n-1
    # according to graph theory n*((n-1)/2) is the maximum number of edges
    max_edges = int(n*(n-1)/2)
    # pick a random number of edges between min and max
    num_edges = random.choice([i for i in range(min_edges, max_edges)])

    for _ in range(0, num_edges):
        while True: # because if v1 == v2 ignores and dont append an edge
            v1 = random.choice(vertexes)[0]
            v2 = random.choice(vertexes)[0]
            if v1 != v2:
                if (v1,v2) not in edges and (v2,v1) not in edges:
                    edges.append((v1,v2))
                    break

    return vertexes, edges

def get_adjacency_list(edges):
    adj_list = {}
    print(sorted(edges))
    for v1, v2 in edges:
        if v1 not in adj_list.keys():
            adj_list[v1] = list(v2)
        else:
            adj_list[v1].append(v2)
            
        if v2 not in adj_list.keys():
            adj_list[v2] = list(v1)
        else:
            adj_list[v2].append(v1)

    for k in sorted(adj_list.keys()):
        print(k, ":", adj_list[k])

    return adj_list

def show_adjacency_matrix(vertexes, edges):
    adj_matrix = [[0 for _ in range(len(vertexes))]for _ in range(len(vertexes))] # start matrix with 0's
    v_list = [v[0] for v in vertexes] # [v1, v2, v3, v4, ...]

    for e in edges:
        x = v_list.index(e[0]) # get index of vertex 1
        y = v_list.index(e[1]) # get index of vertex 2
        adj_matrix[x][y] = 1 # change matrix from 0 to 1
        adj_matrix[y][x] = 1

    for el in adj_matrix:
        print(el)

def show_incidence_matrix(vertexes, edges):
    inc_matrix = [[0 for _ in range(len(vertexes))]for _ in range(len(edges))] # start matrix with 0's
    v_list = [v[0] for v in vertexes] # [v1, v2, v3, v4, ...]

    print("\n")
    for el in inc_matrix:
        print(el)


v,e = generate_graph(4)
adj_list = get_adjacency_list(e) 
show_adjacency_matrix(v, e)
show_incidence_matrix(v,e)