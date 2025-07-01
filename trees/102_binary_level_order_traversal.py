from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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
        
        cur_level = 0
        final_result =[]
        each_level = []
        for val,level in result:
            if level != cur_level:
                final_result.append(each_level)
                cur_level += 1
                each_level = [val]
            else:
                each_level.append(val)
        if cur_level == level:
            final_result.append(each_level)
        return final_result

