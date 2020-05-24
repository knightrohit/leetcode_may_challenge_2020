'''
Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

Time complexity = O(h)
Space complexity = O(N)
'''


# Definition for a binary tree node.
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        
        if preorder:
            val = preorder[0]
            node = TreeNode(val)
            i = 1
            
            while i < len(preorder):
                if val > preorder[i]:
                    i += 1                
                else:
                    break
            
            node.left = self.bstFromPreorder(preorder[1:i])
            node.right = self.bstFromPreorder(preorder[i:])
            return node