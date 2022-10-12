# @Author: Pedro Monteiro
# @Email:  pmapm@ua.pt

import json

def get_graph():
    with open('graph3.txt') as f:
        v = json.loads(f.readline())
        e = json.loads(f.readline())
    f.close()

    return v,e

v,e = get_graph()