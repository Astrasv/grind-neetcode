from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = 0
        index = 0
        stack = []
        for ops in tokens:
            if ops == "+":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b + a)
            elif ops == "-":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b - a)
            elif ops == "*":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b * a)
            elif ops == "/":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b / a)
            else:
                stack.append(ops)

        return int(stack[0])
        