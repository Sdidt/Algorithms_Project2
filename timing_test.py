import math
import random
import time

from bfs import bfs_optimized
from bfs_hospital_wise import bfs_hospital_wise
from bfs_top_k import compute_top_k
from random_graph import make_random_graph


def timing_test_bfs_optimized():
    times = {}
    adj, hospitals = make_random_graph(True)
    nodes = list(adj.keys())
    random_h = random.sample(nodes, 1)[0]
    for h in range(1, 151):
        while adj[random_h][1]:
            random_h = random.sample(nodes, 1)[0]
        adj[random_h][1] = True
        hospitals.append(random_h)
        # print(adj)
        curr_min = {x: [len(adj) + 2, -1] for x in adj.keys()}
        prevs = []
        # print(hospitals)
        start = time.time()
        for i, hosp in enumerate(hospitals):
            prev = {x: -1 for x in adj.keys()}
            ans, prev, curr_min = bfs_optimized(adj, hosp, prev, curr_min, i)
            # print(ans)
            prevs.append(prev)

        # print(prevs)
        # print(curr_min)
        for i, (dist, hosp_i) in curr_min.items():
            print("---- Node " + str(i + 1) + " ----")
            if dist == (len(adj) + 2):
                print("This node cannot reach any hospital")
                continue
            print("Nearest Hospital: " + str(hospitals[hosp_i]))
            print("Nearest Hospital Distance : " + str(dist))
            path = [i + 1]
            curr_node = i
            # print(prevs[hosp_i])
            while prevs[hosp_i][curr_node] != -1:
                path.append(prevs[hosp_i][curr_node] + 1)
                curr_node = prevs[hosp_i][curr_node]
            print("Shortest Path: ")
            for j in range(len(path)):
                print(path[j], end='')
                if j != (len(path) - 1):
                    print(" --> ", end='')
            print()
        end = time.time()
        times[h] = (end - start)
    print("Number of Hospitals\t Time taken")
    for h, t in times.items():
        print(h, "\t", t)


def timing_test_bfs_hosp_wise():
    times = {}
    adj, hospitals = make_random_graph(True)
    # print(adj)
    nodes = list(adj.keys())
    random_h = random.sample(nodes, 1)[0]
    for h in range(1, 151):
        while adj[random_h][1]:
            random_h = random.sample(nodes, 1)[0]
        adj[random_h][1] = True
        hospitals.append(random_h)
        start = time.time()
        dist, prev = bfs_hospital_wise(adj, hospitals)
        for node, (min_dist, closest_hosp) in dist.items():
            print("---- Node " + str(node + 1) + " ----")
            if min_dist == (len(adj) + 1):
                print("This node cannot reach any hospital")
                continue
            if min_dist == 0:
                print("This node is already a hospital")
                continue
            print("Nearest Hospital: " + str(closest_hosp + 1))
            print("Nearest Hospital Distance : " + str(min_dist))
            path = [node + 1]
            curr_node = node
            # print(prevs[hosp_i])
            while prev[closest_hosp][curr_node] != -1:
                path.append(prev[closest_hosp][curr_node] + 1)
                curr_node = prev[closest_hosp][curr_node]
            print("Shortest Path: ")
            for i in range(len(path)):
                print(path[i], end='')
                if i != (len(path) - 1):
                    print(" --> ", end='')
            print()
        end = time.time()
        times[h] = (end - start)
    print("Number of Hospitals\t Time taken")
    for h, t in times.items():
        print(h, "\t", t)


def timing_test_bfs_top_k():
    times = {}
    adj, hospitals = make_random_graph(True)
    # print(adj)
    nodes = list(adj.keys())
    random_h = random.sample(nodes, 1)[0]
    k = int(input("Enter the value of k:"))
    for h in range(1, 151):
        while adj[random_h][1]:
            random_h = random.sample(nodes, 1)[0]
        adj[random_h][1] = True
        hospitals.append(random_h)
        start = time.time()
        distanceFromEachNode, k, hospitals = compute_top_k(adj, hospitals, k)
        for node, lst in distanceFromEachNode.items():
            print("---- Node " + str(node + 1) + " ----")
            if lst[0][0] == 0:
                print("This node is already a hospital!")
                print(str(k - 1) + " nearest hospitals and distances:")
            elif math.isinf(lst[0][0]):
                print("This node cannot reach any hospital!")
            else:
                print(str(k) + " nearest hospitals and distances:")
            for dist, closest_hosp in lst:
                if dist == 0:
                    continue
                print(str(closest_hosp + 1) + " : " + str(dist))
        end = time.time()
        times[h] = (end - start)
    print("Number of Hospitals\t Time taken")
    for h, t in times.items():
        print(h, "\t", t)
