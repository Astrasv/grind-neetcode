from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = set()
        def backtrack(arr,temparr=[]):
            if len(arr) == len(temparr):
                res.append(temparr[::])
                return
            
            for num in arr:
                if num not in visited:
                    visited.add(num)
                    temparr.append(num)
                    backtrack(arr,temparr)
                    visited.remove(num)
                    temparr.pop()

        backtrack(nums)
        return res
        
        