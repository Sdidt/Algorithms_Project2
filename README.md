# CX2001 Project 2 Source Code

This repository contains the source code for the task of finding the shortest paths from every node in a graph to any of a set of special nodes in the graph known as hospitals.

Packages required: networkx

The above package can be installed using "pip install networkx" in a standard shell.

Run main.py and choose any of the options to test out the algorithms. If you would like to test on a real road network, download the txt file dataset from https://snap.stanford.edu/data/roadNet-PA.html.

For the first 2 algorithms (to output the closest hospitals and the paths), the output format is as follows:

"""

The hospitals in this graph:

_List of hospitals_

.

.

.

---- Node X ----

Nearest Hospital: Y

Nearest Hospital Distance : dist

Shortest Path: _actual shortest path_

OR

This node is already a hospital!

OR

This node cannot reach any hospital
.
.
.
.
.
Time taken = value

"""

For the last 2 algorithms (to output the top-2 or top-k closest hospitals), the output format is as follows:

"""

The hospitals in this graph:

_List of hospitals_

.

.

.

---- Node X ----

k nearest hospitals and distances:

Y1: dist1

Y2: dist2

...

Yk: distk

OR

This node is already a hospital!

(k - 1) nearest hospitals and distances:

Y1: dist1

Y2: dist2

...

Y(k-1): dist(k - 1)

OR

This node cannot reach any hospital!

.

.

.

.

.

Time taken = value

"""
