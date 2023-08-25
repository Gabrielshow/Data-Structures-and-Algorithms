# another new day of practice
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

def rec_ins_sort_while(seq, i=None):
    if i is None: i = len(seq)-1
    if i == 0: return
    rec_ins_sort_while(seq, i-1)
    j = i
    while j > 0 and seq[j-1] > seq[j]:
        seq[j-1], seq[j] = seq[j], seq[j-1]
        j -= 1
    return seq

def rec_ins_sort_for(seq, i=None):
    if i is None: i = len(seq)-1
    if i == 0: return
    rec_ins_sort_for(seq, i-1)
    j = i
    for j in range(i):
        if j == 0 or seq[j-1] < seq[j]:
            j += 1
        else:
            seq[j-1], seq[j] = seq[j] , seq[j-1]
            j -= 1
    return  seq

def ite_ins_sort(seq):
    for i in range(len(seq)):
        j = i
        while j > 0 and seq[j-1] > seq[j]:
            seq[j-1], seq[j] = seq[j], seq[j-1]
            j -= 1
    return seq

def sel_sort_for(seq, i=None):
    if i is None: i = len(seq)-1
    if i == 0: return
    max_i = i
    for j in range(i):
        if seq[j] > seq[max_i]: max_i = j
    seq[i], seq[max_i] = seq[max_i], seq[i]
    sel_sort_for(seq, i-1)
    return seq

def ite_sel_sort(seq):
    for i in range(len(seq)-1,0,-1):
        max_i = i
        for j in range(i):
            if seq[j] > seq[max_i]: max_i = j
        seq[i], seq[max_i] = seq[max_i], seq[i]
    return seq

def quicksort_rec(seq):
    if len(seq) < 2: return seq
    else:
        pivot = seq[0]
        less = [i for i in seq[1:] if i <= pivot]
        greater = [i for i in seq[1:] if i > pivot]
        return quicksort_rec(less) + [pivot] + quicksort_rec(greater)
    return seq

def mergesort(seq):
    if len(seq) == 1: return seq
    else:
        mid = seq[len(seq)//2]
        low = mergesort(seq[:mid])
        upp = mergesort(seq[mid+1:])
        res = []
        while low and upp:
            if low[-1] > upp[-1]:
                res.append(low.pop())
            else:
                res.append(upp.pop())
        res.reverse()
        return res
        
                
array = [8, 0, 8, 5,7,9,1,2,7]
print(quicksort_rec(array))
print(mergesort(array))

def mergesort_retry(seq):
    mid = len(seq)//2
    lft, rgt = seq[:mid], seq[mid+1:]
    if len(lft) > 1: lft = mergesort_retry(lft)
    if len(rgt) > 1: rgt = mergesort_retry(rgt)
    res = []
    while lft and rgt:
        if lft[-1] >= rgt[-1]:
            res.append(lft.pop())
        else:
            res.append(rgt.pop())
    res.reverse()
    return (lft or rgt) + res

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

def component_graph(G, s, Q=set()):
    comp = []
    seen = set()
    Q.add(s)
    while Q:
        u = Q.pop()
        for v in G[u]:
            if v in seen: continue
            c = walk(G, v)
            seen.update(c)
            comp.append(c)
    return comp

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
        
def bfs(G, s):
    P, S = {s: None}, deque([s])
    S.add(s)
    while S:
        u = S.popleft()
        for v in G[u]:
            if v in P: continue
            P[v] = u
            S.append(s)
        yield u
        
def top_sort(G, S=None):
    if S is None: S = set(G)
    if len(S) == 1: return list(S)
    v = S.pop()
    arr = top_sort(G, S)
    min_i = 0
    for i, u in enumerate(arr):
        if v in G[u]: min_i += 1
    arr.insert(min_i, v)
    return arr

def iddfs(G, s):
    seen = set()
    n = len(G)
    def recurse(G, s, d, S=None):
        if s not in seen: yield s
        seen.add(s)
        if d == 0: return
        if S is None: S = set()
        S.add(s)
        for u in G[s]:
            if u in S: continue
            for v in recurese(G, u, d-1, S):
                yield v
    for d in range(n):
        if len(seen) == n: break
        for u in recurse(G, s, d):
            yield u
            
class Node:
    rgt = None
    lft = None
    def __init__(self, key, value):
        self.key = key
        self.value = value
        
def insert(node, key, value):
    if node is None: node(key, value)
    if node.key == key: node.value = value
    elif: node.key < key: node.lft = insert(node.lft, key, value)
    else: node.rgt = insert(node.rgt, key, value)
    
def search(node, key):
    if node is None: raise KeyError
    if node.key == key: return node.value
    elif node.key < key: return search(node.lft, key)
    else: return search(node.rgt, key)
    return node

class Tree:
    root = None
    def __setitem__(self,key,value):
        self.root = insert(self.root,key,value)
    def __getitem__(self,key):
        return search(self.root, key)
    def __contains__(self,key):
        try: search(self.root, key)
        except KeyError: return False
        return True