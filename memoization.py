def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    answer = []
    def combinationSumHelper(candidates, cur_index, cur_sum, cur_combination, target):
        if cur_sum ==target:
            answer.append(current_combination)
            return
        if cur_sum > target:
            return
        for i in range(cur_index, len(candidates)):
            combinationSumHelper(candidates, i, cur_sum + candidates[i], current_combination + [candidates[i]], target)
    combinationSumHelper(candidates, 0, 0,[], target)
    return answer

#memoization/dynamic programming
def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    dp = [[] for i in range(target + 1)]
    dp[0].append([])
    
    for candidate in candidates:
        for i in range(1, target + 1):
            if i - candidate >= 0:
                for combination in dp[i-candidate]:
                    dp[i].append(combination + [candidate])
    return dp[-1]