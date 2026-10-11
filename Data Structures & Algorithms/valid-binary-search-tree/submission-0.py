# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        values = []

        def parcours(node):
            if node is None: 
                return
            
            parcours(node.left)
            values.append(node.val)
            parcours(node.right)

        parcours(root)

        for i in range (1, len(values)):
            if values[i] <= values[i -1]: 
                return False 
        return True
            



