# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        def recurse(root):
            if root:
                leftval, leftcount = recurse(root.left)
                rightval, rightcount = recurse(root.right)
                if root.val==floor((leftval+rightval+root.val)/(leftcount+rightcount+1)):
                    self.count+=1
                elif root.val==0 and leftval==rightval==0:
                    self.count+=1
                return leftval+rightval+root.val, leftcount+rightcount+1
            return 0, 0
        recurse(root)
        return self.count
            