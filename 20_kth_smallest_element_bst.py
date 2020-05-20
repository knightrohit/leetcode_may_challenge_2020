"""
root = [3,1,4,null,2], k = 1
output = 1

Time Complexity = O(h), h = height of the bst
Space Complexity = O(N)
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        self.out = []
        
        def traverse(node):
            
            if len(self.out) >= k:
                return None
            
            if not node:
                return None
            
            left = traverse(node.left) 
            if left:
                self.out.append(left.val)
            # Add head
            self.out.append(node.val)
            
            right = traverse(node.right)
            if right:
                self.out.append(right.val)           
        
        traverse(root)
        
        if len(self.out) >= k:
            return self.out[k-1]
        else:
            return None