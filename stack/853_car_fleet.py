from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        nums = sorted(zip(position, speed), key=lambda x: -x[0]) 
        monostack = []
        
        for d, s in nums:
            time = (target - d) / s  
            
            if not monostack or time > monostack[-1]:
                monostack.append(time)
        
        print(monostack)
        return len(monostack)
