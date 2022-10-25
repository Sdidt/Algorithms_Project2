import math
import sys
import time


def bfs_optimized_write_to_file(curr_min, prevs, hospitals, adj, start):
    f = open("output7.txt", 'w')
    original_stdout = sys.stdout
    sys.stdout = f
    print("The hospitals in this graph: ")
    for h in hospitals:
        print(h + 1)
    count = 0
    for i, (dist, hosp_i) in curr_min.items():
        sys.stdout = original_stdout
        # print((count + 1))
        sys.stdout = f
        print("---- Node " + str(i + 1) + " ----")
        if dist == (len(adj) + 2):
            print("This node cannot reach any hospital")
            continue
        print("Nearest Hospital: " + str(hospitals[hosp_i] + 1))
        print("Nearest Hospital Distance : " + str(dist))
        path = [i + 1]
        curr_node = i
        # print(prevs[hosp_i])
        while prevs[hosp_i][curr_node] != -1:
            path.append(prevs[hosp_i][curr_node] + 1)
            curr_node = prevs[hosp_i][curr_node]
        print("Shortest Path: ")
        for i in range(len(path)):
            print(path[i], end='')
            if i != (len(path) - 1):
                print(" --> ", end='')
        print()
        count += 1
    end = time.time()
    print("Time taken = " + str(end - start))
    sys.stdout = original_stdout


def bfs_hosp_wise_write_to_file(dist, prev, adj, hospitals, start):
    f = open("output7.txt", 'w')
    original_stdout = sys.stdout
    sys.stdout = f
    print("The hospitals in this graph: ")
    for h in hospitals:
        print((h + 1))
    count = 0
    for node, (min_dist, closest_hosp) in dist.items():
        sys.stdout = original_stdout
        # print((count + 1))
        sys.stdout = f
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
        count += 1
    end = time.time()
    print("Time taken = " + str(end - start))
    sys.stdout = original_stdout


def bfs_top_k_write_to_file(distanceFromEachNode, k, start, hospitals):
    f = open("output7.txt", 'w')
    original_stdout = sys.stdout
    sys.stdout = f
    print("The hospitals in this graph: ")
    for h in hospitals:
        print((h + 1))
    count = 0
    for node, lst in distanceFromEachNode.items():
        sys.stdout = original_stdout
        # print((count + 1))
        sys.stdout = f
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
        count += 1
    end = time.time()
    print("Time taken = " + str(end - start))
    sys.stdout = original_stdout
