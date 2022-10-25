import time

from bfs import run_through_hospitals
from bfs_hospital_wise import bfs_hospital_wise
from parse_from_file import parse_from_file
from output_paths_to_file import *
from bfs_top_k import *
from timing_test import *


def input_graph():
    n = int(input("Nodes:"))
    m = int(input("Edges:"))
    data = list(map(int, input().split()))
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = {}
    for (a, b) in edges:
        if (a - 1) not in adj:
            adj[a - 1] = [[b - 1], False]
        else:
            adj[a - 1][0].append(b - 1)
        # print(adj)
        if (b - 1) not in adj:
            adj[b - 1] = [[a - 1], False]
        else:
            adj[b - 1][0].append(a - 1)
    num_h = int(input("Hospitals:"))
    hospitals = list(map(int, input().split()))
    hospitals = [(h - 1) for h in hospitals]
    for h in hospitals:
        adj[h][1] = True
    # print(adj)
    return adj, hospitals


def run_bfs_optimized(choice):
    if choice == 1:
        adj, hospitals = input_graph()
    if choice == 2:
        adj, hospitals = make_random_graph()
    if choice == 3:
        adj, hospitals = parse_from_file()
    curr_min, prevs, start = run_through_hospitals(adj, hospitals)
    bfs_optimized_write_to_file(curr_min, prevs, hospitals, adj, start)


def run_bfs_hospital_wise(choice):
    if choice == 1:
        adj, hospitals = input_graph()
    if choice == 2:
        adj, hospitals = make_random_graph()
    if choice == 3:
        adj, hospitals = parse_from_file()
    # print(adj)
    start = time.time()
    dist, prev = bfs_hospital_wise(adj, hospitals)
    # print(dist, prev)
    bfs_hosp_wise_write_to_file(dist, prev, adj, hospitals, start)


def run_bfs_top_k(choice, k=-1):
    if choice == 1:
        adj, hospitals = input_graph()
    if choice == 2:
        adj, hospitals = make_random_graph()
    if choice == 3:
        adj, hospitals = parse_from_file()
    # print(len(hospitals))
    # print(adj)
    if k == -1:
        k = int(input("Enter the value of k (less than " + str(len(hospitals)) + "):"))
        if k > len(hospitals):
            print("Please enter a value of k less than the number of hospitals.")
            return
    start = time.time()
    distanceFromEachNode, k, hospitals = compute_top_k(adj, hospitals, k)
    bfs_top_k_write_to_file(distanceFromEachNode, k, start, hospitals)


while True:
    print("Enter your choice according to the following menu:")
    print("1. Input graph manually")
    print("2. Test on random graph.")
    print("3. Test on real road network")
    print("4. Exit")
    choice = int(input())
    if choice == 4:
        exit()
    if choice not in [1, 2, 3, 4]:
        print("Please enter a correct option.")
        continue
    print("1. Find nearest hospitals and paths.")
    print("2. Find nearest hospitals and paths. (independent of h)")
    print("3. Find top-2 nearest hospitals.")
    print("4. Find top-k nearest hospitals.")
    print("5. Exit")

    choice1 = int(input())
    if choice1 == 1:
        run_bfs_optimized(choice)
    elif choice1 == 2:
        run_bfs_hospital_wise(choice)
    elif choice1 == 3:
        run_bfs_top_k(choice, 2)
    elif choice1 == 4:
        run_bfs_top_k(choice)
    elif choice1 == 5:
        exit()
    else:
        print("Please enter a correct input.")
