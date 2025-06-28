from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        
        s1_count = Counter(s1)
        s2_count = Counter(s2[:len(s1)])
        
        if s1_count == s2_count:
            return True
        
        for i in range(len(s1), len(s2)):
            start_char = s2[i - len(s1)]
            end_char = s2[i]
            
            s2_count[end_char] += 1
            s2_count[start_char] -= 1
            
            # Delete key if char not there in counter
            if s2_count[start_char] == 0:
                del s2_count[start_char]
                
            if s1_count == s2_count:
                return True
        
        return False
