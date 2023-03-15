from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        queue = deque([root])
        flag = False
        while queue:
            n = len(queue)
            for i in range(n):
                curr = queue.popleft()
                if curr.left is None:
                    flag=True
                else:
                    if flag:
                        return False
                    queue.append(curr.left)
                if curr.right is None:
                    flag=True
                else:
                    if flag:
                        return False
                    queue.append(curr.right)               
        return True
                    