# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def recurse(a, b):
            if not a and not b:
                return True
            elif a and b and a.val==b.val:
                return recurse(a.left, b.left) and recurse(a.right, b.right)
            else:
                return False
        return recurse(p, q)
                
                