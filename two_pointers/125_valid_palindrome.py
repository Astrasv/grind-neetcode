class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        for i in s:
            if i.isalnum()==False:
                s=s.replace(i,"")
        
        left , right = 0 , len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        
        return True