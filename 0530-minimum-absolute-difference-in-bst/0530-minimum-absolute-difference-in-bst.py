# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        tree=[]
        def inorder(root):
            nonlocal tree
            if root:
                inorder(root.left)
                tree.append(root.val)
                inorder(root.right)
        inorder(root)
        minval = tree[1]-tree[0]
        for i in range(1, len(tree)):
            minval = min(minval, tree[i]-tree[i-1])
        return minval
            
                