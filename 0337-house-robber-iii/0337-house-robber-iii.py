# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        dp = {}
        def recurse(root):
            if not root:
                return 0
            if root in dp:
                return dp[root]
            robbed = root.val
            nrobbed = 0
            if root.left:
                nrobbed+=recurse(root.left)
                if root.left.left:
                    robbed+=recurse(root.left.left)
                if root.left.right:
                    robbed+=recurse(root.left.right)
            if root.right:
                nrobbed+=recurse(root.right)
                if root.right.left:
                    robbed+=recurse(root.right.left)
                if root.right.right:
                    robbed+=recurse(root.right.right)
            dp[root] = max(robbed, nrobbed)
            return dp[root]
        return recurse(root)
        