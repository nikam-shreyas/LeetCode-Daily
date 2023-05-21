class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for eq, val in zip(equations, values):
            a, b = eq
            adj[a].append((b, val))
            adj[b].append((a, 1/val))
            
        ans = []
        def bfs(start, end):
            if start not in adj or end not in adj:
                return -1.0
            queue = deque([(start, 1)])
            visited = set()
            while queue:
                n = len(queue)
                for i in range(n):
                    curr, val = queue.popleft()
                    visited.add(curr)
                    for nextnode, nextval in adj[curr]:
                        if nextnode==end:
                            adj[start].append((end, val*nextval))
                            return val*nextval
                        if nextnode not in visited:
                            queue.append((nextnode, val*nextval))
            return -1.0
        for c, d in queries:
            ans.append(bfs(c, d))
        return ans
                            
            
        