"""
Input: root = [1,2,3,4], x = 4, y = 3
Output: false

Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true

Time Complexity = O(N)
Space Complexity = O(2^d)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        if not root.val:
            return False
        
        queue = deque()        
        queue.append((root, 0))
        out = {x: [None, None], y: [None, None]}
        found = 2
        
        while queue:
            node, depth = queue.popleft()
            left  = node.left
            right = node.right
            
            if left:
                if left.val in out:
                    found -= 1
                    out[left.val] = [node.val, depth + 1]
                queue.append((left, depth + 1))
            
            if right:
                if right.val in out:
                    found -= 1
                    out[right.val] = [node.val, depth + 1]
                queue.append((right, depth + 1))
             
            if not found:
                break                

            
        x_p, x_d = out[x]
        y_p, y_d = out[y]
        
        if x_p != y_p and x_d == y_d:
            return True
        else:
            return False