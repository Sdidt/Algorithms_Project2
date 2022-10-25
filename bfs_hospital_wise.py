def bfs_hospital_wise(adj, hospitals):
    dist = {x: [len(adj) + 1, -1] for x in adj.keys()}
    visited = {v: False for v in adj.keys()}
    prev = {h: {x: -1 for x in adj.keys()} for h in hospitals}
    q = [[h, h] for h in hospitals]
    for h in hospitals:
        visited[h] = True
        dist[h] = [0, h]
    # print(dist)
    while len(q) != 0:
        u, curr_h = q[0]
        q.pop(0)
        for v in adj[u][0]:
            # print(dist)
            if dist[v][0] == (len(adj) + 1) and not visited[v]:
                visited[v] = True
                q.append([v, curr_h])
                dist[v] = [dist[u][0] + 1, curr_h]
                prev[curr_h][v] = u
    return dist, prev
