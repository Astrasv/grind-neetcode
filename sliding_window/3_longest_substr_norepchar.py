class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:return 0
        if len(s) == 1: return 1

        l,r = 0,1
        
        visited = set()
        visited.add(s[l])

        max_len = 0
        winlen = 1

        while r < len(s) :
            if s[r] not in visited:
                visited.add(s[r])
                winlen += 1
                r += 1
            else:
                max_len = max(max_len,winlen)
                winlen -= 1
                visited.remove(s[l])
                l += 1
        
        max_len = max(max_len,winlen)
        return max_len
            
