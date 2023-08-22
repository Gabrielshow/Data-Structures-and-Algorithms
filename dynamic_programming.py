# minimum coin problem
# dynamic programming
def min_ignore_none(a, b):
    if a is None:
        return b
    if b is None:
        return a
    return min(a,b)

def minimum_coins(m, coins):
    if m == 0:
        answer = 0
    else:
        answer = None
        for coin in coins:
            subproblem = m - coin
            if subproblem < 0:
                # skip solutions where we try to reach [m]
                # from a negative subproblem.
                continue
            answer = min_ignore_none(answer, minimum_coins(subproblem, coins) + 1)
    return answer

print(minimum_coins(13, [1, 4, 5]))

# using memoization

def memo_coins(m, coins):
    memo = {}
    if m in memo:
        return memo[m]
    if m == 0:
        answer = 0
    else:
        answer = None
        for coin in coins:
            subproblem = m - coin
            if subproblem < 0:
                continue
            answer = min_ignore_none(answer, minimum_coins(subproblem, coins) + 1)
    memo[m] = answer
    return answer

# another approach, the fastest of the memo type
def memo(m, coins):
    memo = {}
    memo[0] = 0
    for i in range(1, m+1):
        for coin in coins:
            subproblem = i - coin
            if subproblem < 0:
                continue
            memo[i] = min_ignore_none(memo.get(i), memo.get(subproblem) + 1)
    return memo[m]

print(memo(150, [1,5,4]))

# In how many ways can we form the sum m using these coins?
from collections import defaultdict

def how_many_ways(m, coins):
    memo = defaultdict(lambda _: 0)
    
    memo[0] = 1
    for i in range(1, m + 1):
        memo[i] = 0
        for coin in coins:
            subproblem = i - coin
            if subproblem < 0:
                continue
            memo[i] = memo[i] + memo[subproblem]
    return memo[m]

print(how_many_ways(7,[1,4,5]))

# Maze problem
# NxM grid, in how many ways can a rabbit get from the top-left to the bottom
# right corner if it can only move down or right?
def grid_paths(n, m):
    memo = {}
    for i in range(1, n+1):
        memo[(i,1)] = 1
    for j in range(1, m+1):
        memo[(1,j)] = 1
    
    for i in range(2, n+1):
        for j in range(2, m +1):
            memo[(i,j)] = memo[(i-1, j)] + memo[(i, j-1)]
    return memo[(n,m)]

print(grid_paths(18,6))
print(grid_paths(75,19))

# climbing stairs problem
# bottom-up position
class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n-1):
            one , two = one+two, one
        return one
s1 = Solution()
print(s1.climbStairs(10))