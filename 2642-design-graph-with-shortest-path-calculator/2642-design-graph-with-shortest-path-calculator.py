from heapq import heapify, heappop, heappush
class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.adj = defaultdict(list)
        for start, end, cost in edges:
            self.adj[start].append((end, cost))

    def addEdge(self, edge: List[int]) -> None:
        start, end, cost = edge
        self.adj[start].append((end, cost))
        

    def shortestPath(self, node1: int, node2: int) -> int:
        h = [(0, node1)]
        heapify(h)
        visited = set()
#         print()
#         print(self.adj)
#         print(node1, node2)
        
        while h:
            curr_cost, curr_node = heappop(h)
            print(curr_node, curr_cost)
            if curr_node==node2:
                return curr_cost
            else:
                for next_node, edge_cost in self.adj[curr_node]:
                    if (curr_node, next_node) not in visited:
                        visited.add((curr_node, next_node))
                        heappush(h, (edge_cost+curr_cost, next_node))
        return -1
                        
                    
                    
        
        


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)