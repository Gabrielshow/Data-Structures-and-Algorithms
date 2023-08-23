def gnomesort(seq):
    for i in range(len(seq)):
        for j in range(len(seq)):
            if j == 0 or seq[j-1] < seq[j]:
                j += 1
            else:
                seq[j-1], seq[j] = seq[j], seq[j-1]
                j -= 1
    return seq

# also possible
def gnome1(seq):
    i = 0
    while i < len(seq):
        if i == 0 or seq[i-1] < seq[i]:
            i += 1
        else:
            seq[i-1], seq[i] = seq[i], seq[i-1]
            i -= 1
    return seq

array = [5,6,7,2,1,0]
print(gnomesort(array))
print(gnome1(array))

def gnomesort(seq):
    for i in range(len(seq)):
        for j in range(len(seq)):
            if j == 0 or seq[j-1] < seq[j]:
                j += 1
            else:
                seq[j-1], seq[j] = seq[j], seq[j-1]
    return seq

def gnomesort(seq):
    i = 0
    while i < len(seq):
        if i == 0 or seq[i-1] < seq[i]:
            i += 1
        else:
            seq[i-1], seq[i] = seq[i], seq[i-1]
            i -= 1
    return seq

def ins_sort_rec_while(seq, i=None):
    if i is None: i = len(seq)-1
    if i == 0: return
    ins_sort_rec(seq, i-1)
    j = i
    while j > 0 and seq[j-1]>seq[j]:
        seq[j-1], seq[j] = seq[j], seq[j-1]
        j -= 1
    return seq

def ins_sort_rec_for(seq, i=None):
    if i is None: i = len(seq)-1
    if i == 0: return
    ins_sort_rec1(seq, i-1)
    j = i
    for j in range(i):
        if j == 0 or seq[j-1] < seq[j]:
            j += 1
        else:
            seq[j-1], seq[j] = seq[j], seq[j-1]
            j -= 1
    return seq

def ins_sort_ite(seq):
    for i in range(len(seq)):
        j = i
        while j > 0 and seq[j-1] > seq[j]:
            seq[j-1], seq[j] = seq[j] , seq[j-1]
            j -= 1
    return seq

def gnome_sort_for(seq):
    for i in range(len(seq)):
        for j in range(len(seq)):
            if j == 0 or seq[j-1] < seq[j]:
                j += 1
            else:
                seq[j-1], seq[j] = seq[j], seq[j-1]
                j -= 1
    return seq
    
def gnome_sort_while(seq):
    i = 0
    while i < len(seq):
        if i == 0 or seq[i-1] < seq[i]:
            i += 1
        else:
            seq[i-1], seq[i] = seq[i] , seq[i-1]
    return seq

def ins_sort_rec_while(seq, i=None):
    if i is None: i = len(seq)-1
    if i == 0: return
    ins_sort_rec_while(seq, i-1)
    j = i
    while j > 0 and seq[j-1] > seq[j]:
        seq[j-1], seq[j] = seq[j] , seq[j-1]
        j -= 1
    return seq

def ins_sort_rec_for(seq,i=None):
    if i is None: i = len(seq)-1
    if i == 0: return
    ins_sort_rec_for(seq, i-1)
    j = i
    for j in range(i):
        if j == 0 or seq[j-1] < seq[j]:
            j += 1
        else:
            seq[j-1], seq[j] = seq[j], seq[j-1]
            j -= 1
    return seq

def ins_sort_ite(seq):
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
    for j in range(i):
        if seq[j] > seq[max_i]: max_i = j
    seq[i], seq[max_i] = seq[max_i], seq[i]
    sel_sort_rec(seq, i-1)
    return seq

def sel_sort_ite(seq):
    for i in range(len(seq)-1, 0, -1):
        max_i = i
        for j in range(i):
            if seq[j] > seq[max_i]: max_i = j
        seq[i], seq[max_i] = seq[max_i], seq[i]
    return seq

def quicksort_rec(seq):
    if len(seq) < 2: return seq
    else:
        pivot = seq[0]
        left = [i for i in seq[1:] if i <= pivot]
        right = [i for i in seq[1:] if i > pivot]
        return quicksort(left) + [pivot] + quicksort(right)
    return seq

