class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        stack = [([0], set())]
        ans = []
        n = len(graph)
        while stack:
            path_orig, visited_orig = stack.pop()
            curr = path_orig[-1]
            for neighbor in graph[curr]:
                path = path_orig[:]
                visited = visited_orig.copy()
                if neighbor not in visited:
                    path.append(neighbor)
                    visited.add(neighbor)
                    if neighbor==n-1:
                        ans.append(path)
                    else:
                        stack.append((path, visited))
        return ans
        