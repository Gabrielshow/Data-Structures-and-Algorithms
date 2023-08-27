# revision
def bfs(G, s):
    P, Q = {s: None}, deque[(s)]
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if v in P: continue
            P[v] = u
            Q.append(v)
    return P
            
def dfs_rec(G, s, S=None):
    if S is None: S = set()
    S.add(s)
    for u in G[s]:
        if u in S: continue
        rec_dfs(G,u, S)
        
        
def bfs(G, s):
    P, Q = {s: None}, deque[(s)]
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if v in P: continue
            P[v] = u
            Q.append(u)
    return P

def rec_dfs(G, s, S=None):
    if S is None: S = set()
    S.add(s)
    for u in G[s]:
        if u in S: continue
        rec_dfs(G, u, S)
        
def ite_dfs(G, s, S=None):
    P , Q = set(), []
    Q.append(s)
    while Q:
        u = Q.pop()
        if u in P: continue
        P.add(u)
        Q.extend(G[v])
        yield u
def walk(G, s, S=None):
    P, Q = dict(), set()
    P[s] = None
    Q.add(s)
    while Q:
        u = Q.pop()
        for v in G[u].difference(P, S):						# if equivalent to the check if v in P: continue
            Q.add(v)
            P[v] = u      
    return P

def components(G):
    comp = []
    seen = set()
    for u in G:
        if u in seen: continue
        c = walk(G, v, Q)
        seen.update(c)
        comp.append(c)
    return comp

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

def comp(G):
    comp = []
    seen = set()
    for u in G:
        if u in seen: continue
        c = walk(G, u)
        seen.updating(c)
        comp.append(c)
    return comp

def bfs(G, s):
    P, Q = {s: None}, deque[(s)]
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if v in P: continue
            P[v] = u
            Q.append(v)
    return P

def traverse(G, s, qtype=set):
    P, Q = set(), qtype()
    Q.add(s)
    while Q:
        u = Q.pop()
        if u in P: continue
        P.add(u)
        for v in G[u]:
            Q.add(v)
            yield u

def walk(G, s, S=None):
    P, Q = dict(), set()
    P[s] = None
    Q.add(s)
    while Q:
        u = Q.pop()
        for v in G[u].difference(P, S):
            Q.add(v)
            P[v] = u
    return P

def components(G):
    comp = []
    seen = set()
    for u in G:
        if u in seen: continue
        c = walk(G, v)
        seen.update(c)
        comp.append(c)
    return comp

def dfs_rec(G, s, S=None):
    if S is None: S = set()
    S.add(s)
    for u in G[s]:
        if u in S: continue
        dfs_rec(G, u, S)
        
def dfs_ite(G, s):
    P, Q = set(), []
    Q.append(s)
    while Q:
        u = Q.pop()
        if u in P: continue
        P.add(v)
        Q.extend(G[v])
        yield u
        
def walk(G, s, S=None):
    P, Q = {s: None}, set()
    Q.add(s)
    while Q:
        u = Q.pop()
        for v in G[u].difference(P, S):
            if v in P: continue
            Q.add(v)
            P[v] = u
    return P

def components(G):
    comp = []
    seen = set()
    for u in G:
        if u in seen: continue
        c = walk(G, u)
        seen.update(c)
        comp.append(c)
    return comp

def bfs(G, s):
    P, Q = {s: None}, deque[(s)]
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if v in P: continue
            P[v] = u
            Q.append(u)
    return P

def traverse(G, s):
    P, Q = set(), set()
    Q.add(s)
    while Q:
        u = Q.pop()
        if u in P: continue
        P.add(u)
        for v in G[u]:
            Q.add(v)
        yield u
        
# dfs with timestamps
def dfs(G, s, d, f, S=None, t=0):
    if S is None: S = set()
    d[s] = t; t += 1
    S.add(s)
    for v in G[u]:
        if u in S: continue
        t = dfs(G, v, d, f, S, t)
    f[t] = t; t += 1
    return t

def dfs_rec(G, s, S=None):
    if S is None: S = set()
    S.add(s)
    for u in G:
        if u in S: continue
        dfs_rec(G, u, S)
        
def dfs_ite(G, s):
    P, Q = set(), []
    Q.append(s)
    while Q:
        u = Q.pop()
        if u in P: continue
        P.add(u)
        Q.extend(G[u])
        yield u
        
def dfs(G, s, d, f, S=None, t=0):
    if S is None: S = set()
    d[s] = t; t += 1
    S.add(s)
    for u in G[s]:
        if u in S: continue
        t = dfs(G, s, u, f, S, t)
    f[t] = t; t += 1
    return t

def dfs_rec(G, s):
    Q = set()
    Q.add(s)
    for u in G:
        if u in Q: continue
        dfs_rec(G, u)

def dfs_ite(G, s):
    P, Q = set(), []
    Q.append(s)
    while Q:
        u = Q.pop()
        if u in P: continue
        P.add(u)
        Q.extend(G[u])
        yield u
        
