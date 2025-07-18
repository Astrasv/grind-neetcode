from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(p, q):
            if p is None and q is None:return True
            if p is None or q is None:return False
            
            if p.val == q.val:
                return isSame(p.left, q.left) and isSame(p.right, q.right)
            
            return False

        if not root: return False
        if isSame(root, subRoot): return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
