# longest increasing subsequence
from itertools import combinations
from functools import wraps

def naive_lis(seq):
    for length in range(len(seq), 0, -1):
        for sub in combinations(seq, length):
            if list(sub) == sorted(sub):
                return sub
            

def fib(i):
    if i < 2: return 1
    return fib(i-1) + fib(i-2)

def memo(func):
    cache = {}
    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap

fib = memo(fib)
print(fib(100))

# memo is even designed to be used as a decorator
# e.g
# @memo
# def fib(i):
# 	  if i < 2: return 1
#     return fib(i-1) + fib(i-2)

@memo
def two_pow(i):
    if i == 0: return 1
    return two_pow(i-1) + two_pow(i-1)

print(two_pow(100))

# another version of the two_pow function is this which reduces the recursive call from two to one
def two_pow1(i):
    if i == 0: return 1
    return 2*two_pow1(i-1)
print(two_pow1(100))

@memo
def C(n, k):
    if k == 0: return 1
    if n == 0: return 0
    return C(n-1, k-1) + C(n-1,k)

print(C(100,50))

# Another method for filling Pascal's triangle
