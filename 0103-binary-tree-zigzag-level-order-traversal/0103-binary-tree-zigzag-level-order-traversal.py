# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = 1
        if root is None:
            return []
        q = [root]
        ans = []
        while q:
            q1 = q[:]
            if d==1:    
                ans.append([node.val for node in q1])
            else:           
                ans.append([node.val for node in q1[::-1]])
            q = []
            while q1:
                curr = q1.pop(0)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                # else:
                #     if curr.right:
                #         q.append(curr.right)                    
                #     if curr.left:
                #         q.append(curr.left)
                    
            d = -d
        return ans