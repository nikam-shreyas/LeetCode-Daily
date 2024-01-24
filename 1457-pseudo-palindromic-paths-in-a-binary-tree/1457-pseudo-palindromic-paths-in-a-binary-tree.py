# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.count = 0
        def isPPP(counter):
            evens = 0
            odds = 0
            for k, v in counter.items():
                if v%2==0:
                    evens+=1
                else:
                    odds+=1
            if odds<2:
                self.count+=1
            
        d = defaultdict(int)
        def recurse(root):
            if not root:
                return
            if root.left is None and root.right is None:
                d[root.val]+=1
                isPPP(d)
                d[root.val]-=1
                return
            d[root.val]+=1
            recurse(root.left)
            recurse(root.right)
            d[root.val]-=1
        recurse(root)
        return self.count
            