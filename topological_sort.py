# topological sort
def topsort(G):
    count = dict((u, 0) for u in G)						# the in- degree for each node
    for u in G:
        for v in G[u]:
            count[v] += 1
    Q = [u for u in G if count[u] == 0]
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# naive solution
def naive_topsort(G, S=None):
    if S is None: S = set(G)
    if len(S) == 1: return list(S)
    v = S.pop()
    arr = naive_topsort(G, S)
    min_i = 0
    for i, u in enumerate(arr):
         if v in G[u]: min_i = i+1
    seq.insert(min_i, v)
    return arr