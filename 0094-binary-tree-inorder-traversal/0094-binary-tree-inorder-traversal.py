# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return []
        st = [root]
        i = 0
        while st:
            curr = st.pop()
            if isinstance(curr, int):
                ans.append(curr)
            else:
                if curr.right:
                    st.append(curr.right)
                st.append(curr.val)
                if curr.left:
                    st.append(curr.left)
        return ans
                    
        