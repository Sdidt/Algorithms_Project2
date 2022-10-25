import math


def bfs(adj, s, prev):
    dist = {x: len(adj) + 1 for x in adj.keys()}
    dist[s] = 0
    q = [s]
    while len(q) != 0:
        u = q[0]
        q.pop(0)
        for v in adj[u][0]:
            if dist[v] == (len(adj) + 1):
                q.append(v)
                dist[v] = dist[u] + 1
                prev[v] = u
    return dist


def compute_top_k(adj, hospitals, k):
    distanceFromEachHospital = {h: {} for h in hospitals}
    for h in hospitals:
        prev = {x: float('inf') for x in adj.keys()}
        # print("--- Node " + str(node) + " ---")
        # print(h)
        distance = bfs(adj, h, prev)
        distanceFromEachHospital[h] = distance
    # print(distanceFromEachHospital)
    distanceFromEachNode = {x: [] for x in adj.keys()}
    for hosp, array in distanceFromEachHospital.items():
        for node, val in array.items():
            distanceFromEachNode[node].append([val, hosp])
    # print(distanceFromEachNode)
    for node in distanceFromEachNode.keys():
        distanceFromEachNode[node] = sorted(distanceFromEachNode[node], key=lambda tup: tup[0])[:k]
    return distanceFromEachNode, k, hospitals
