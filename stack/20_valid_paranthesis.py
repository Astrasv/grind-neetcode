class Solution:
    def isValid(self, s: str) -> bool:

        paran_map = {')':'(' , '}':'{', ']':'['}
        stack = []
        for i in range(len(s)):
            if s[i] in [')',']','}']:
                if stack == []:
                    return False
                if stack.pop() != paran_map[s[i]]:
                    return False
                
            else:
                stack.append(s[i])
        
        return True if stack == [] else False
