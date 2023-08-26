# heaps
# an example of building a heap piece by piece:
from heapq import heappush, heappop
from random import randrange
Q = []
for i in range(10):
    heappush(Q, randrange(100))
    
print(Q)
print([heappop(Q) for i in range(10)])

# just like bisect
def sift_up(heap, startpos, pos):
    newitem = heap[pos]					# The item we're sifting up
    while pos > startpos:				# Don't gp beyond the root
        parentpos = (pos - 1) >> 1 		# The same as (pos-1)//2
        parent = heap[parentpos]		# Who's your daddy?
        if parent <= newitem: break		# Valid parent found
        heap[pos] = parent				# Otherwise: copy parent down
        pos = parentpos					# Next candidate position
    heap[pos] = newitem					# Place the item in its spot
    

denom = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1]
owed = 5632
payed = []
for d in denom:
    while owed >= d:
        owed -= d
        payed.append(d)

print(sum(payed))
print(payed)

