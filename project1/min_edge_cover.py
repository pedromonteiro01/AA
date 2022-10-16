# @Author: Pedro Monteiro
# @Email:  pmapm@ua.pt

import json, itertools, time

from matplotlib.pyplot import get
import os


def get_graph(n, p):
    file = 'graph'+str(n)+'-'+str(p)+'.txt'
    if os.path.exists(file):
        with open(file) as f:
            return json.loads(f.readline()), json.loads(f.readline())

def find_solution(v,e):
    start = time.time()
    v_list = {vertex[0] for vertex in v} # set with all vertexes

    for i in range(1, len(v_list)+1):
        for data in itertools.combinations(e, i): # get all subsets of edges
            temp_set = set()
            #print("data: ",list(data))
            for item in data:
                temp_set.update({item[0], item[1]}) # add {'x1', 'x2} to set
                if sorted(v_list) == sorted(temp_set): # only covering edges here!
                    end = (time.time() - start)
                    print("time: ", end)
                    return i
                    
    return None

percentages = [12.5, 25, 50, 75]

for i in range(2,5):
    for p in percentages:
        file = 'graph'+str(i)+'-'+str(p)+'.txt'
        if os.path.exists(file):
            with open(file) as f:
                v,e = json.loads(f.readline()), json.loads(f.readline())
                v,e = get_graph(i,p)
                min_edge = find_solution(v,e)
                print("num_v: ", len(v), "num_edges: ", len(e), "percentage: ", p)
                print("min_edge: ",min_edge)

