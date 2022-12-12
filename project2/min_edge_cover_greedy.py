# @Author: Pedro Monteiro
# @Email:  pmapm@ua.pt


import json, itertools, time

from matplotlib.pyplot import get
import os
from utils import get_adjacency_list

def get_new_graph():
    file = 'SWtinyG.txt'
    edges = []
    vertices = set()
    if os.path.exists(file):
        with open(file) as f:
            for line in f:
                line = line.strip().split(" ")
                edges.append([line[0], line[1]])
                vertices.update({line[0], line[1]})

    return list(vertices), edges

def check_isolated_graph(v,e):
    graph_vertices = {vertex[0] for vertex in v}
    vertices_in_edges = {}
    for element in e:
        vertices_in_edges.update({element[0], element[1]})
    
    if len(graph_vertices) == len(vertices_in_edges):
        return True

    return False

def get_vertex_with_less_edges(adj_list, lst):
    vertex_dic = {} # {vertex: number_of_neighbours}
    for v in lst:
        vertex_dic[v] = len(adj_list[v])

    ordered_vertex_dic = dict(sorted(vertex_dic.items(), key=lambda item: item[1]))

    if list(ordered_vertex_dic.keys()):
        return list(ordered_vertex_dic.keys())[0]
    
    return None


def find_solution(v,e):
    associated_vertices = set()
    iterations = 0
    if not check_isolated_graph:
        return None
    
    adj_list = get_adjacency_list(e)

    # get ordered vertexes with less edges
    sort_vertex_by_num_edges = dict(sorted(adj_list.items(), key=lambda item: len(item[1])))

    min_edge = 0 
    for vertex in sort_vertex_by_num_edges.keys():
        iterations += 1
        if vertex not in associated_vertices:
            min_edge += 1
            min_vertex = get_vertex_with_less_edges(adj_list, sort_vertex_by_num_edges[vertex])
            iterations+=len(sort_vertex_by_num_edges[vertex])

            while min_vertex in associated_vertices:
                iterations += 1
                adj_list2 = adj_list.copy()
                if min_vertex in adj_list2[vertex]:
                    adj_list2[vertex].remove(min_vertex)
                else:
                    break
                
                min_vertex = get_vertex_with_less_edges(adj_list2, sort_vertex_by_num_edges[vertex]) 
                iterations+=len(sort_vertex_by_num_edges[vertex])
            
            associated_vertices.update({vertex,min_vertex})

        if len(associated_vertices) == len(v):
            break
    
    return min_edge, iterations



v,e = get_new_graph()
start = time.time()
min_edge, iterations = find_solution(v,e)
end = (time.time() - start)

print(f"vertices: {len(v)} edges: {len(e)} minedge: {min_edge} time: {end} operations: {iterations}\n")