# graphs
# connected graphs
# walking through all connected graphs
def walk(G, s, S):
    P, Q = dict(), set()
    P[s] = None
    Q.add(s)
    while Q:
        u = Q.pop()
        for v in G[u].difference(P,S):
            if v in P: continue
            Q.add(v)
            P[v] = u
    return P

def components(G, s, S=set()):
    comp = []
    seen = set()
    S.add(s)
    while S:
        u = S.pop()
        for v in G[u]:
            if v in seen: continue
            c = walk(G, v)
            seen.update(c)
            comp.append(c)
    return comp

def dfs(G, s, P=None):
    P, Q = set(), []
    Q.append(s)
    while Q:
        u = Q.pop()
        if u in P: continue
        P.add(u)
        Q.append(G[u])
        yield u
    
def dfs_ite(G, s, P=None):
    P, Q = set(), []
    Q.append(s)
    while Q:
        u = Q.pop()
        if u in P: continue
        P.add(u)
        Q.append(G[u])
        yield u
    
def rec_dfs(G, s, S=None):
#   P, S = set(), set()        #the recursive version doesn't need previous
    if S is None: S = Set()
    S.add(s)
    for v in G[s]:
        if v in P: continue
        rec_dfs(G, v, S)

def dfs_ite(G, s, P=None):
    P, Q = set(), []
    Q.append(s)
    while Q:
        u = Q.pop()
        if u in P: continue
        P.add(u)
        Q.append(G[u])
        yield u

def dfs_rec(G, s, Q=None):
    if Q is None: Q = set()
    Q.add(s)
    for v in G[s]:
        if v in Q: continue
        dfs_rec(G, v, Q)
        
def dfs_ite(G, s, P=None):
    P, Q = set(), []
    Q.append(s)
    while Q:
        u = Q.pop()
        if u in P: continue
        P.add(u)
        Q.append(G[u])
        yield u

def dfs_rec(G, s, P=None):
    if P is None: P = set()
    P.add(s)
    for u in G[s]:
        if u in P: continue
        rec(G, u, P)

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
        
def bfs(G, s):
    P , Q = {s:None}, deque[s]
    Q.add(s)
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if v in P: continue
            P[v] = u
            Q.append(v)
        yield u
        
def top_sort(seq, S=None):
    if S is None: S = set(G)
    if len(S) == 1: return list(S)
    v = S.pop()
    arr = top_sort(seq, S)
    min_i = 0
    for i, u in enumerate(arr):
        if v in G[u]: min_i = i + 1
    seq.insert(min_i, v)
    return arr

def top_sort_naive(seq, S=None):
    if S is None: S = set(G)
    if len(S) == 1: return list(S)
    c = S.pop()
    arr = top_sort_naive(seq, S)
    min_i = 0
    for i, u in enumerate(arr):
        if c in G[u]: min_i = i + 1
    seq.insert(min_i, c)
    return arr

def top_sort_naive(seq, S= None):
    if S is None: S = set(G)
    if len(S) == 1: return list(S)
    c = S.pop()
    arr = top_sort_naive(seq, S)
    min_i = 0
    for i, v in enumerate(arr):
        if c in G[v]: min_i = i + 1
    seq.insert(min_i, c)
    return arr

# iterative deeping depth-first search
def iddfs(G, s):
    n = len(G)
    seen = set()
    def recurse(G, u, d, S=None):
        if u not in seen: yield u
        seen.add(u)
        if d == 0: return
        if S is None: S = set()
        S.add(v)
        for v in G[s]:
            if v in S: continue
            for z in recurse(G, v, d-1, S):
                yield z
    for d in range(n):
        if len(seen) == n: break
        for v in recurse(G, s, d):
            yield v
            
# another go
def bfs(G, s):
    P, Q = {s: None}, deque[s]
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if v in P: continue
            P[v] = u
            Q.append(v)
        yield u
        
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
            for v in recurse(G, s, d-1, S):
                yield v
    for d in range(n):
        if len(seen) == n: break
        for u in recurse(G, s, d):
            yield u

def walk(G, s, S=None):
    P, Q = dict(), set()
    P[s] = None
    Q.add(s)
    while Q:
        u = Q.pop()
        for v in G[u].difference(P,S):
            if v in P: continue
            P[v] = u
            Q.add(v)
    return P

