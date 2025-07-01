from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dfs(index):
            if index >= len(nums):
                return 0
            if index in memo:
                return memo[index]

            rob_current = nums[index] + dfs(index + 2)
            skip_current = dfs(index + 1)
            memo[index] = max(rob_current, skip_current)
            return memo[index]

        return dfs(0)