# Binary search
from bisect import bisect
a = [0,2,3,5,6,8,8,9]
print(bisect(a,5))

def bisect_right(a, x, lo=0, hi=None):
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if x < a[mid]: hi = mid
        else: lo = mid+1
    return lo