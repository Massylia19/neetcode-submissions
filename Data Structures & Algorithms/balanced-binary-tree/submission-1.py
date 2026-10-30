# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def maxHeight(node): 
            if node is None: 
                return 0 
            
            left = maxHeight(node.left)
            right = maxHeight(node.right)

            return 1 + max(left,right)

        if root is None: 
            return True
        if abs(maxHeight(root.left) - maxHeight(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        else: 
            return False