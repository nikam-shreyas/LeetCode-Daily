# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def rightPreorder(root, val):
            if root is None:
                return
            if root.right:
                val=rightPreorder(root.right, val)
            root.val += val
            val=root.val
            if root.left:
                val = rightPreorder(root.left, val)
            return val
        rightPreorder(root, 0)
        return root
        
                
            
                
                