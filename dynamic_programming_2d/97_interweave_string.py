class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}
        
        def recur(ptr1, ptr2, ptr3):
            if (ptr1, ptr2) in memo:
                return memo[(ptr1, ptr2)]

            if ptr1 == len(s1) and ptr2 == len(s2) and ptr3 == len(s3):
                return True
            
            ans = False
            if ptr1 < len(s1) and ptr1 + ptr2 < len(s3) and s1[ptr1] == s3[ptr3]:
                ans = ans or recur(ptr1 + 1, ptr2, ptr3 + 1)
            if ptr2 < len(s2) and ptr1 + ptr2 < len(s3) and s2[ptr2] == s3[ptr3]:
                ans = ans or recur(ptr1, ptr2 + 1, ptr3 + 1)

            memo[(ptr1, ptr2)] = ans
            return ans

        if len(s1) + len(s2) != len(s3):
            return False
        
        return recur(0, 0, 0)