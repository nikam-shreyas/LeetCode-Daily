# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans=[]
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.ans = []
        def recurse(root):
            if root is not None:
                recurse(root.left)
                self.ans.append(root.val)
                recurse(root.right)
        recurse(root)
        res = []
        for i in range(1, len(self.ans)):
            res.append(self.ans[i]-self.ans[i-1])
        return min(res)
            
            