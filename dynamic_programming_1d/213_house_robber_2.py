from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        def dfs(index, end, memo):
            if index > end:
                return 0
            if index in memo:
                return memo[index]

            rob_current = nums[index] + dfs(index + 2, end, memo)
            skip_current = dfs(index + 1, end, memo)
            memo[index] = max(rob_current, skip_current)
            return memo[index]

        res1 = dfs(0, n - 2, {})
        res2 = dfs(1, n - 1, {})
        
        return max(res1, res2)