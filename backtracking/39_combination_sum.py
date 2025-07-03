from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(nums, target, temparr=[], current_sum=0, idx=0):
            if current_sum > target:
                return

            if current_sum == target:
                result.append(temparr[:])
                return

            for i in range(idx, len(nums)):
                num = nums[i]
                temparr.append(num)  
                backtrack(nums, target, temparr, current_sum + num, i)
                temparr.pop()  

        backtrack(nums, target, [], 0, 0)
        return result