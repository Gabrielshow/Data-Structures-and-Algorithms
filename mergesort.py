#Gnome sort- it is a simplified version of the insertion sort
def gnomesort(seq):
    i = 0
    while i < len(seq):
        if i == 0 or seq[i-1] <= seq[i]:
            i += 1
        else:
            seq[i], seq[i-1] = seq[i-1], seq[i]
            i -= 1
    return seq
            

def mergesort(seq):
    mid = int(len(seq)/2)
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
    return (lft or right) + res

array_to_sort = [9, 0, 4, 7, 8]
print(gnomesort(array_to_sort))
print(mergesort(array_to_sort))
