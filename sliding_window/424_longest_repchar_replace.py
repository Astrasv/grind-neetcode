class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left,right = 0,0
        winlen = 0
        freq = [0] * 26
        res = 0
        while right < len(s):
            freq[ord(s[right])-65] += 1
            winlen = right - left + 1
            if winlen - max(freq) <= k:
                right += 1
            else:
                
                res = max(res,right - left)
                freq[ord(s[left])-65] -= 1
                freq[ord(s[right])-65] -= 1
                left += 1



        return max(res,right - left)