# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []

        def parcours(node):
            if not node: 
                return 

            parcours(node.left)
            values.append(node.val)
            parcours(node.right)

        parcours(root)
        return values[k - 1]
