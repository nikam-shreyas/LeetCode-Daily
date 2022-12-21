from collections import deque
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def bfs(node):
            queue = deque([node])
            color[node] = 0
            while queue:
                curr = queue.popleft()
                for neighbor in adjlist[curr]:
                    if color[neighbor]==color[curr]:
                        return False
                        
                    if color[neighbor]==-1:
                        color[neighbor] = 1 - color[curr]
                        queue.append(neighbor)
                        
            return True
        
        adjlist = [[] for _ in range(n+1)]
        for x, y in dislikes:
            adjlist[x].append(y)
            adjlist[y].append(x)
            
        color = [-1]*(n+1)
        for i in range(1, n+1):
            if color[i]==-1:
                if not bfs(i):
                    return False
        return True
        
                        
                
        
                        