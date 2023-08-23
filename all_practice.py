def rec_sel_sort(seq, i=None):
    if i is None: i = len(seq)-1
    if i == 0: return
    max_index = i
    for j in range(i):
        if seq[j] > seq[max_index]: max_index = j
    seq[i], seq[max_index] = seq[max_index], seq[i]
    rec_sel_sort(seq, i-1)
    return seq

array = [8, 9, 2, 4,0]
print(rec_sel_sort(array))

def ite_sel_sort(seq):
    for i in range(len(seq)-1, 0, -1):
        max_i = i
        for j in range(i):
            if seq[j] > seq[max_i]:
                max_i = j
        seq[i], seq[max_i] = seq[max_i], seq[i]
    return seq
print(ite_sel_sort(array))

def rec_ins_sort(seq, i=None):
    if i is None: i = len(seq)-1
    if i == 0: return
    rec_ins_sort(seq, i-1)
    j = i
    while j > 0 and seq[j-1] > seq[j]:
        seq[j-1], seq[j] = seq[j], seq[j-1]
        j -= 1
    return seq

print(rec_ins_sort(array))

def ite_ins_sort(seq):
    for i in range(1, len(seq)):
        j = i
        while j > 0 and seq[j-1] > seq[j]:
            seq[j-1], seq[j] = seq[j], seq[j-1]
            j -= 1
        return seq
        
def quick_sort(seq):
    if len(seq) < 2: return seq
    else:
        pivot = seq[0]
        left = [i for i in seq[1:] if i <= pivot]
        right = [i for i in seq[1:] if i > pivot]
        return quick_sort(left)+ [pivot]+ quick_sort(right)
    return seq

print(quick_sort(array))

def quicksort(seq):
    pivot = seq[0]
    left = []
    right = []
    for i in range(1, len(seq)):
        left += [i for i in seq[1:] if i <= pivot]
        right += [i for i in seq[1:] if i > pivot]
        
        
def bubblesort(seq):
    for i in range(len(seq)):
        for j in range(i+1, len(seq)):
            if seq[i] > seq[j]:
                seq[i], seq[j] = seq[j], seq[i]
    return seq
    
def rec_bubblesort(seq, i=0):
    if i == len(seq)-1: return seq
    for j in range(0, len(seq)-i-1):
        if seq[j] > seq[j+1]:
            seq[j], seq[j+1] = seq[j+1], seq[j]
    return rec_bubblesort(seq, i+1)

print(rec_bubblesort(array))
print(bubblesort(array))

def celeb_problem(G):
    for u in range(len(G)):
        for v in range(len(G)):
            if u == v: continue
            if G[u][v]: break
            if not G[v][u]: break
        else:
            return u
    return None

# a more refined approach
def celeb(G):
    u = 0
    v = 1
    n = len(G)
    for c in range(2,n+1):
        if G[u][v]: u = c
        if not G[v][u]: v = c
        
    if u == n: v = c
    else: u = c
    for v in range(n):
        if c == v: continue
        if G[c][v]: break
        if not G[v][c]: break
    else:
        return c
    return None

# walking through a component graph
def walk(G, s, S=None):
    P, Q = dict(), set()
    P[s] = None
    Q.add(s)
    while Q:
        u = Q.pop()
        for v in G[u].difference(P,S):
            Q.add(v)
            P[v] = u
        return P
    
# using to find connected graphs
def components(G, s):
    comp = []
    seen = set()
    for u in G[s]:
        if u in seen: continue
        c = walk(G, u)
        seen.update(c)
        comp.append(c)
    return comp

def dfs(G, s):
    P , Q = set(), []
    Q.add(s)
    while Q:
        u = Q.pop()
        for v in G[u]:
            if v in P: continue
            Q.add(p)
            Q.append(G[v])
        yield u
        
def rec_dfs(G, s, Q=None):
    if Q is None: Q = set()
    Q.add(s)
    while Q:
        u = Q.pop()
        for v in G[u]:
            rec_dfs(G, v, Q)
            
# general traversal algorithm
def traverse(G, s, qtype=set):
    P , Q = set(), qtype()
    Q.add(s)
    while Q:
        u = Q.pop()
        if u in P: continue
        P.add(v)
        for v in G[u]:
            Q.add(G[v])
        yield u

def bfs(G, s):
    P , Q = {s: None}, deque[s]
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if v in P: continue
            P[v] = u
            Q.append(v)
        yield u
        
def bfs(G, s):
    P, Q = {s: None}, deque[s]
    while Q:
        u = popleft()
        for v in G[u]:
            if v in P: continue
            P[v] = u
            Q.append(v)
        yield u
        
def bfs(G, s):
    P, Q = {s: None}, deque[s]
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if v in P: continue
            P[v] = u
            Q.append(v)
        yield u
        
def dfs(G, s):
    P , Q = set(), []
    Q.append(s)
    while Q:
        u = Q.pop()
        for v in G[u]:
            if v in P: continue
            P.add(v)
            Q.append(G[v])
        yield u
        
def traverse(G, qtype=set):
    P, Q = set(), qtype()
    Q.add(s)
    while Q:
        u = Q.pop()
        if u in P: continue
        P.add(u)
        for v in G[u]:
            Q.add(G[v])
        yield u
            
        