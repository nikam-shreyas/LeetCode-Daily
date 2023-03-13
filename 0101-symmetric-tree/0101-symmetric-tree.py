# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def ispalindrome(arr):
            n = len(arr)
            for i in range(n//2):
                if arr[i]!=arr[n-i-1]:
                    return False
            return True
        
        queue = deque([root])
        while queue:
            n = len(queue)
            arr = []
            for i in range(n):
                curr = queue.popleft()
                if curr:
                    arr.append(curr.val)
                    if curr.left:
                        queue.append(curr.left)
                    else:
                        queue.append(None)
                    if curr.right:
                        queue.append(curr.right)
                    else:
                        queue.append(None)
                else:
                    arr.append(None)
            print(arr)
            if not ispalindrome(arr):
                return False
        return True