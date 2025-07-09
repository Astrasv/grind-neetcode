from math import ceil
from typing import List

class Solution:
    def minEatingSpeed(self, nums: List[int], h: int) -> int:
        def could_finish(nums, k):
            count = 0
            for num in nums:count += ceil(num / k)
            return count <= h

        left, right = 1, max(nums) 

        while left < right:
            mid = (left + right) // 2
            if could_finish(nums, mid):
                right = mid
            else:
                left = mid + 1

        return left
