import random
from generate_random_hospitals import gen_random_hospitals


def parse_from_file():
    file = open('roadNet-PA.txt', 'r')
    file.readline()
    file.readline()
    node_edge_line = file.readline().split()
    n, m = list(map(int, [node_edge_line[2], node_edge_line[4]]))
    # print(n, m)
    file.readline()
    adj = {}
    for i in range(m):
        a, b = list(map(int, file.readline().split()))
        # print(a, b)
        if a not in adj:
            adj[a] = [[b], False]
        else:
            adj[a][0].append(b)
    nodes = [node for node in adj.keys()]
    gen_random_hospitals(nodes)
    f = open("hospitals.txt", 'r')
    hospitals = []
    for line in f:
        # print(line)
        if line[0] == '#':
            h = int(line[1:])
        else:
            hospitals.append(int(line))
    # print(hospitals)
    for hosp in hospitals:
        adj[hosp][1] = True
    return adj, hospitals
