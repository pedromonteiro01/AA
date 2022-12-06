import os, json, random, time

def get_graph(n,p):
    file = 'graph'+str(n)+'-'+str(p)+'.txt'
    if os.path.exists(file):
        with open(file) as f:
            return json.loads(f.readline()), json.loads(f.readline())

def get_new_graph():
    file = 'SWlargeG.txt'
    edges = []
    vertices = set()
    if os.path.exists(file):
        with open(file) as f:
            for line in f:
                line = line.strip().split(" ")
                edges.append([line[0], line[1]])
                vertices.update({line[0], line[1]})
    
    return list(vertices), edges


def randomized_search():
    v,e = get_graph(14,50)
    #v,e = get_new_graph()
    edges_copy = e[:] # copy edges list
    unique_vertices = set()
    min_edge = 0
    while len(unique_vertices) != len(v): # while all vertices are not chosen
        selected_edge = random.choice(e) # pick a random edge
        if selected_edge in edges_copy: # check if was already picked
            edges_copy.remove(selected_edge) 
            unique_vertices.update({selected_edge[0], selected_edge[1]}) # add to set with vertices already chosen
            min_edge+=1

    return min_edge, len(e)

min_prev=9999999999999
num_simulations = 100000
start = time.time()
for i in range(num_simulations):
    min_edge, edge = randomized_search()
    if min_edge < min_prev:
        min_prev = min_edge
end = time.time()
print("time: ", end - start)
print("min edge: ", min_prev)
