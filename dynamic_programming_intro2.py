from collections import defaultdict

def pascal_triangle(n,k):
    C = defaultdict(int)
    for row in range(n+1):
        C[row, 0] = 1
        for col in range(1,k+1):
            C[row,col] = C[row-1, col-1] + C[row-1, col]
    return C[n, k]
print(pascal_triangle(100, 50))

def memo(func):
    cache = {}
    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap

# Recursive Memoized DAG shortest Path
def rec_dag_sp(W, s, t):
    @memo
    def d(u):
        if u == t: return 0
        return min(W[u][v]+d(v) for v in W[u])
    return d(s)

# iterative solution
def dag_sp(W, s, t):
    d = {u:float('inf') for u in W}
    d[s] = 0
    for u in topsort(W):         # already implemented just import it
        if u == t: break
        for v in W[u]:
            d[v] = min(d[v], d[u] + W[u][v])
    return d[t]

# this above is the iterative algorithm
# there ave many ways of finding the shortest path in a DAG and, by extension,
# solving most DP problems. You could do it recursively, with memoization, or you could do it iteratively, wiht relaxation.
# for the recursion start at the first node, try various "next steps" and the recurse on the remainder, or if your graph representation permits, you could
# look at the last node and try " previous steps" and recurse on the initial part. the former is usually much more natural, while the latter corresponds more closely to what happens in the iterative version.
# if you use the iterative version, you also have two choices: you can relax the edges out of each node( in topsort order) or you can relax all edges into each node.
# the latter more obviously yields a correct result but requires access to nodes by following edges bakward.
# outward relaxation, called reaching, is exactly equivalent when you relax all edges. As explained, once you get to a node, all its in-edges will have been relaxed anyway. However, with reaaching, you can do something that's hard in the recursive version(or relaxing in-edges): pruning.
# if, for example, you're interested only in finding all nodes that are within a distance r, you can skip any node that has distance estimate greater tahn r. you wil still need to visit every node, but you can potentially ignore lots of edges during the relaxation. this won't affect the asymptotic running time, though

# finding the longest nondecreasing subsequence
# recursive decomposition/sub problems
def rec_lis(seq):
    @memo
    def L(cur):
        res = 1
        for pre in range(cur):
            if seq[pre] <= seq[cur]:
                res = max(res, 1 + L(pre))
        return res
    return max(L(i) for i in range(len(seq)))

# iterative version
def basic_lis(seq):
    L = [1] * len(seq)
    for cur, val in enumerate(seq):
        for pre in range(cur):
            if seq[pre] <= val:
                L[cur] = max(L[cur], 1 + L[pre])
    return max(L)