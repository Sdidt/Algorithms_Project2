import time


def bfs_optimized(adj, s, prev, curr_min, i):
    dist = {x:len(adj) + 1 for x in adj.keys()}
    dist[s] = 0
    q = [s]
    curr_min[s] = [0, i]
    while len(q) != 0:
        u = q[0]
        q.pop(0)
        for v in adj[u][0]:
            if dist[v] == (len(adj) + 1) and (dist[u] + 1) < (curr_min[v][0]):
                q.append(v)
                dist[v] = dist[u] + 1
                prev[v] = u
                curr_min[v] = [dist[v], i]
                # print(curr_min)
    return dist, prev, curr_min


def run_through_hospitals(adj, hospitals):
    curr_min = {x: [len(adj) + 2, -1] for x in adj.keys()}
    prevs = []
    # print(hospitals)
    start = time.time()
    for i, hosp in enumerate(hospitals):
        prev = {x: -1 for x in adj.keys()}
        ans, prev, curr_min = bfs_optimized(adj, hosp, prev, curr_min, i)
        # print(ans)
        prevs.append(prev)
    return curr_min, prevs, start
