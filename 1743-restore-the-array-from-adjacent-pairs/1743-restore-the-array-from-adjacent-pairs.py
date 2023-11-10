class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
#       Convert the adjacent pairs to an adjacency list
        adj = defaultdict(list)
        for x, y in adjacentPairs:
            adj[x].append(y)
            adj[y].append(x)
#       Find the start element
        start = None
        for key in adj:
            if len(adj[key])==1:
                start = key
                break
        visited = set([start])
        ans = [start]
        n = len(adj.keys())
        while len(ans)<n:
            for adj_ele in adj[start]:
                if adj_ele not in visited:
                    start = adj_ele
                    ans.append(start)
                    visited.add(start)
                    break
        return ans
        
        
                