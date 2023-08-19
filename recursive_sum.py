#recursive version of sums
def S(seq, i=0):
    if i == len(seq): return 0
    return S(seq, i+1) + seq[i]

#running cost of S
def T(seq, i=0):
    if i == len(seq): return 1
    return T(seq, i+1) + 1

seq = range(1, 	101)
print(S(seq))
print(T(seq))