from random import randrange
def firstseq():
    seq = [randrange(10**10) for i in range(100)]
    dd = float("inf")
    for x in seq:
        for y in seq:
            if x == y: continue
            d = abs(x-y)
            if d < dd:
                xx, yy, dd = x, y, d
    return xx, yy, dd
                
def secondseq():
    seq = [randrange(10**10) for i in range(100)]
    seq.sort
    dd = float("inf")
    for i in range(len(seq)-1):
        x,y = seq[i], seq[i+1]
        if x == y: continue
        d = abs(x-y)
        if d < dd:
            xx, yy, dd = x, y, d
    return xx, yy, dd


print(firstseq())
print(secondseq())
    