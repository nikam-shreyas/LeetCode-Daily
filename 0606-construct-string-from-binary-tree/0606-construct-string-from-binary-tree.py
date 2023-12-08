# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        self.ans = []
        if not root:
            return ""
        def recurse(root):
            self.ans.append(str(root.val))
            if root.left:
                self.ans.append('(')
                recurse(root.left)
                self.ans.append(')')
            if root.right:
                if not root.left:
                    self.ans.append('()')
                self.ans.append('(')
                recurse(root.right)
                self.ans.append(')')
        recurse(root)
        return ''.join(self.ans)