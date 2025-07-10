import heapq
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize != 0:
            return False
        
        freq = {}
        for num in hand: freq[num] = freq.get(num,0)+1
        
        minheap = list(freq.keys())
        heapq.heapify(minheap)
        while minheap:
            first = minheap[0]
            for i in range(first,first+groupSize):
                if i not in freq:
                    return False
                freq[i] -= 1
                if freq[i] == 0:
                    if i != minheap[0]:
                        return False
                    heapq.heappop(minheap)
        
        return True
