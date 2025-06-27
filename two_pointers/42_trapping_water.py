from typing import List
class Solution:
    def trap(self, arr: List[int]) -> int:
        count = 0
        n = len(arr)
        for i in range(1,n):
            left_max = max(arr[0:i])
            right_max = max(arr[i:n])
            level = min(left_max,right_max)
            if level > arr[i]:
                count += level - arr[i]

        return count