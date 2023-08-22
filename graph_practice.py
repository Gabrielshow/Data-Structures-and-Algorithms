# connected graph
def walk(G, s, S=set()):
    P, Q = dict(), set()
    P[s] = None
    Q.add(s)
    while Q:
        u = Q.pop()
        for v in G[u].difference(P,S):
            Q.add(v)
            P[v] = u
    return P

def components(G):
    comp = []
    seen = set()
    for u in G[u]:
        if u in seen: continue
        c = walk(G, u)
        seen.update(c)
        comp.append(c)
    return comp

def Tree_walk(T, r):
    for u in T[r]:
        Tree_walk(T, u)

# recursive depth first
def rec_dfs(G, s, S=None):
    if S is None: S = set()
    S.add(s)
    for u in G[s]:
        if u in S: continue
        rec_dfs(G, u, S)
        

def ite_dfs(G, s, P=None):
    P, Q = set(), []
    Q.append(s)
    while Q:
        u = Q.pop()
        if u in P: continue
        P.add(u)
        Q.extend(G[u])
        yield u
        
def ite_dfs(G, s, P=None):
    P, Q = set(), []
    Q.append(s)
    while Q:
        u = Q.pop()
        if u in P: continue
        P.add(u)
        Q.extend(G[u])
        yield u

def rec_dfs(G, s, Q=None):
    if Q is None: Q = set()
    Q.add(s)
    for u in G[s]:
        if u in Q: continue
        rec_dfs(G, u, Q)

def rec_dfs(G, s, S=None):
    if S is None: S = set()
    S.add(s)
    for u in G[s]:
        if u in S: continue
        rec_dfs(G, u, S)
        
def ite_dfs(G):
    P, Q = set(), []
    Q.append(s)
    while Q:
        u = Q.pop()
        if u in P: continue
        P.add(u)
        Q.extend(G[u])
        yield u
        
        
def walk(G, s, S=None):
    if S is None: S = set()
    P, Q = dict(), set()
    P[s] = None
    Q.add(s)
    while Q:
        u = Q.pop()
        for v in G[u].difference(P,S)
            Q.add(v)
            P[v] = u
    return P

def components(G):
    comp = []
    Q = set()
    for u in G[u]:
        if u in Q: continue
        c = walk(G, u)
        Q.update(c)
        comp.append(u)
    return comp

# general traversal algorithm
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
    if S is None: S=set()
    P, Q = dict(), set()
    P[s] = None
    Q.add(s)
    while Q:
        u = Q.pop()
        for v in G[u].difference(P,S):
            Q.add(v)
            P[v] = u
    return P

# breadth-First Search
def bfs(G, s):
    P, Q = {s: None}, deque([s])
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if v in P: continue
            P[v] = u
            Q.append(v)
    return P
        
            
    
    