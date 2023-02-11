from collections import defaultdict
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red = defaultdict(list)
        blue = defaultdict(list)
        for x, y in redEdges:
            red[x].append(y)
        for x, y in blueEdges:
            blue[x].append(y)
        ans = [inf for i in range(n)]
        queue = [(0, 1, 0), (0, 0, 0)]
        visited = set()
        # blue = 1, red = 0
        while queue:
            print(queue)
            curr = queue.pop(0)
            if (curr[0], curr[1]) in visited:
                continue
            visited.add((curr[0], curr[1]))
            ans[curr[0]]=min(ans[curr[0]], curr[2])
            if curr[1]==1:
                for n in red[curr[0]]:
                    queue.append((n, 0, curr[2]+1))
            else:
                for n in blue[curr[0]]:
                    queue.append((n, 1, curr[2]+1))
        for index, dist in enumerate(ans):
            if dist==inf:
                ans[index]=-1
        return ans
                    