def dft_top_sort(G, s):
    seen, res = set(), []
    def recurse(u):
        if u in seen: return
        seen.add(u)
        for v in G[u]:
            recurse(v)
        res.append(u)
    for u in G:
        recurse(u)
    res.reverse()
    return res

def bfs(G, s):
    P, Q = {s:None}, deque([s])
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if v in P: continue
            P[v] = u
            Q.append(v)
    return P

def iddfs(G, s):
    seen = set()
    n = len(G)
    def recurse(G, u, d, S=None):
        if u not in seen: yield u
        seen.add(u)
        if d == 0: return
        if S is None: S = set()
        S.add(u)
        for v in G[u]:
            if v in S: continue
            for z in recurse(G, u, d-1, S):
                yield z
    for d in range(n):
        if len(seen) == n: continue
        for u in recurse(G, u, d):
            yield u

def dfs_topsort(G, s):
    seen , res = set(), []
    def recurse(s):
        if s in Seen: return
        seen.add(s)
        for u in G[s]:
            recurse(u)
        res.append(u)
    for u in G:
        recurse(u)
    res.reverse
    return res

def naive_top_sort(G, S=None):
    if S is None: S = set(G)
    if len(S) == 1: return list(S)
    v = S.pop()
    arr = naive_top_sort(G, S)
    min_index = 0
    for i, u in enumerate(arr):
        if v in G[u]: min_index += 1
    arr.insert(min_index, v)
    return arr

def top_sort(G):
    count = dict((u, 0) for u in G)
    for u in G:
        for v in G[u]:
            count[v] += 1
    Q = [ u for u in G if count[v] == 0]
    res = []
    while Q:
        u = Q.pop()
        res.append(u)
        for v in G[u]:
            count[v] -= 1
            if count[v] == 0:
                res.append(v)
    return res

def naive_top_sort(G, S=None):
    if S is None: S = set(G)
    if len(S) == 1: return list(S)
    v = S.pop()
    seq = naive_top_sort(G, S)
    min_i = 0
    for i, u in enumerate(seq):
        if v in G[u]: min_i += 1
    seq.insert(min_i, v)
    return seq

def top_sort(G):
    count = dict((u, 0) for u in G)
    for u in G:
        for v in G[u]:
            count[v] += 1
    Q = [u for u in G if count[u] == 0]
    res = []
    while Q:
        u = Q.pop()
        res.append(u)
        for v in G[u]:
            count[v] -= 1
            if count[v] == 0:
                res.append(v)
    return res

def celeb(G):
    n = len(G)
    for u in range(n):
        for v in range(n):
             if u == v: continue
             if G[u][v]: break
             if not G[v][u]: break
        else:
            return u
    return None

def celeb_optimised(G):
    u = 0
    v = 1
    n = len(G)
    for c in range(2,n):
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


def gnomesort_for(seq):
    for i in range(len(seq)):
        for j in range(len(seq)):
            if j == 0 or seq[i] < seq[j]:
                j += 1
            else:
                seq[i], seq[j] = seq[j], seq[i]
                j -= 1
    return seq

def gnomesort_while(seq):
    i = 0
    while i < len(seq):
        if i == 0 or seq[i-1] < seq[i]:
            i += 1
        else:
            seq[i-1], seq[i] = seq[i], seq[i-1]
            i -= 1
    return seq

def rec_ins_for(seq, i=None):
    if i is None: i = len(seq)-1
    if i == 0: return
    rec_ins_for(seq, i-1)
    j = i
    for j in range(i):
        if j == 0 or seq[j-1] < seq[j]:
            j += 1
        else:
            seq[j-1], seq[j] = seq[j], seq[j-1]
            j -= 1
    return seq

def rec_ins_while(seq, i=None):
    if i is None: i = len(seq)-1
    if i == 0: return
    rec_ins_for(seq, i-1)
    j = i
    while j > 0 and seq[j-1] > seq[j]:
        seq[j-1], seq[j] = seq[j], seq[j-1]
        j -= 1
    return seq

def ins_ite(seq):
    for i in range(len(seq)):
        j = i
        while j > 0 and seq[j-1] > seq[j]:
            seq[j-1], seq[j] = seq[j], seq[j-1]
            j -= 1
    return seq

def sel_sort_rec(seq, i=None):
    if i is None: i = len(seq)-1
    if i == 0: return
    max_i = i
    for j in  range(i):
        if seq[j] > seq[max_i]: max_i = j
    seq[i], seq[max_i] = seq[max_i], seq[i]
    sel_sort_for(seq, i-1)
    return seq

def sel_sort_ite(seq):
    for i in range(len(seq)-1, 0, -1):
        max_i = i
        for j in range(i):
            if seq[j] > seq[max_i]: max_i = j
        seq[i], seq[max_i] = seq[max_i], seq[i]
    return seq

array = [9, 8, 6, 4, 3, 1]
print(sel_sort_ite(array))

def quicksort(seq):
    if len(seq) < 2: return seq
    else:
        pivot = seq[0]
        left = [u for u in seq[1:] if u <= pivot]
        greater = [u for u in seq[1:] if u > pivot]
        return quicksort(left) + [pivot] + quicksort(greater)
    return seq
print(quicksort(array))

        
    