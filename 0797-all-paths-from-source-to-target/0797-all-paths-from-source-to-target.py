class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # dfs
        n = len(graph)
        stack = [([0], set())]
        paths = []
        # till the stack is not empty
        while stack!=[]:
        # path, visited = pop from the stack
            path_orig, visited_orig = stack.pop()
        # set curr_node to last element in the path
            curr_node = path_orig[-1]
        # for neighbors of last element, iterate over adjacent nodes, 
            for neighbor in graph[curr_node]:
        # if it is not visited, visit it, add it to path, and add the path to stack
                path = path_orig.copy()
                visited = visited_orig.copy()
                if neighbor not in visited:
                    visited.add(neighbor)
                    path.append(neighbor)
                    if neighbor == n-1:
                        paths.append(path)
                    else:
                        stack.append((path, visited))
        # if the current node is end node (n-1), append path to paths
        # return ans
        return paths
        