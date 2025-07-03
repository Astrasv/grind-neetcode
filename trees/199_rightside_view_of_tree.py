from collections import deque
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
            if not root: return []

            result = []
            queue = deque([])
            queue.append((root,0))
            while queue:
                popped,level = queue.popleft()
                result.append((popped.val,level))
                if popped.left is not None:
                    queue.append((popped.left,level+1))
                if popped.right is not None:
                    queue.append((popped.right,level+1))
            return result
        
        result = levelOrder(root)
        
        final_result =[]
        i=0
        while i < len(result) - 1:
            if result[i+1][1] != result[i][1]:
                final_result.append(result[i][0])
            i += 1
        
        print(i,len(result))
        final_result.append(result[i][0])
        return final_result
            
