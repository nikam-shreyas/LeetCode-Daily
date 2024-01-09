# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        seq = []
        def dfs(root):
            if not root:
                return
            stack = [root]
            while stack:
                curr = stack.pop()
                if not curr.left and not curr.right:
                    seq.append(curr.val)
                if curr.left:
                    stack.append(curr.left)
                if curr.right:
                    stack.append(curr.right)
        dfs(root1)
        s1 = seq[:]
        seq=[]
        dfs(root2)
        s2 = seq[:]
        return s1==s2
        