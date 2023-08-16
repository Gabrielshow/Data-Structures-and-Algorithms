# to use timeit to check the a function speed
# python -m timeit -s"import mymodule as m" "m.myfunction()
# Graph nomenclature
# a graph G = (v, e) consists of a set of nodes, v, and edges between them, e. if teh edges have a direction, we say the graph is directed
# nodes with an edge between them are adjacent. the edge is then incident to both.
# the nodes that are adjacent to v are the neighbors of v.
# the degree of a node is the number of edges incident to it.
# subgraph of G = (V, E) consists of a subset of V and a subset of E. a path in G is a subgraph
# where the edges connect the nodes in a sequence, without revisiting any node. A cycle is like a path, exvept that the last edge links the last node to the first.
# if we associate a weight with each edge in G, we say that G is a weighted graph. the length ofa path or cycle is the sum of its edge weights, or, for unweighted graphs, simply the number of edges
# a forest is a cycle-free graph, and a connected forest is a tree. in other words, a forest consists of one or more trees.
# one of the most intuituve ways of implementing graphs is using adjacency lists. Basically, for each node, we can access a list(or set or other container or iterable) of its neighbors.
# a simple graph
a, b, c, d, e,f ,g,h = range(8)
N = [{b,c,d,e,f},  #adjacency sets for a
     {c, e},  #b
     {d}, #c
     {e}, #d
     {f}, #e
     {c,g,h}, #f
     {f,h},  #g
     {f,g}  #h
     ]
#an empty set is written as set() because {} is an empty dict.
print(b in N[a])
print(len(N[f]))

# we could replace the adjacency sets with an adjacency list
# the best representation depends on what you need to do with your graph. e.g. using adjacency lists(or arrays) keeps the overhead low and lets you efficiently iterate over N(v) for any node v.
# However, checking whether u and v are neighbors is linear in the minimum of their degrees, which can be problematic if the graph is dense, that is, if it has many edges. In these cases, adjacency sets may be the way to go.
# deleting objects from the middle of a Python list is costly. Deleting from the end of a list takes constant time, though.
# If you don't care about the order of the neighbors, you can delete arbitrary neighbors in constant time by overwriting them wiht the one that is currently last in the adjacency list, before calling the pop method.
# a slight variation of this would be to represent the neighbor sets as sorted lists.
# if you aren't modifying the lists much, you can keep them sorted and use bisection to check for membership, which might lead to slightly less overhead in terms of memory use and iteration time
# but would lead to a membership check complexity of O(log k) where k is the number of neighbors fo rthe given node.(This is still very low, in practice using the built-in set type is a lot less hassle)
# another way is to use dicts instead of sets or lists. the neighbors would then be keys in this dict, and you're free to associate each neighbor(or out-edge) with some extra value, such as an edge weight
# this is shown with arbitrary edge weights added.
# a, b, c, d, e, f, g, h = range(8)
# N =  [
#  {b:2, c:1, d:3, e:9, f:4}, # a
#  {c:4, e:3}, # b
#  {d:8}, # c
#  {e:7}, # d
#  {f:5}, # e
#  {c:2, g:2, h:2}, # f
#  {f:1, h:6}, # g
#  {f:9, g:8} # h
# ]
# until now, the main collection containing our adjecency structures-be they lists, sets, or dicts- has been a list, indexed by the node number. A more flexible approach, allowing us to use arbitrary, hashable, node labels, is to use a dict as this main structure.
# N = {
#     'a': set('bcdef'),
#     'b': set('ce'),
#     'c': set('d'),
#     'd': set('e'),
#     'e': set('f'),
#     'f': set('cgh'),
#     'g': set('fh'),
#     'h': set('fg')
#     }

#using adjacency matrix
# a, b, c, d, e, f, g, h = range(8)
# # a b c d e f g h
# N = [[0,1,1,1,1,1,0,0], # a
#  [0,0,1,0,1,0,0,0], # b
#  [0,0,0,1,0,0,0,0], # c
#  [0,0,0,0,1,0,0,0], # d
#  [0,0,0,0,0,1,0,0], # e
#  [0,0,1,0,0,0,1,1], # f
#  [0,0,0,0,0,1,0,1], # g
#  [0,0,0,0,0,1,1,0]] # h
# The way we’d use this is slightly different from the adjacency lists/sets. Instead of checking whether b is in N[a], 
# you would check whether the matrix cell N[a][b] is true. Also, you can no longer use len(N[a]) to find the number of 
# neighbors, because all rows are of equal length. Instead, use sum:
# >>> N[a][b] # Neighborhood membership
# 1
# >>> sum(N[f]) # 3
# inf = float('inf') to let nonexistent edges get an infinite weight
# we could also assign them to None, -1
i, j, k, l, m, n, o, p = range(8)
inf = float('inf')
# # a b c d e f g h
W = [[ 0, 2, 1, 3, 9, 4, inf, inf], # a
 [inf, 0, 4, inf, 3, inf, inf, inf], # b
 [inf, inf, 0, 8, inf, inf, inf, inf], # c
 [inf, inf, inf, 0, 7, inf, inf, inf], # d
 [inf, inf, inf, inf, 0, 5, inf, inf], # e
 [inf, inf, 2, inf, inf, 0, 2, 2], # f
 [inf, inf, inf, inf, inf, 1, 0, 6], # g
 [inf, inf, inf, inf, inf, 9, 8, 0]] # h
# Weight  matrices make it easy to access edge weights, of course, but membership checking and finding the degree 
# of a node, for example, or even iterating over neighbors must be done a bit differently now. You need to take the 
# infinity value into account. Here’s an example:
# W[a][b] < inf # Neighborhood membership
# True
# W[c][e] < inf # Neighborhood membership
# False
print(sum(1 for w in W[a] if w < inf) - 1) # Degree sum
N = [[0]*10 for i in range(10)]
# in NumPy, you can use the zeros function:
# >>> import numpy as np
# >>> N = np.zeros([10,10])
# if you have a relatively sparse graph, with only a small protion of a the matrix filled in,
# you could save quite a bit of memory by using an even more specialized form of sparse matrix, available as part of the scipy distribution
# in the scipy.sparse module
T = [["a", "b"], ["c"], ["d", ["e", "f"]]]
print(T[0][1])
print(T[2][1][0])

# 5