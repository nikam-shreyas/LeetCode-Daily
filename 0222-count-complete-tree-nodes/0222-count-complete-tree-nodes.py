# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode], pow=0) -> int:
        if not root:
            return 0
        if root.right or root.left:
            return 1+self.countNodes(root.right)+self.countNodes(root.left)
        return 1