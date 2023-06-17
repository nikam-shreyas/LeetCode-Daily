# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maxval = -inf
        queue = deque([root])
        level = 1
        maxlevel = 1
        while queue:
            n = len(queue)
            levelsum = 0
            for i in range(n):
                curr = queue.popleft()
                levelsum+=curr.val
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            if maxval<levelsum:
                maxval = levelsum
                maxlevel = level
            level+=1
        return maxlevel
        
        