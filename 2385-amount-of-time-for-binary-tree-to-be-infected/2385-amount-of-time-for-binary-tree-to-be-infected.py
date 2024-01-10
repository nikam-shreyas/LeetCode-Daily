# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        adj = defaultdict(list)
        def recurse(root):
            if root.left:
                adj[root.val].append(root.left.val)
                adj[root.left.val].append(root.val)
                recurse(root.left)
            if root.right:
                adj[root.val].append(root.right.val)
                adj[root.right.val].append(root.val)
                recurse(root.right)
        if root:
            recurse(root)
        queue = deque([start])
        visited = set([start])
        time = -1
        while queue:
            n = len(queue)
            for i in range(n):
                curr_node = queue.popleft()
                for next_node in adj[curr_node]:
                    if next_node not in visited:
                        visited.add(next_node)
                        queue.append(next_node)
            time+=1
        return time