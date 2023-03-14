# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        numbers= []
        def recurse(num, root):
            if root is None:
                numbers.append(num)
                return
            sum_=0
            num+=root.val
            if root.left is None and root.right is None:
                numbers.append(num)
            if root.left:
                recurse(num*10, root.left)
            if root.right:
                recurse(num*10, root.right)
            
        recurse(0, root)
        # print(numbers)
        return sum(numbers)