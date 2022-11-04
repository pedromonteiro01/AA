# @Author: Pedro Monteiro
# @Email:  pmapm@ua.pt

import random, string, json
from utils import get_adjacency_list, show_adjacency_matrix, show_incidence_matrix, show_graph

random.seed(97484) # seed = student number
alphabet = list(string.ascii_letters) # get alphabet letters to use as vertex

def generate_graph(n, p): # create a graph with n vertexes and p percentage
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
    # calculate num_edges with probability p
    if n > 2:
        num_edges = int(p/100 * max_edges)
    else: # in case there is only 2 vertexes, is only available 1 edge 
        num_edges = 1

    prev_v = set()
    if min_edges <= num_edges <= max_edges:
        for _ in range(0, num_edges):
            while True: # if v1 == v2 ignores and dont append an edge
                v1 = random.choice(vertexes)[0]
                v2 = random.choice(vertexes)[0]
                # in case all vertices have at least one edge
                #input()
                if len(vertexes) == len(prev_v):
                    assert len(vertexes) == len(prev_v)
                    if v1 != v2:
                        if (v1,v2) not in edges and (v2,v1) not in edges:
                            edges.append((v1,v2))
                            break
                else: # if there is any vertex that has not been chosen => graph must be connected
                    if v1 != v2 and (v1 not in prev_v or v2 not in prev_v):
                        prev_v.update({v1,v2})
                        if (v1,v2) not in edges and (v2,v1) not in edges:
                            edges.append((v1,v2))
                            break

    return vertexes, edges

def write_to_file():
    percentages = [12.5, 25, 50, 75]
    for p in percentages:
        for i in [3,4,5,7,8,9,10,11,12,13,14,15,16,17,18,19,20]:
            v,e = generate_graph(i,p)
            if len(e):
                with open('graph'+str(i)+'-'+str(p)+'.txt', 'w') as f:
                    f.write(json.dumps(v))
                    f.write('\n')
                    f.write(json.dumps(e))

if __name__=='__main__':
    v = [["a", [1, 13]], ["b", [8, 20]], ["c", [8, 5]], ["d", [5, 1]], ["e", [20, 16]]]
    e = [["d", "c"], ["a", "e"], ["b", "c"], ["e", "b"], ["b", "a"]]
    e2 = [["d", "c"], ["a", "e"], ["e", "b"]]

    #v,e = generate_graph(17, 12.5)
    print("Vertexes: \n",v)
    print("Edges: \n",sorted(e))
    print("num edges: ", len(e))
    print("\nAdjacency List: ")
    adj_list = get_adjacency_list(e) 
    print("\n")
    get_adjacency_list(e2)
    print("\nAdjacency Matrix: ")
    show_adjacency_matrix(v, e)
    print("\n")
    show_adjacency_matrix(v, e2)
    print("\nIncidence Matrix: ")
    print(show_incidence_matrix(v,e))
    print("\n")
    print(show_incidence_matrix(v,e2))
    #show_graph(v,e)
    write_to_file()