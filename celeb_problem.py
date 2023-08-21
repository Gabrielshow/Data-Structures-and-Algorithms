# celebrity problem
# knows no one, but everyone knows him
from random import randrange

# naive solution
def naive_celeb(G):
    n = len(G)
    for u in range(n):						# For every candidate...
        for v in range(n):					# For everyone else...
            if u == v: continue				# Same person? Skip.
            if G[u][v]: break				# Candidate knows other
            if not G[u][v]: break			# Other doesn't know candidate
        else:
            return u						# No breaks? Celebrity!
    return None							# Couldn't find anyone


# Refactoring naive solution
# to improve the problem we must find a non-celebrity someone who either knows someone or is unknown by someone else.
# if we check G[u][v] for any nodes u and v, we can eliminate either u or v!
# if G[u][v] is true, we eliminate u
def celeb(G):
    n = len(G)
    u, v = 0, 1													# The first two
    for c in range(2, n+1):										# Others to check
        if G[u][v]: u = c										# u knows v? replace u
        else: v = c												# Otherwise, replace v
    if u == n: c = v											# u was replaced last; use v
    else:      c = u											# otherwise, u is a candidate
    for v in range(n):											# for everyone else...
        if c == v: continue										# Same person? Skip.
        if G[c][v]: break										# Candidate knows other
        if not G[v][c]: break									# Other doesn't know candidate
    else:
        return c												# No breaks? celebrity!
    return None													# Couldn't find anyone

# creating a random graph
num = 100
P = [[randrange(2) for i in range(num)] for i in range(num)]
e = randrange(num)
for i in range(num):
    P[i][e] = True
    P[e][i] = False
    #print(naive_celeb(P))
    print(celeb(P))
        
