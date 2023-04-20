# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = defaultdict(list)
        def bfs(root, level, prev, child):
            if not root:
                return
            # print(level, root.val)
            if child=='left':
                ans[level].append(prev*2)                
                if root.left:
                    bfs(root.left, level+1, prev*2, 'left')
                if root.right:
                    bfs(root.right, level+1, prev*2, 'right')
            else:
                ans[level].append(prev*2+1)
                if root.left:
                    bfs(root.left, level+1, prev*2+1, 'left')
                if root.right:
                    bfs(root.right, level+1, prev*2+1, 'right')
        if not root:
            return 0
        bfs(root.left, 1, 1, 'left')
        bfs(root.right, 1, 1, 'right')
        # print(ans)
        maxwidth = 0
        for level in ans:
            maxwidth = max(maxwidth, max(ans[level])-min(ans[level]))
        return maxwidth+1
        
            
        