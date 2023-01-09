# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        st = [root]
        while st:
            curr = st.pop()
            if curr:
                ans.append(curr.val)
                st.append(curr.right)
                st.append(curr.left)
        return ans
        