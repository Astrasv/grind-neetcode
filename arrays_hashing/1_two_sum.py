from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            check = target - num
            if check in num_map:
                return [i, num_map[check]]
            num_map[num] = i
