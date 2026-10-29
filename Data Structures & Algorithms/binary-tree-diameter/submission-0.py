# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_dim = 0 
        def parcours(node):
    
            if node is None: 
                return 0

            diam_right = parcours(node.right)
            diam_left = parcours(node.left)

            self.max_dim = max(self.max_dim, diam_left + diam_right)

            return max(diam_right, diam_left) + 1
           
        
        if root is None:  
            return 0 
        
        parcours(root)
        return self.max_dim
        


        