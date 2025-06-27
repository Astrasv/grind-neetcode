from typing import List
class Solution:
    def maxArea(self, nums: List[int]) -> int:
        left,right = 0, len(nums)-1
        max_area = 0
        while left < right:
            curr_area = min(nums[left],nums[right]) * (right-left)
            if nums[left] < nums[right]:
                left += 1
            else:
                right -= 1
            max_area = max(curr_area,max_area)
        
        return max_area