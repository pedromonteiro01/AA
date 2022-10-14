# @Author: Pedro Monteiro
# @Email:  pmapm@ua.pt

import random, string, json

random.seed(97484) # seed = student number
alphabet = list(string.ascii_letters) # get alphabet letters to use as vertex

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
    if n > 2:
        num_edges = random.choice([i for i in range(min_edges, max_edges+1)])
    else: # in case there is only 2 vertexes, is only available 1 edge 
        num_edges = 1

    prev_v1 = ""
    prev_v2 = ""
    prev_v = set()
    for _ in range(0, num_edges):
        while True: # if v1 == v2 ignores and dont append an edge
            v1 = random.choice(vertexes)[0]
            v2 = random.choice(vertexes)[0]
            prev_v.update({v1,v2})
            prev_v1 = v1
            prev_v2 = v2
            # in case all vertices have at least one edge
            if len(vertexes) == len(prev_v):
                assert len(vertexes) == len(prev_v)
                if v1 != v2:
                    if (v1,v2) not in edges and (v2,v1) not in edges:
                        edges.append((v1,v2))
                        break
            else: # if there is any vertex that has not been chosen => graph must be connected
                if v1 != v2:
                    if (v1,v2) not in edges and (v2,v1) not in edges:
                        if (v1 != prev_v1) or (v2 != prev_v2) or (v1 != prev_v1 and v2 != prev_v2):
                            edges.append((v1,v2))
                            break

    return vertexes, edges

def get_adjacency_list(edges):
    adj_list = {}
    #print(sorted(edges))
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
        adj_matrix[x][y] = 1 # change matrix from 0 to 1 on (a,b)
        adj_matrix[y][x] = 1 # change matrix from 0 to 1 on (b,a)

    for el in adj_matrix:
        print(el)

def show_incidence_matrix(vertexes, edges):
    inc_matrix = [[0 for _ in range(len(edges))]for _ in range(len(vertexes))] # start matrix with 0's
    v_list = [v[0] for v in vertexes] # [v1, v2, v3, v4, ...]

    for i, e in enumerate(edges):
        x = v_list.index(e[0]) # get index of vertex 1
        y = v_list.index(e[1]) # get index of vertex 2
        inc_matrix[x][i] = 1 # change matrix from 0 to 1
        inc_matrix[y][i] = 1 # change matrix from 0 to 1

    for el in inc_matrix:
        print(el)

def write_to_file():
    for i in range(2,50):
        v,e = generate_graph(i)
        with open('graph-'+str(i)+'.txt', 'w') as f:
            f.write(json.dumps(v))
            f.write('\n')
            f.write(json.dumps(e))

if __name__=='__main__':
    #v = [["a", [4, 6]], ["b", [1, 3]], ["c", [4, 20]], ["d", [16, 10]], ["e", [2, 15]], ["f", [20, 16]], ["g", [4, 13]], ["h", [2, 7]], ["i", [7, 20]], ["j", [14, 13]], ["k", [5, 4]]]
    #e = [["e", "j"], ["h", "j"], ["h", "b"], ["c", "d"], ["i", "b"], ["e", "f"], ["b", "c"], ["a", "e"], ["h", "g"], ["j", "b"]]
    v,e = generate_graph(11)
    print("Vertexes: \n",v)
    print("Edges: \n",sorted(e))
    print("\nAdjacency List: ")
    adj_list = get_adjacency_list(e) 
    print("\nAdjacency Matrix: ")
    show_adjacency_matrix(v, e)
    print("\nIncidence Matrix: ")
    show_incidence_matrix(v,e)
    #write_to_file()