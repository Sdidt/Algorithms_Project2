from networkx.generators import *
import random
from generate_random_hospitals import gen_random_hospitals


def make_random_graph(testing=False):
    random_graph = gnm_random_graph(10000, 15000)

    # print(random_graph.edges)
    # print(random_graph.nodes)
    m = len(random_graph.edges)
    n = len(random_graph.nodes)
    adj = {}
    for (a, b) in random_graph.edges:
        if a not in adj:
            adj[a] = [[b], False]
        else:
            adj[a][0].append(b)
        # print(adj)
        if b not in adj:
            adj[b] = [[a], False]
        else:
            adj[b][0].append(a)

    hospitals = []
    if not testing:
        nodes = list(adj.keys())
        # print(nodes)
        gen_random_hospitals(nodes)
        f = open("hospitals.txt", 'r')
        for line in f:
            if line[0] == '#':
                h = int(line[1:])
            else:
                hospitals.append(int(line))
        # print(hospitals)
        for hosp in hospitals:
            adj[hosp][1] = True
    return adj, hospitals
