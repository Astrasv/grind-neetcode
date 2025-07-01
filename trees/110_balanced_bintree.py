from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def balanced(node):
            if not node: return 1
            return abs(balanced(node.left)-balanced(node.right)) <= 1
        
        return balanced(root)