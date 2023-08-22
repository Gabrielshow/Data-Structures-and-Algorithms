# graph algorithms
# walk through a connnected component of a Graph represented using adjacency sets
def walk(G, s, S=set()):
    P, Q = dict(), set()						# predecessors + "to do" queue
    P[s] = None
    Q.add(s)
    while Q:
        u = Q.pop()
        for v in G[u].difference(P,S):
            Q.add(v)
            P[v] = u						# remember where we came from
    return P								# the traversal tree

# finding connected components
def components(G):
    comp = []
    seen = set()
    for u in G:
        if u in seen: continue
        c = walk(G, u)
        seen.update(c)				#update the keys
        comp.append(c)
    return comp

def naive_celebrity_problem(G, S=None):
    if S is None: S = set(range(len(M)))
    for u in S:
        for v in S:
            if u == v: continue
            if G[u][v]: break
            if not G[v][u]: break
        else:
            return u
    return None

def celeb_problem(G):
    n = len(arr)
    u = 0
    v = 1
    for c in (2, n):
        if G[u][v]: u = c
        else: v = c
    if u == n: c = v
    else: c = u
    for v in range(n):
        if c == v: continue
        if G[c][v]: break
        if not G[v][c]: break
    else:
        return c
    return None
    
# left-hand rule for solving mazes
def tree_walk(T, r):					# Traveerse T from root r
    for u in T[r]:						# For each child
        tree_walk(T, u)					# ...traverse its subtree
        
# Tremaux's algorithm or depth first search
# Recursive Depth-First Search
def rec_dfs(G, s, S=None):
    if S is None: S = set()				# store the history 
    S.add(s)
    for u in G[s]:
        if u in S: continue
        rec_dfs(G, u, S)

# iterative version
def iter_dfs(G, s):
    S, Q = set(), []				#visited set and queue
    Q.append(s)
    while Q:
        u = Q.pop()
        if u in S: continue
        S.add(u)
        Q.extend(G[u])
        yield u
        
        
a,b,c,d,e,f,g,h = range(8)        
N = [
 {b, c, d, e, f}, # a
 {c, e}, # b
 {d}, # c
 {e}, # d
 {f}, # e
 {c, g, h}, # f
 {f, h}, # g
 {f, g} # h
]

print(list(iter_dfs(N,0)))

# general traverse algorithm
# a mature version of walk
def traverse(G, s, qtype=set):
    S, Q = set(), qtype()
    Q.add(s)
    while Q:
        u = Q.pop()
        if u in S: continue
        S.add(u)
        for v in G[u]:
            Q.add(v)
        yield u
        
def walk(G, s, S=None):
    if S is None: S = set()
    P, Q = dict(), set()
    P[s] = None
    Q.add(s)
    while Q:
        u = Q.pop()
        for v in G[u].difference(P,S):
            Q.add(v)
            P[v] = u
    return P

# def components(G):
#     comp = []
#     seen = set()
#     for u in G[u]:
#         if u in seen: continue
#         c = walk(G, u)
#         seen.update(c)
#         comp.append(c)
#     return comp

# the default queue type is Set for the traverse function
# we could easily define a class stack type( with proper add and pop methods of our general queue protocol)
class stack(list):
    add = list.append
    
print(list(traverse(N, 0, stack)))

        
