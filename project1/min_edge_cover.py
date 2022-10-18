# @Author: Pedro Monteiro
# @Email:  pmapm@ua.pt

import json, itertools, time

from matplotlib.pyplot import get
import os

from utils import get_adjacency_list, show_incidence_matrix


def get_graph(n,p):
    file = 'graph'+str(n)+'-'+str(p)+'.txt'
    if os.path.exists(file):
        with open(file) as f:
            return json.loads(f.readline()), json.loads(f.readline())

def find_solution(v,e):
    v_list = {vertex[0] for vertex in v} # set with all vertexes

    for i in range(1, len(v_list)+1):
        for data in itertools.combinations(e, i): # get all subsets of edges
            temp_set = set()
            #print("data: ",list(data))
            for item in data:
                temp_set.update({item[0], item[1]}) # add {'x1', 'x2} to set
                if sorted(v_list) == sorted(temp_set): # only covering edges here!
                    return i

    return None

def find_solution_with_inc_matrix(v,e):
    v_list = [vertex[0] for vertex in v] # set with all vertexes
    for i in range(1, len(v_list)+1):
        for data in itertools.combinations(e, i): # get all subsets of edges
            adj = get_adjacency_list(list(data))
            if [] not in adj.items() and len(adj) == len(v_list): # when all vertices from the graph have at least 1 edge
                return i

percentages = [12.5]
with open('brute_force_results.txt', 'w') as result_file:
    #result_file.write(f"n \t\tpercentage \t\tedges \t\tmin_edge \t\ttime\n")
    for i in range(20,25):
        for p in percentages:
            file = 'graph'+str(i)+'-'+str(p)+'.txt'
            if os.path.exists(file):
                with open(file) as f:
                    v,e = json.loads(f.readline()), json.loads(f.readline())
                    v,e = get_graph(i,p)
                    #start = time.time()
                    #min_edge = find_solution(v,e)
                    #end = (time.time() - start)
                    #inc_matrix = show_incidence_matrix(v,e)
                    start = time.time()
                    min_edge = find_solution_with_inc_matrix(v,e)
                    end = (time.time() - start)
                    #result_file.write("%s %10s %10s %10s %10s\n" % (len(v), p, len(e), min_edge, end))
                    #print("num_v: ", len(v), "num_edges: ", len(e), "percentage: ", p)
                    print("min_edge: ",min_edge)
                    print(end)