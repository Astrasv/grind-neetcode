from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def dfs(paranthesis, num_open, num_close):
            if num_open == n and num_close == n:
                result.append(paranthesis)
                return
            if num_open < n:
                dfs(paranthesis + '(', num_open + 1, num_close)
            if num_close < num_open:
                dfs(paranthesis + ')', num_open, num_close + 1)

        dfs('', 0, 0)
        return result