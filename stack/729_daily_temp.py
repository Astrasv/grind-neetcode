from typing import List
class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        monostack = []  
        res = [0] * len(nums)

        for i in range(len(nums)):
            while monostack and nums[i] > monostack[-1][1]:
                j, temp = monostack.pop()
                res[j] = i - j
            monostack.append((i, nums[i]))

        return res
