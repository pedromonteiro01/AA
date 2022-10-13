# @Author: Pedro Monteiro
# @Email:  pmapm@ua.pt

import json, itertools, time

def get_graph():
    with open('graph-10.txt') as f:
        v = json.loads(f.readline())
        e = json.loads(f.readline())
    f.close()

    return v,e

def find_solution(v,e):
    start = time.time()
    v_list = {vertex[0] for vertex in v} # set with all vertexes
    dic2 = {}

    for i in range(1, len(v_list)+1):
        for data in itertools.combinations(e, i): # get all subsets of edges
            dic = {i: set()}
            #print("data: ",list(data))
            for item in data:
                dic[i].add(item[0])
                dic[i].add(item[1])
                if sorted(v_list) == sorted(dic[i]): # only covering edges here!
                    dic2[i] = dic
                    end = (time.time() - start)
                    print(end)
                    return i

    return None

v,e = get_graph()
print(find_solution(v,e))