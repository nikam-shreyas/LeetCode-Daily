from collections import defaultdict
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        adjlist = defaultdict(list)
        for x, y in enumerate(edges):
            adjlist[x].append(y)
        path1 = {}
        path2 = {}
        def bfs(node, visited, dist, path):
            if node in path:
                path[node]=min(dist, path[node])
            else:
                path[node]=dist
            if node in visited:
                return
            visited.add(node)
            for nextnode in adjlist[node]:
                if nextnode not in visited:
                    bfs(nextnode, visited, dist+1, path)
    
        bfs(node1, set(), 0, path1)
        bfs(node2, set(), 0, path2)
        ans = []
        for i in path1:
            if i in path2:
                ans.append((max(path1[i], path2[i]), i))
        ans.sort()
        return ans[0][1] if ans else -1
