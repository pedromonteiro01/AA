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

def find_solution_starting_up(v,e):
    min_edge = 1000000
    iterations = 0
    for i in range(len(v), 0, -1): # start with bigger subsets
        for data in itertools.combinations(e, i): # get all subsets of edges
            temp_set = set()
            for item in data:
                iterations+=1
                temp_set.update({item[0], item[1]}) # add {'x1', 'x2} to set
                
                if len(v) == len(temp_set): # only covering edges here!
                    if i < min_edge:
                        min_edge = i

    return min_edge, iterations

def find_solution(v,e):
    operations = 0
    stop = False
    min_edge = 0
    solutions = []
    conf_tested = 0
    for i in range(1, len(v)+1):
        for data in itertools.combinations(e, i): # get all subsets of edges
            conf_tested+=1
            temp_set = set() # reset set with vertices
            for item in data:
                operations += 1
                temp_set.update({item[0], item[1]}) # add {'x1', 'x2} to set
                
                if len(v) == len(temp_set): # only covering edges here! when all vertices are in the edges subset 
                    solutions.append(data)
                    min_edge = i
                    stop = True # to be possible to count solutions found

        if stop: 
            break

    return min_edge, len(solutions), operations, conf_tested

percentages = [12.5, 25, 50, 75]
with open('brute_force_results.txt', 'w') as result_file:
    result_file.write(f"n \t\tpercentage \t\tedges \t\tmin_edge \t\ttime \t\operations \t\tsolutions \t\tconfigurations\n")
    for i in range(3,16):
        for p in percentages:
            file = 'graph'+str(i)+'-'+str(p)+'.txt'
            if os.path.exists(file):
                with open(file) as f:
                    v,e = json.loads(f.readline()), json.loads(f.readline())
                    v,e = get_graph(i,p)
                    start = time.time()
                    min_edge, solutions, operations, configurations = find_solution(v,e)
                    end = (time.time() - start)
                    print(v, len(e), min_edge, end, operations, solutions, configurations)
                    #print(f"{len(v)} {p} {len(e)} {min_edge} {end} {operations} {solutions} {configurations}\n")
