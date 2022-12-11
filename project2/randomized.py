from math import log2
import os, json, random, time, itertools

def get_graph(n,p):
    file = 'graph'+str(n)+'-'+str(p)+'.txt'
    if os.path.exists(file):
        with open(file) as f:
            return json.loads(f.readline()), json.loads(f.readline())

def get_new_graph():
    file = 'lastfm_asia_edges.csv'
    edges = []
    vertices = set()
    if os.path.exists(file):
        with open(file) as f:
            for line in f:
                line = line.strip().split(",")
                edges.append([line[0], line[1]])
                vertices.update({line[0], line[1]})
    
    return list(vertices), edges

def get_edges_number(e):
    return len(e)

def randomized_search(v,e):
    operations = 0 # initialize operations counter variable
    edges_copy = e[:] # copy edges list
    unique_vertices = set()
    min_edge = 0
    operations += 3
    solution = set()
    while len(unique_vertices) != len(v): # while all vertices are not chosen - O(v) vezes
        selected_edge = random.choice(edges_copy) # pick a random edge
        operations += 2
        if selected_edge in edges_copy: # check if was already picked
            edges_copy.remove(selected_edge) # O(e) vezes
            solution.add(tuple(selected_edge))
            unique_vertices.update({selected_edge[0], selected_edge[1]}) # add to set with vertices already chosen
            min_edge+=1
            operations += 4

    return min_edge, operations, solution

percentages = [12.5, 25, 50, 75]
with open('randomized_results.txt', 'w') as result_file:
    result_file.write(f"n \t\t\tpercentage \t\t\tedges \t\t\t\tmin_edge \t\t\t\toperations \t\t\t\tsolutions \t\ttime \n")
    for n in range(3,21):
        for p in percentages:
            file = 'graph'+str(n)+'-'+str(p)+'.txt'
            solutions = set()
            if os.path.exists(file):
                with open(file) as f:
                    v,e = get_graph(n,p)
                    min_prev=9999999999999 # set variable high to be updated
                    num_edges = get_edges_number(e) # get edges number -> len(e)
                    combinations = 2**(num_edges)-1
                    num_simulations = max([100, round(log2(combinations)*num_edges*len(v)*10)]) # calculate number of simulations, using 60%
                    #print("Iterations: ", num_simulations)
                    start = time.time()
                    timeout = time.time() + 60*5   # 5 minutes from now
                    for i in range(num_simulations):
                        min_edge, operations, solution = randomized_search(v,e) # perform randomized search
                        while solution in solutions:
                            min_edge, operations, solution = randomized_search(v,e) # prevent from test same solution
                        
                        solutions.add(tuple(solution))
                        if min_edge < min_prev: # update min edge value when is less than the previous one
                            min_prev = min_edge
                        if time.time() > timeout: # prevent algorithm from taking to much time to run
                            print("exceeded time")
                            break
                    end = time.time()
                    result_file.write(f"{len(v)} \t\t\t{p} \t\t\t\t\t{len(e)} \t\t\t\t\t{min_prev} \t\t\t\t\t\t{operations} \t\t\t\t{len(solutions)} \t\t\t\t{end - start}\n")
                    #print("Vertices: ", len(v),"%: ", p,"time: ", end - start, "min edge: ", min_prev, "operations: ", operations, "solutions: ", len(solutions))