def iddfs(G, s):
    Q = set()
    n = len(G)
    def recurse(G, s, d, S=None):
        if s not in Q: yield s
        Q.add(s)
        if d == 0: return
        if S is None: S = set()
        S.add(s)
        for u in G[s]:
            if u in S: continue
            for v in recurse(G, u, d-1, S):
                yield v
    for d in range(n):
        if len(Q) == d:	break
        for u in recurse(G, s, d):
            yield u
            
def naive_tsort(seq, S=None):
    if S is None: S = set(G)
    if len(S) == 1:  return list(S)
    v = S.pop()
    arr = naive_tsort(seq, S)
    min_i = 0
    for i, u in enumerate(arr):
        if v in G[v]: min_i += 1
    seq.insert(min_i, v)
    return arr
            
        
        
    

array = [9,0,2,6,4,6,7,0,1]
print(gnome_sort_while(array))
print(gnome_sort_for(array))
print(ins_sort_rec_while(array))
print(ins_sort_rec_for(array))
print(ins_sort_ite(array))
print(sel_sort_rec(array))
print(sel_sort_ite(array))

# bisection
def binary(arr, value, low=0, upp=None):
    if upp is None:
        upp = len(arr)
    while low < upp:
        mid = (low+upp)//2
        if value < arr[mid]: upp = mid
        else: low = mid+1
    return low

def binary_search(arr, val, lo=0,hi=None):
    if hi is None:
        hi = len(arr)
    while lo < hi:
        mid = (lo + hi)//2
        if x < arr[mid]: hi = mid
        else: lo = arr[mid+1]
    return lo

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
            for v in recurse(G, s, d-1, S):
                yield v
    for d in range(n):
        if len(seen) == n: break
        for u in recurse(G, s, d):
            yield u
            
def binary_search_ite(seq, val, lo=0, hi=None):
    if hi is None:
        hi = len(seq)
    while lo < hi:
        mid = (lo+hi)//2
        if x < arr[mid]: hi = mid
        else: lo = arr[mid+1]
    return lo
# binary search tree
class Node:
    lft = None
    rgt = None
    def __init__(self, key, val):
        self.key = key
        self.val = val

def insert(node, key, val):
    if node is None: return Node(key,val)
    if node.key == key: node.val = val
    elif key < node.key:
        node.lft = insert(node.lft, key, val)
    else:
        node.rgt = insert(node.rgt, key, val)
    return node
def search(node, key):
    if node is None: raise KeyError
    if node.key == key: return node.val
    elif key < node.key:
        return search(node.lft, key)
    else:
        return search(node.rgt, key)
    
class Tree:
    root = None
    def __setitem__(self, key, val):
        self.root = insert(self.root, key, val)
    def __getitem__(self, key):
        return search(self.root, key)
    def __contains__(self, key):
        try: search(self.root, key)
        except KeyError: return False
        return True
    
def walk(G, s):
    P, Q = dict(), set()
    P[s] = None
    Q.add(s)
    while Q:
        u = Q.pop()
        for v in G[u].difference(P,S):
            if v in P: continue
            P[v] = u
            Q.add(u)
    return P

def traverse(G, s, qtype=set):
    P, Q = set(), qtype()
    Q.add(s)
    while Q:
        u = Q.pop()
        if u in P: continue
        P.add(s)
        for v in G[u]:
            Q.add(v)
        yield u
        
class Node:
    lft = None
    rgt = None
    def __init__(self,key, val):
        self.key == key
        self.val == val

def insert(node, key, val):
    if node is None: Node(key, val)
    if node.key == key: node.value = val
    elif key < node.key:
        node.lft = insert(node.lft, key, val)
    else:
        node.rgt = insert(node.lft, key, val)
    return node

def search(node, val):
    if node is None: raise KeyError
    if node.key == key: return node.val
    elif key < node.key: return search(node.lft, key)
    else: search(node.rgt, key)
    
class Tree:
    root = None
    def __setitem__(self,key, value):
        self.root = insert(self.root, key, value)
    def __getitem__(self, key):
        search(self.root,value)
    def __contains__(self, key):
        try: search(self.root, key)
        except KeyError: return False
        return True
    
