# naive implementation of Kruskal's Algorithm
def naive_find(C, u):
    while C[u] != u:
        u = C[u]
    return u

def naive_union(C, u, v):
    u = naive_find(C, u)
    v = naive_find(C, v)
    C[u] = v
    
def naive_kruskal(G):
    E = [(G[u][v], u, v) for u in G for v in G[u]]
    T = set()
    C = {u:u for u in G}
    for _, u, v in sorted(E):
        if naive_find(C, u) != naive_find(C, v):
            T.add((u, v))
            naive_union(C, u, v)
    return T

# improvement to the algorithm
# using path compression
def find(C, u):
    if C[u] != u:
        C[u] = find(C, C[u])
    return C[u]

def union(C, R, u, v):
    u, v = find(C, u), find(C, v)
    if R[u] > R[v]:
        C[v] = u
    else:
        C[u] = v
    if R[u] == R[v]:
        R[v] += 1
        
def kruskal(G):
    E = [(G[u][v], u, v) for u in G for v in G[u]]
    T = set()
    C, R = {u:u for u in G}, {u:0 for u in G}
    for _, u, v in sorted(E):
        if find(C, u) != find(C, v):
            T.add((u, v))
            union(C, R, u, v)
    return T

# Prim's algorithm is just another traversal algorithm
# the main difference between traversal algorithms is the ordering of our "to-do-list"
# among the unvisited nodes we've discovered, which one do we grow our traversal tree to next?
# In breadth-first search, we used a simple queue(that is , a deque); in Prim's algorithm,
# we simply replace this queue with a priority queue, implemented with a heap, using the heapq library
# also we would discover new edges pointing to nodes that are already in our queue. if the new edge we discovered was shorter than the previous one, we
# should adjust the priority based on this new edge.
# Prim's algorithm
from heapq import heappop, heappush

def prim(G, s):
    P, Q = {}, [(o, None, s)]
    while Q:
        _, p, u = heappop(Q)
        if u in P: continue
        P[u] = p
        for v, w in G[u].items():
            heappush(Q, (w, u, v))
    return P

# prim function assumes that the graph G is an undirected graph where both directions are explicitly represented, so we can easily traverse each edge in both directions.
# three algorithms that are used in the minimum spanning tree problem
# 1) Add a shortest edge that joins two different fragments
# 2) Add a shortest edge that joins the fragment containing the root to another fragment.
# 3) for every fragment, add the shortest edge that joins it to another fragment.
# 1 is for kruskal, 2 is for prim, and 3 for Boruvka
