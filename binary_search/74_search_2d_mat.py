from typing import List 
class Solution:
    def searchMatrix(self,nums: List[List[int]], target: int) -> bool:
        rows = len(nums)
        cols = len(nums[0])

        left,right = 0, rows*cols - 1
        while left <= right:
            mid = (left + right) // 2
            
            x,y = mid // cols , mid % cols
            if nums[x][y] < target: left = mid + 1
            elif nums[x][y] > target: right = mid - 1
            else: 
                return True
        
        return False
