# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.maxval = 0
        # 1 = right
        # 0 = left
        def recurse(root, direction, val):
            if root is None:
                self.maxval = max(self.maxval, val)
                return
            # print(root.val, direction, val)
            if direction==1:
                recurse(root.left, 0, val+1)
                recurse(root.right, 1, 1)
            else:
                recurse(root.left, 0, 1)
                recurse(root.right, 1, val+1)
        # print()
        recurse(root, 0, 0)
        recurse(root, 1, 0)
        return max(self.maxval-1, 0)