def naive_top_sort(G, S=None):
    if S is None: S = set(G)
    if len(S) == 1: return list(S)
    v = S.pop()
    arr = naive_top_sort(G, S)
    min_i = 0
    for i, u in enumerate(arr):
        if v in G[u]: min_i += 1
    seq.insert(min_i, v)
    return seq

class Node:
    lft = None
    rgt = None
    def __init__(self, key, val):
        self.key = key
        self.val = val

def insert(node, key, val):
    if node is None: Node(key,val)
    if node.key == key: node.val = val
    elif node.key < key:
        node.lft = insert(node.lft, key, val)
    else:
        node.rgt = insert(node.rgt, key, val)
    return node

def search(node, key):
    if node is None: raise KeyError
    if node.key == key: return node.val
    elif node.key < key:
        return search(node.lft, key)
    else:
        return search(node.rgt, key)
    
class Tree:
    root = None
    def __setitem__(self, key, value):
        self.root = insert(self.root, key, value)
    def __getitem__(self, key):
        return search(self.root, key)
    def __contains__(self, key):
        try: search(self.root, key)
        except KeyError: return False
        return True
    
def gnomesort_retry_for(seq):
    for i in range(len(seq)):
        for j in range(len(seq)):
            if j == 0 or seq[j-1] < seq[j]:
                j += 1
            else:
                seq[j-1], seq[j] = seq[j], seq[j-1]
                j -= 1
    return seq

def gnomesort_retry_while(seq):
    i = 0
    while i < len(seq):
        if i == 0 or seq[i-1] < seq[i]:
            i += 1
        else:
            seq[i-1], seq[i] = seq[i], seq[i-1]
            i -= 1
    return seq

def retry_sort_ins_for(seq, i=None):
    if i is None: i = len(seq)-1
    if i == 0: return
    retry_sort_ins_for(seq, i-1)
    j = i
    for j in range(i):
        if j == 0 or seq[j-1] < seq[j]:
            j += 1
        else:
            seq[j-1], seq[j] = seq[j], seq[j-1]
            j -= 1
    return seq

def retry_sort_ins_while(seq, i=None):
    if i is None: i = len(seq)-1
    if i == 0: return
    retry_sort_ins_while(seq, i-1)
    j = i
    while j > 0 and seq[j-1] > seq[j]:
        seq[j-1], seq[j] = seq[j] , seq[j-1]
        j -= 1
    return seq

def retry_sort_ins_ite(seq):
    for i in range(len(seq)):
        j = i
        while j > 0 and seq[j-1] > seq[j]:
            seq[j-1], seq[j] = seq[j], seq[j-1]
            j -= 1
        return seq
    
# selection
# using the partition and select method
# to find the kth smallest
# in the randomized select the pivot is chosen pretty randomly
def partition(seq):
    pi, seq = seq[0], seq[1:]
    lo = [x for x in seq if x <= pi]
    hi = [x for x in seq if x > pi]
    return lo, pi, hi

def select(seq, k):
    lo, pi, hi = partition(seq)
    m = len(lo)
    if m == k: return pi
    elif m < k:
        return select(hi, k-m-1)
    else:
        return select(lo, k)

print(select(array, 7))

# another version of quicksort
def quicksort(seq):
    if len(seq)<= 1: return seq
    lo, pi, hi = partition(seq)
    return quicksort(lo)+[pi]+quicksort(hi)

# mergesort
def mergesort(seq):
    mid = len(seq)//2
    lft, rgt = seq[:mid], seq[mid:]
    if len(lft) > 1: lft = mergesort(lft)
    if len(rgt) > 1: rgt = mergesort(rgt)
    res = []
    while lft and rgt:
        if lft[-1] >= rgt[-1]:
            res.append(lft.pop())
        else:
            res.append(rgt.pop())
    res.reverse()
    return (lft or rgt) + res

# greatest slice
n = len(array)
result = max((array[i:j] for i in range(n) for j in range(i+1,n+1)), key = sum)
print(result)
    
# refactoring greatest slice to run in quadratic time
def greatest_slice(arr):
    best = arr[0]
    n = len(arr)
    for size in range(1,n+1):
        cur = sum(arr[:size])
        for i in range(n-size):
            cur += arr[i+size] - arr[i]
            best = max(best, cur)
    return best

print(greatest_slice(array))
